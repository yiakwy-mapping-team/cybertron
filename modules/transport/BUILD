load("@rules_cc//cc:defs.bzl", "cc_library", "cc_test")
load("//tools:cpplint.bzl", "cpplint")

package(default_visibility = ["//visibility:public"])

cc_library(
    name = "transport",
    srcs = ["transport.cc"],
    hdrs = ["transport.h"],
    deps = [
        "//modules/service_discovery:role",
        "//modules/task",
        "//modules/transport/dispatcher:intra_dispatcher",
        "//modules/transport/dispatcher:rtps_dispatcher",
        "//modules/transport/dispatcher:shm_dispatcher",
        "//modules/transport/message:history",
        "//modules/transport/qos",
        "//modules/transport/receiver",
        "//modules/transport/rtps:attributes_filler",
        "//modules/transport/rtps:participant",
        "//modules/transport/rtps:sub_listener",
        "//modules/transport/rtps:underlay_message",
        "//modules/transport/rtps:underlay_message_type",
        "//modules/transport/transmitter",
        "@fastrtps",
    ],
)

cc_test(
    name = "transport_test",
    size = "small",
    srcs = ["transport_test.cc"],
    deps = [
        "//modules:cyber_core",
        "//modules/proto:unit_test_cc_proto",
        "@com_google_googletest//:gtest",
    ],
)

cpplint()
