load("@rules_cc//cc:defs.bzl", "cc_library", "cc_test")
load("//tools:cpplint.bzl", "cpplint")

package(default_visibility = ["//visibility:public"])

cc_library(
    name = "timer",
    srcs = ["timer.cc"],
    hdrs = ["timer.h"],
    deps = [
        ":timing_wheel",
        "//modules/common:global_data",
    ],
)

cc_library(
    name = "timer_task",
    hdrs = ["timer_task.h"],
)

cc_library(
    name = "timer_bucket",
    hdrs = ["timer_bucket.h"],
    deps = [
        ":timer_task",
    ],
)

cc_library(
    name = "timing_wheel",
    srcs = ["timing_wheel.cc"],
    hdrs = ["timing_wheel.h"],
    deps = [
        ":timer_bucket",
        "//modules/task",
        "//modules/time",
        "//modules/time:duration",
        "//modules/time:rate",
    ],
)

cc_test(
    name = "timer_test",
    size = "small",
    srcs = ["timer_test.cc"],
    deps = [
        "//modules:cyber_core",
        "//modules:init",
        "@com_google_googletest//:gtest_main",
    ],
)

cpplint()
