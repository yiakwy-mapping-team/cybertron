import importlib
import os
import sys

# loading cyber lib, make sure u have run gen_cyber_api.sh
CYBER_ROOT=os.path.join(os.path.dirname(__file__), "../..")
CYBER_LIBS_PATH=os.path.join(os.path.dirname(__file__), "../../cybertron_api")

# TODO(yiakwy) : verify the destination
wrapper_lib_path = "{}/libs/modules/python/internal".format(CYBER_LIBS_PATH)
wrapper_lib_path = os.path.abspath(wrapper_lib_path)

sys.path.append(wrapper_lib_path)

# step 1
# TODO(yiakwy) : verify the dynamic loading
# to make sure loading the cyber sucessfully
try:
    _CYBER = importlib.import_module("_cyber_wrapper")
except:
    print("CYBER LIB PATH {} is not valid", CYBER_LIBS_PATH)
    exit(-1)

print("Cyber lib {} is loaded".format(_CYBER))

# step 2
# add python path to python/cyber_py3
cyber_python_path="{}/modules/python/cyber_py3".format(CYBER_ROOT)
cyber_python_path=os.path.abspath(cyber_python_path)
sys.path.append(cyber_python_path)

cyber_python_path_ext="{}/python/modules".format(CYBER_LIBS_PATH)
cyber_python_path_ext=os.path.abspath(cyber_python_path_ext)
sys.path.append(cyber_python_path_ext)

# step 3
# equivalent to import python package cyber compiled by bazel system from CYBER_ROOT
# from cyber.python.cyber_py3 import cyber

# step 4
# add protobuf path
# import proto as Proto
demo_proto_python_client_path="{}/examples/proto".format(CYBER_ROOT)
sys.path.append(demo_proto_python_client_path)


if __name__ == "__main__":
    import cyber

    # wrapper of _CYBER.py_init (also wrapper of appollo::cyber::init)
    cyber.init()

    if not cyber.ok():
        print('Well, something went wrong.')
        sys.exit(1)

    cyber.shutdown()
