load("@rules_cc//cc:defs.bzl", "cc_library")
load("//tools:cpplint.bzl", "cpplint")

package(default_visibility = ["//visibility:public"])

cc_library(
    name = "perf_event_cache",
    srcs = ["perf_event_cache.cc"],
    hdrs = ["perf_event_cache.h"],
    deps = [
        ":perf_event",
        "//modules:state",
        "//modules/base:bounded_queue",
        "//modules/common:global_data",
        "//modules/common:log",
        "//modules/common:macros",
        "//modules/time",
    ],
)

cc_library(
    name = "perf_event",
    hdrs = ["perf_event.h"],
    deps = [
        "//modules/common:global_data",
    ],
)

cpplint()
