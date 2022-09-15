import cyber
from simple_sensor_image_pb2 import ImgShape as ImgShapeMsg, RawImage as RawImageMsg
from simple_sensor_lidar_pb2 import PointCloud as PointCloudMsg

from utils import async_logging_info

import time

# used to synchronize data fetched from Python API.
# the data will be fused and directed to **proc**
class DataVisitor:
    pass

class Component:
    pass

# in python API you must create Reader explicitly by yourself
# while in C++ API, the scheduler will create reader for you automatically
class MultiInputDetectionComponent(Component):

    def __init__(self):
        self._implicit_sub = cyber.Node("subscriber")
        self.data_visitor = DataVisitor()
        
        # subscribe
        self.lidar_reader = self._implicit_sub.create_reader("lidar:0", PointCloudMsg, self.onLidarScan)
        self.cam_reader = self._implicit_sub.create_reader("cam:0", RawImageMsg, self.onCamCapture)

    # TODO (yiakwy) : initialize event registration
    def Init(self):
        pass

    # TODO (yiakwy) : read fused data from data visitor
    def Proc(self, pointCloud, image):
        pass

    # user defined data fusion interface

    def onLidarScan(self, lidarMsg):
        # TODO(yiakwy) write to data visitor
        async_logging_info("fetch lidar message Msg#{}, decode it and feed it to dataVisitor...".format(lidarMsg.frame_id))
        
        # mock
        time.sleep(3)
        pass

    def onCamCapture(self, camMsg):
        # TODO(yiakwy) write to data visitor
        async_logging_info("fetch lidar message Msg#{}, decode it and feed it to dataVisitor...".format(camMsg.frame_id))
        
        # mock 
        time.sleep(3)
        pass

    def spin(self):
        self._implicit_sub.spin()


