load("@rules_cc//cc:defs.bzl", "cc_binary")
load("//tools/install:install.bzl", "install")
load("//tools:cpplint.bzl", "cpplint")

package(default_visibility = ["//visibility:public"])

cc_binary(
    name = "talker",
    srcs = ["talker.cc"],
    deps = [
        "//modules:cyber",
        "//modules/examples/proto:examples_cc_proto",
    ],
)

cc_binary(
    name = "listener",
    srcs = ["listener.cc"],
    deps = [
        "//modules:cyber",
        "//modules/examples/proto:examples_cc_proto",
    ],
)

install(
    name = "install",
    targets = [
        ":talker",
        ":listener",
    ],
    runtime_dest = "modules/examples",
    deps = [
        "//modules/examples/common_component_example:install",
        "//modules/examples/timer_component_example:install",
    ],
)

cc_binary(
    name = "paramserver",
    srcs = ["paramserver.cc"],
    deps = [
        "//modules:cyber",
        "//modules/parameter",
    ],
)

cc_binary(
    name = "service",
    srcs = ["service.cc"],
    deps = [
        "//modules:cyber",
        "//modules/examples/proto:examples_cc_proto",
    ],
)

cc_binary(
    name = "record",
    srcs = ["record.cc"],
    deps = [
        "//modules:cyber",
        "//modules/proto:record_cc_proto",
    ],
)

cpplint()
