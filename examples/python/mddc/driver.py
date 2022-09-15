import time
from datetime import datetime

import cyber
from simple_sensor_image_pb2 import ImgShape as ImgShapeMsg, RawImage as RawImageMsg
from simple_sensor_lidar_pb2 import PointXYZI as PointXYZIMsg, PointCloud as PointCloudMsg

import numpy as np
import cv2
import base64

from utils import async_logging_info

class DDC:
    def __init__(self):
        self._seq = -1

    def Poll(self):
        raise NotImplementedError

    def seq(self):
        self._seq += 1
        return self._seq


# Note this class is python wrapper used for unit test/integration test to mock the behavior of a camera
class MockedCamera:

    H = 255
    W = 255
    C = 3

    # no distor rectify parameters

    # 
    fps = 60
    cam_latency = 1.0 / fps

    def __init__(self, cam_type):
        self.cam_type = cam_type

    # create an image
    def capture(self, cam_idx=0, batches=1):
        # create python cv2 (bgr) image, CVU8
        img = (np.random.standard_normal(size=(batches, self.H, self.W, self.C)) * 255).astype(np.uint8)
        return img

# Note this class is python wrapper used for unit test/integration test to mock the behavior of a lidar
class MockedLidar:

    N = 1024
    C = 4

    # lidar unwarp info

    # dump to PCD asynchronously?
    isDumpedPCD = False

    # reference pose trajectory
    trajectory = None

    fps = 10

    def __init__(self, lidar_type):
        self.lidar_type = lidar_type

    def scan(self):
        pc = np.random.randn(self.C, self.N)
        pc /= np.linalg.norm(pc, axis=0)
        return pc

class MockedLidarNet:

    numOfDevices = 1

    def __init__(self):
        self.devices = [MockedLidar("MockedMemsLidar")]

    def scan(self, lidar_idx=0):
        return self.devices[lidar_idx].scan()


# A mocked camera DDC
class MockCameraEndPoint(DDC):

    def __init__(self):
        super(type(self), self).__init__()
        self.endpoint = cyber.Node("MockCameraEndPoint")
        self.qos_depth = 10
        # the writer will create transmitter to pass massages to another endpoint's receiver
        self.writer = self.endpoint.create_writer("cam:0", RawImageMsg, self.qos_depth)
        self.cam = MockedCamera("MonoRGB")

    # TODO (yiakwy) : polling asynchronously with asyncio
    def Poll(self):
        img = self.cam.capture(0)[0] 
        time.sleep(self.cam.cam_latency)
        return img

    # mock method
    def DistributeImages(self):
        now = datetime.now()
        img = self.Poll()

        # create image with time compensation
        img = self.rectify(img)

        # create img message
        msg = RawImageMsg()

        msg.timestamp = int(round(now.timestamp()))
        msg.frame_id = "CameraFrame#{}".format(self.seq())

        shape = ImgShapeMsg()
        shape.H = img.shape[0]
        shape.W = img.shape[1]
        shape.C = img.shape[2]

        msg.shape.CopyFrom(shape)

        msg.data = self.encode(img)

        async_logging_info("writing MSG#{}...".format(msg.frame_id))
        self.writer.write(msg)
        delta = datetime.now() - now
        async_logging_info("complete writing MSG#{}, elapsed {}".format(msg.frame_id, delta))

    def encode(self, img):
        return img.tobytes()

    # mocked rectify with cam intrinsic values
    def rectify(self, img):
        return img


class MockedLidarNetEndPoint(DDC):

    def __init__(self):
        super(type(self), self).__init__()
        self.endpoint = cyber.Node("MockedLidarNet")
        self.qos_depth = 10
        self.writer = self.endpoint.create_writer("lidar:0", PointCloudMsg, self.qos_depth)
        self.lidar_net = MockedLidarNet()
        self._seq = -1
        pass

    # TODO (yiakwy) : polling asynchronously with asyncio
    def Poll(self):
        pc = self.lidar_net.scan(0)
        # lidar usually accumulate scanning data within 0.1 s
        # it is your response to unwarp the data if you are moving fast
        time.sleep(0.1)
        return pc

    def DistributePointCloud(self):
        now = datetime.now()
        pc = self.Poll()

        # unwarp point cloud, this could be done asynchronously in host side
        unwarped_pc = self.unwarp(pc)

        msg = PointCloudMsg()
        msg.timestamp = int(round(now.timestamp()))
        msg.frame_id = "LidarFrame#{}".format(self.seq())
        msg.width = pc.shape[0]
        msg.height = pc.shape[1]

        for i in range(pc.shape[0]):
            p = PointXYZIMsg()
            p.x = pc[i,0]
            p.y = pc[i,1]
            p.z = pc[i,2]
            msg.points.append(p)

        async_logging_info("writing MSG#{}...".format(msg.frame_id))
        self.writer.write(msg)
        delta = datetime.now() - now
        async_logging_info("complete writing MSG#{}, elapsed {}".format(msg.frame_id, delta))

    # mocked unwarp lidar points with motion compensation
    def unwarp(self, pc):
        return pc


# Multiple data distribute control
class MDDCDriver:

    def __init__(self):
        self.camera_ddc = MockCameraEndPoint()
        self.lidarnet_ddc = MockedLidarNetEndPoint()

        self.Init()

    def Init(self):
        # parse config manager

        # parse flags

        self.hz = 60
        pass

    def DistributeData(self):
        self.camera_ddc.DistributeImages()
        self.lidarnet_ddc.DistributePointCloud()