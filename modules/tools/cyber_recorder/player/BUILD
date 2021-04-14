load("@rules_cc//cc:defs.bzl", "cc_library")
load("//tools:cpplint.bzl", "cpplint")

package(default_visibility = ["//visibility:public"])

cc_library(
    name = "play_param",
    hdrs = ["play_param.h"],
)

cc_library(
    name = "play_task",
    srcs = ["play_task.cc"],
    hdrs = ["play_task.h"],
    deps = [
        "//modules/common:log",
        "//modules/message:raw_message",
        "//modules/node:writer",
    ],
)

cc_library(
    name = "play_task_buffer",
    srcs = ["play_task_buffer.cc"],
    hdrs = ["play_task_buffer.h"],
    deps = [
        ":play_task",
    ],
)

cc_library(
    name = "play_task_consumer",
    srcs = ["play_task_consumer.cc"],
    hdrs = ["play_task_consumer.h"],
    deps = [
        ":play_task_buffer",
        "//modules/common:log",
        "//modules/time",
    ],
)

cc_library(
    name = "play_task_producer",
    srcs = ["play_task_producer.cc"],
    hdrs = ["play_task_producer.h"],
    deps = [
        ":play_param",
        ":play_task_buffer",
        "//modules:cyber",
        "//modules/common:log",
        "//modules/message:protobuf_factory",
        "//modules/message:raw_message",
        "//modules/node",
        "//modules/node:writer",
        "//modules/record:record_reader",
        "//modules/record:record_viewer",
    ],
)

cc_library(
    name = "player",
    srcs = ["player.cc"],
    hdrs = ["player.h"],
    deps = [
        ":play_param",
        ":play_task_buffer",
        ":play_task_consumer",
        ":play_task_producer",
        "//modules:init",
    ],
)

cpplint()
