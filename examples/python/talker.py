import time
from datetime import datetime
import os
import sys

import cyber
import cyber_time

# simply for test
from proto.unit_test_pb2 import ChatterBenchmark

sys.path.insert(0, os.path.dirname(__file__))

# real py Multi data distribution control (MDDC) test
from .mddc import MDDCDriver
from .utils import async_logging_info

DEBUG = False
if 'DEBUG' in os.environ and OS.environ['DEBUG'] == 'True':
    DEBUG = True

# simply for test
def startTalker():
    msg = ChatterBenchmark()
    seq = 0

    # a node wrapper of PyNode (wrapper of appllo::cyber::Node)
    node = cyber.Node("py_talker")
    qos_depth = 10

    # std::unique_ptr<PyWriter> pw(
    #     node.create_writer("channel/chatter", msgChat->GetTypeName(), qos_depth));
    writer = node.create_writer("channel/pychatter", ChatterBenchmark, qos_depth)

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
    
if __name__ == "__main__":
    print("start talker node ...")

    # wrapper of _CYBER .py_init (also wrapper of appollo::cyber::init)
    cyber.init()

    # create a talker node
    if DEBUG:
        startTalker()
    else:
        mddc_driver = MDDCDriver()

        cyber_rate = cyber_time.Rate(mddc_driver.hz)
        while not cyber.is_shutdown():
            mddc_driver.DistributeData()
            cyber_rate.sleep()

    print("clear down...")
    cyber.shutdown()