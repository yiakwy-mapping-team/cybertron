import cyber
import cyber_time

import os
import sys

# simply for test
from proto.unit_test_pb2 import ChatterBenchmark

sys.path.insert(0, os.path.dirname(__file__))

# real mddc python demo
from .mddc import MultiInputDetectionComponent
from .utils import async_logging_info

DEBUG = False
if 'DEBUG' in os.envrion and OS.envrion['DEBUG'] == 'True':
    DEBUG = True

def onMessage(msg):
    async_logging_info("="*80)
    async_logging_info("reading msg : {}".format(msg))

def startListener():
    node = cyber.Node("py_listener")
    reader = node.create_reader("channel/pychatter", ChatterBenchmark, onMessage)
    node.spin()

if __name__ == "__main__":
    print("start listener node ...")

    # wrapper of _CYBER.py_init (also wrapper of appollo::cyber::init)
    cyber.init()

    # start the client
    if DEBUG:
        startListener()
    else:
        pass
    
    cyber.shutdown()