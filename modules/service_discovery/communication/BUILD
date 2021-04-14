load("@rules_cc//cc:defs.bzl", "cc_library")
load("//tools:cpplint.bzl", "cpplint")

package(default_visibility = ["//visibility:public"])

cc_library(
    name = "participant_listener",
    srcs = ["participant_listener.cc"],
    hdrs = ["participant_listener.h"],
    deps = [
        "//modules/common:log",
        "@fastrtps",
    ],
)

cc_library(
    name = "subscriber_listener",
    srcs = ["subscriber_listener.cc"],
    hdrs = ["subscriber_listener.h"],
    deps = [
        "//modules/common:log",
        "//modules/transport/rtps:underlay_message",
        "//modules/transport/rtps:underlay_message_type",
        "@fastrtps",
    ],
)

cpplint()
