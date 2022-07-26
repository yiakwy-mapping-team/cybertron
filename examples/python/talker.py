import time
from datetime import datetime

import cyber
import cyber_time
from proto.unit_test_pb2 import ChatterBenchmark

def async_logging_info(msg):
    # TODO (yiakwy) : add async logger
    print("[PyTalker] {}".format(msg))

def startTalker():
    msg = ChatterBenchmark()
    seq = 0

    # a node wrapper of PyNode (wrapper of appllo::cyber::Node)
    node = cyber.Node("py_talker")

    # std::unique_ptr<PyWriter> pw(
    #     node.create_writer("channel/chatter", msgChat->GetTypeName(), 10));
    writer = node.create_writer("channel/pychatter", ChatterBenchmark, 10)

    # handle signal
    pollFreq = 10 # Hz
    # wrapper of cyber::Rate
    cyber_rate = cyber_time.Rate(pollFreq)
    while not cyber.is_shutdown():
        now = datetime.now()
        msg.content = "Hello, this is python msg publisher, sending heart beating..."
        msg.stamp = int(round(now.timestamp()))
        msg.seq = seq
        async_logging_info("writing MSG#{}...".format(seq))
        writer.write(msg)
        delta = datetime.now() - now
        async_logging_info("complete writing MSG#{}, elapsed {}".format(seq, delta))
        seq = seq + 1
        cyber_rate.sleep()
        time.sleep(3)

# Note this class is python wrapper used for unit test/integration test to mock the behavior of a camera
class MockedCamera:
    pass

class MockCameraEndPoint(cyber.Node):
    pass

def sendImages():
    pass

# Multiple data distribute control
class MDDC:
    pass

if __name__ == "__main__":
    print("start talker node ...")

    # wrapper of _CYBER .py_init (also wrapper of appollo::cyber::init)
    cyber.init()

    # create a talker node
    startTalker()

    print("clear down...")
    cyber.shutdown()