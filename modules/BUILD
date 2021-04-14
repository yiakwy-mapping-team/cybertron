load("@rules_cc//cc:defs.bzl", "cc_library")
load("//tools/install:install.bzl", "install")
load("//tools:cpplint.bzl", "cpplint")

package(default_visibility = ["//visibility:public"])

cc_library(
    name = "cyber",
    linkstatic = False,
    deps = [
        ":cyber_core",
    ],
)

install(
    name = "install",
    data = [
        ":.release.bash",
        ":cyber_conf",
    ],
    rename = {
        "modules/.release.bash": "setup.bash",
    },
    deps = [
        "//modules/mainboard:install",
        "//modules/tools:install",
    ],
)

cc_library(
    name = "binary",
    srcs = ["binary.cc"],
    hdrs = ["binary.h"],
)

cc_library(
    name = "state",
    srcs = ["state.cc"],
    hdrs = ["state.h"],
    deps = [
        "//modules/common",
    ],
)

cc_library(
    name = "init",
    srcs = ["init.cc"],
    hdrs = ["init.h"],
    deps = [
        "//modules:binary",
        "//modules:state",
        "//modules/common:file",
        "//modules/logger:async_logger",
        "//modules/node",
        "//modules/proto:clock_cc_proto",
        "//modules/sysmo",
        "//modules/time:clock",
        "//modules/timer:timing_wheel",
    ],
)

cc_library(
    name = "cyber_core",
    srcs = ["cyber.cc"],
    hdrs = ["cyber.h"],
    linkopts = ["-lrt"],
    deps = [
        "//modules:binary",
        "//modules:init",
        "//modules:state",
        "//modules/base",
        "//modules/blocker:blocker_manager",
        "//modules/class_loader",
        "//modules/class_loader:class_loader_manager",
        "//modules/common",
        "//modules/component",
        "//modules/component:timer_component",
        "//modules/croutine",
        "//modules/data",
        "//modules/event:perf_event_cache",
        "//modules/io",
        "//modules/logger",
        "//modules/logger:async_logger",
        "//modules/message:message_traits",
        "//modules/message:protobuf_traits",
        "//modules/message:py_message_traits",
        "//modules/message:raw_message_traits",
        "//modules/node",
        "//modules/parameter:parameter_client",
        "//modules/parameter:parameter_server",
        "//modules/proto:run_mode_conf_cc_proto",
        "//modules/record",
        "//modules/scheduler",
        "//modules/scheduler:scheduler_factory",
        "//modules/service",
        "//modules/service:client",
        "//modules/service_discovery:topology_manager",
        "//modules/sysmo",
        "//modules/task",
        "//modules/time",
        "//modules/time:clock",
        "//modules/time:duration",
        "//modules/time:rate",
        "//modules/timer",
        "//modules/transport",
        "//modules/transport/rtps:participant",
        "//modules/transport/rtps:sub_listener",
        "@com_github_google_glog//:glog",
        "@com_google_protobuf//:protobuf",
        "@fastrtps",
    ],
)

filegroup(
    name = "cyber_conf",
    srcs = glob([
        "conf/*.conf",
    ]),
)

cpplint()
