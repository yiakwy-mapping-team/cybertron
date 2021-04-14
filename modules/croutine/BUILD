load("@rules_cc//cc:defs.bzl", "cc_library", "cc_test")
load("//tools:cpplint.bzl", "cpplint")

package(default_visibility = ["//visibility:public"])

cc_library(
    name = "croutine",
    srcs = ["croutine.cc"],
    hdrs = ["croutine.h"],
    linkopts = ["-latomic"],
    deps = [
        "//modules/base:atomic_hash_map",
        "//modules/base:atomic_rw_lock",
        "//modules/base:bounded_queue",
        "//modules/base:concurrent_object_pool",
        "//modules/base:macros",
        "//modules/base:wait_strategy",
        "//modules/common",
        "//modules/croutine:routine_context",
        "//modules/croutine:routine_factory",
        "//modules/croutine:swap",
        "//modules/event:perf_event_cache",
        "//modules/time",
    ],
)

cc_library(
    name = "routine_context",
    srcs = ["detail/routine_context.cc"],
    hdrs = ["detail/routine_context.h"],
    deps = [
        "//modules/common",
    ],
)

cc_library(
    name = "routine_factory",
    hdrs = ["routine_factory.h"],
    deps = [
        "//modules/common",
        "//modules/event:perf_event_cache",
    ],
)

cc_library(
    name = "swap",
    srcs = select(
        {
            "@platforms//cpu:x86_64": [
                "detail/swap_x86_64.S",
            ],
            "@platforms//cpu:aarch64": [
                "detail/swap_aarch64.S",
            ],
        },
        no_match_error = "Please Build with a Linux aarch64 or x86_64 platform",
    ),
)

cc_test(
    name = "croutine_test",
    size = "small",
    srcs = ["croutine_test.cc"],
    deps = [
        "//modules:cyber",
        "@com_google_googletest//:gtest_main",
    ],
)

cpplint()
