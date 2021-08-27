# adpated from cyber_rt dockerfile

set -e

if [[ $EUID -ne 0 ]]; then
  echo "$0: must be root" 1>&2
  exit 1
fi

cd "$(dirname "$BASH_SOURCE[0]")/../scripts"

GEOLOC=cn # (cn, us)
INSTALL_MODE=download
CLEAN_DEPS=false

BUILD_STAGE=cyber
IS_IN_DOCKER=

## import libraries
source installers/installer_base.sh

## API

# check if the command running in guest machine
function is_in_container() {
  if [ -f /.dockerenv ]; then
    echo "true"
  else
    echo "false"
  fi
}


## export automation toolkits API for subshells

export -f is_in_container

is_in_container

IS_IN_DOCKER=$(is_in_container)
export IS_IN_DOCKER=$IS_IN_DOCKER

if [ "$IS_IN_DOCKER" == "true" ];then
  info "Inside docker container $CONTAINER"
else
  info "Outside of docker container."
fi

info "Please check your cuda installation in advance"
info "Here is example for cuda 10.2: https://gitlab.com/nvidia/container-images/cuda/-/blob/master/dist/10.2/ubuntu18.04/devel/Dockerfile"

# cyber_rt is released with apolloauto main line

# add apollo dist env
APOLLO_DIST_DIR=/opt/apollo

if [ ! -d $APOLLO_DIST_DIR/rcfiles ]; then
  cp -r rcfiles $APOLLO_DIST_DIR
fi

bash installers/install_minimal_environment.sh $GEOLOC
# use our cmake comment the following lines if you want install cmake
## bash installers/install_cmake.sh
bash installers/install_cyber_deps.sh $INSTALL_MODE
bash installers/install_llvm_clang.sh
bash installers/install_qa_tools.sh
bash installers/install_visualizer_deps.sh
if [ "$IS_IN_DOCKER" == "false" ]; then
  warn "outside of container, unset QT5_PATH and QT_QPA_PLATFORM_PLUGIN_PATH to avoid conflicts with existing software"
  unset QT5_PATH 
  unset QT_QPA_PLATFORM_PLUGIN_PATH
fi
bash installers/install_bazel.sh
bash installers/post_install.sh $BUILD_STAGE
