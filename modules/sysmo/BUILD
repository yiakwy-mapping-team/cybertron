load("@rules_cc//cc:defs.bzl", "cc_library", "cc_test")
load("//tools:cpplint.bzl", "cpplint")

package(default_visibility = ["//visibility:public"])

cc_test(
    name = "sysmo_test",
    size = "small",
    srcs = ["sysmo_test.cc"],
    deps = [
        "//modules:cyber_core",
        "//modules/scheduler:scheduler_factory",
        "@com_google_googletest//:gtest_main",
    ],
)

cc_library(
    name = "sysmo",
    srcs = ["sysmo.cc"],
    hdrs = ["sysmo.h"],
    deps = [
        "//modules/scheduler:scheduler_factory",
    ],
)

cpplint()
