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

## import libraries
source installers/installer_base.sh

## API

# check if the command running in guest machine
is_in_container() {
  if [ -f /.dockerenv ]; then
    return 0
  else
    return -1
  fi
}


## export automation toolkits API for subshells

export -f is_in_container

# cyber_rt is released with apolloauto main line

# add apollo dist env
APOLLO_DIST_DIR=/opt/apollo

if [ ! -d $APOLLO_DIST_DIR/rcfiles ]; then
  cp -r rcfiles $APOLLO_DIST_DIR
fi

sudo bash installers/install_minimal_environment.sh $GEOLOC
# use our cmake comment the following lines if you want install cmake
# bash installers/install_cmake.sh
bash installers/install_cyber_deps.sh $INSTALL_MODE
bash installers/install_llvm_clang.sh
bash installers/install_qa_tools.sh
bash installers/install_visualizer_deps.sh
if [ is_in_container == 0 ]; then
  warn "outside of container, unset QT5_PATH and QT_QPA_PLATFORM_PLUGIN_PATH to avoid conflicts with existing software"
  unset QT5_PATH 
  unset QT_QPA_PLATFORM_PLUGIN_PATH
fi
bash installers/install_bazel.sh
bash installers/post_install.sh $BUILD_STAGE
