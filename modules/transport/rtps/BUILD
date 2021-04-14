load("@rules_cc//cc:defs.bzl", "cc_library", "cc_test")
load("//tools:cpplint.bzl", "cpplint")

package(default_visibility = ["//visibility:public"])

cc_library(
    name = "attributes_filler",
    srcs = ["attributes_filler.cc"],
    hdrs = ["attributes_filler.h"],
    deps = [
        "//modules/common:log",
        "//modules/transport/qos",
        "@fastrtps",
    ],
)

cc_library(
    name = "underlay_message",
    srcs = ["underlay_message.cc"],
    hdrs = ["underlay_message.h"],
    deps = [
        "//modules/common:log",
        "@fastcdr",
    ],
)

cc_library(
    name = "participant",
    srcs = ["participant.cc"],
    hdrs = ["participant.h"],
    deps = [
        ":underlay_message",
        ":underlay_message_type",
        "//modules/common:global_data",
    ],
)

cc_library(
    name = "sub_listener",
    srcs = ["sub_listener.cc"],
    hdrs = ["sub_listener.h"],
    deps = [
        ":underlay_message",
        ":underlay_message_type",
        "//modules/transport/message:message_info",
    ],
)

cc_library(
    name = "underlay_message_type",
    srcs = ["underlay_message_type.cc"],
    hdrs = ["underlay_message_type.h"],
    deps = [
        ":underlay_message",
        "@fastcdr",
        "@fastrtps",
    ],
)

cc_test(
    name = "rtps_test",
    size = "small",
    srcs = ["rtps_test.cc"],
    deps = [
        "//modules:cyber_core",
        "@com_google_googletest//:gtest_main",
        "@fastcdr",
    ],
)

cpplint()
