ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# to meet requirement from $ROOT/third_party/py/
PYTHON3_BIN_PATH=$(which python)
export PYTHON3_BIN_PATH

PYTHON_LIBRARY=$(python -c "import distutils.sysconfig as sysconfig; print('%s/%s' %
(sysconfig.get_config_var('LIBDIR'), sysconfig.get_config_var('INSTSONAME')))")

echo "PYTHON_LIBRARY: $PYTHON_LIBRARY"
export PYTHON_LIBRARY=$PYTHON_LIBRARY
# to meet requirement from $ROOT/third_party/py/
export PYTHON3_LIB_PATH=$PYTHON_LIBRARY

PYTHON_INCLUDE_DIR=$(python -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())")

echo "PYTHON_INCLUDE_DIR: $PYTHON_INCLUDE_DIR"
export PYTHON_INCLUDE_DIR=$PYTHON_INCLUDE_DIR

export CUDA_TOOLKIT_ROOT_DIR="/usr/local/cuda"
export CUDA_HOME=$CUDA_TOOLKIT_ROOT_DIR

CMAKE_CUDA_COMPILER="$CUDA_HOME/bin/nvcc"
export CMAKE_CUDA_COMPILER=$CMAKE_CUDA_COMPILER

export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$ANACONDA_HOME/lib::$LD_LIBRARY_PATH

NOCMAKE_PATH=$PATH
PATH=$ROOT/scripts/cmake-3.16.0-Linux-x86_64/bin:$PATH
export PATH
export NOCMAKE_PATH

