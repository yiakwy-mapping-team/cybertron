load("@rules_cc//cc:defs.bzl", "cc_binary", "cc_library", "cc_test")
load("//tools:cpplint.bzl", "cpplint")

package(default_visibility = ["//visibility:public"])

cc_library(
    name = "io",
    deps = [
        ":poll_data",
        ":poll_handler",
        ":poller",
        ":session",
    ],
)

cc_library(
    name = "poll_data",
    hdrs = ["poll_data.h"],
)

cc_library(
    name = "poll_handler",
    srcs = ["poll_handler.cc"],
    hdrs = ["poll_handler.h"],
    deps = [
        ":poll_data",
        ":poller",
        "//modules/common:log",
        "//modules/croutine",
    ],
)

cc_library(
    name = "poller",
    srcs = ["poller.cc"],
    hdrs = ["poller.h"],
    deps = [
        ":poll_data",
        "//modules/base:atomic_rw_lock",
        "//modules/common:log",
        "//modules/common:macros",
        "//modules/scheduler:scheduler_factory",
        "//modules/time",
    ],
)

cc_test(
    name = "poller_test",
    size = "small",
    srcs = ["poller_test.cc"],
    deps = [
        ":poller",
        "//modules:cyber_core",
        "@com_google_googletest//:gtest",
    ],
)

cc_library(
    name = "session",
    srcs = ["session.cc"],
    hdrs = ["session.h"],
    deps = [
        ":poll_handler",
        "//modules/common:log",
    ],
)

cc_binary(
    name = "tcp_echo_client",
    srcs = ["example/tcp_echo_client.cc"],
    deps = [
        "//modules:cyber_core",
    ],
)

cc_binary(
    name = "tcp_echo_server",
    srcs = ["example/tcp_echo_server.cc"],
    deps = [
        "//modules:cyber_core",
    ],
)

cc_binary(
    name = "udp_echo_client",
    srcs = ["example/udp_echo_client.cc"],
    deps = [
        "//modules:cyber_core",
    ],
)

cc_binary(
    name = "udp_echo_server",
    srcs = ["example/udp_echo_server.cc"],
    deps = [
        "//modules:cyber_core",
    ],
)

cpplint()
