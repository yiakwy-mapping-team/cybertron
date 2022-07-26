#! /usr/bin/env zsh
TOP_DIR="$(cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd)"
source ${TOP_DIR}/scripts/apollo.bashrc

export APOLLO_BAZEL_DIST_DIR="${APOLLO_CACHE_DIR}/distdir"
export CYBER_PATH="${APOLLO_ROOT_DIR}/modules"

bazel_bin_path="${TOP_DIR}/bazel-bin"

mainboard_path="${bazel_bin_path}/modules/mainboard"
cyber_tool_path="${bazel_bin_path}/modules/tools"
recorder_path="${cyber_tool_path}/cyber_recorder"
launch_path="${cyber_tool_path}/cyber_launch"
channel_path="${cyber_tool_path}/cyber_channel"
node_path="${cyber_tool_path}/cyber_node"
service_path="${cyber_tool_path}/cyber_service"
monitor_path="${cyber_tool_path}/cyber_monitor"
visualizer_path="${bazel_bin_path}/modules/tools/visualizer"

# TODO(all): place all these in one place and pathprepend
for entry in "${mainboard_path}" \
    "${recorder_path}" "${monitor_path}"  \
    "${channel_path}" "${node_path}" \
    "${service_path}" \
    "${launch_path}" \
    "${visualizer_path}" ; do
    echo "appending ${entry}..."
    # pathprepend "${entry}"
    export PATH=${entry}:$PATH
done

# pathprepend ${bazel_bin_path}/modules/python/internal PYTHONPATH
echo "adding python path ${bazel_bin_path}/modules/python/internal"
export PYTHONPATH=${bazel_bin_path}/modules/python/internal:$PYTHONPATH

export CYBER_DOMAIN_ID=80
export CYBER_IP=127.0.0.1

export GLOG_log_dir="${APOLLO_ROOT_DIR}/data/log"
echo "bazel_bin_path: $bazel_bin_path"
echo "APOLLO_ROOT_DIR: ${APOLLO_ROOT_DIR}"
export GLOG_alsologtostderr=1
export GLOG_colorlogtostderr=1
export GLOG_minloglevel=0

export sysmo_start=0

# for DEBUG log
#export GLOG_v=4
echo "CYBER_PATH: ${CYBER_PATH}"
source ${CYBER_PATH}/tools/cyber_tools_auto_complete.bash
