import cyber
import cyber_time

# simply for test
from proto.unit_test_pb2 import ChatterBenchmark

def async_logging_info(msg):
    # TODO (yiakwy) : add async logger
    print("[PyReader] {}".format(msg))

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
    startListener()
    
    cyber.shutdown()