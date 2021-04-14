load("@rules_cc//cc:defs.bzl", "cc_library", "cc_test")
load("//tools:cpplint.bzl", "cpplint")

package(default_visibility = ["//visibility:public"])

cc_library(
    name = "base",
    deps = [
        "//modules/base:atomic_hash_map",
        "//modules/base:atomic_rw_lock",
        "//modules/base:bounded_queue",
        "//modules/base:concurrent_object_pool",
        "//modules/base:for_each",
        "//modules/base:macros",
        "//modules/base:object_pool",
        "//modules/base:reentrant_rw_lock",
        "//modules/base:rw_lock_guard",
        "//modules/base:signal",
        "//modules/base:thread_pool",
        "//modules/base:thread_safe_queue",
        "//modules/base:unbounded_queue",
        "//modules/base:wait_strategy",
    ],
)

cc_library(
    name = "atomic_hash_map",
    hdrs = ["atomic_hash_map.h"],
)

cc_test(
    name = "atomic_hash_map_test",
    size = "small",
    srcs = ["atomic_hash_map_test.cc"],
    deps = [
        "//modules/base:atomic_hash_map",
        "@com_google_googletest//:gtest_main",
    ],
)

cc_library(
    name = "atomic_rw_lock",
    hdrs = ["atomic_rw_lock.h"],
    deps = [
        "//modules/base:rw_lock_guard",
    ],
)

cc_test(
    name = "atomic_rw_lock_test",
    size = "small",
    srcs = ["atomic_rw_lock_test.cc"],
    deps = [
        "//modules/base:atomic_rw_lock",
        "//modules/base:reentrant_rw_lock",
        "@com_google_googletest//:gtest_main",
    ],
)

cc_library(
    name = "bounded_queue",
    hdrs = ["bounded_queue.h"],
    deps = [
        "//modules/base:macros",
        "//modules/base:wait_strategy",
    ],
)

cc_test(
    name = "bounded_queue_test",
    size = "small",
    srcs = ["bounded_queue_test.cc"],
    deps = [
        "//modules/base:bounded_queue",
        "@com_google_googletest//:gtest_main",
    ],
)

cc_library(
    name = "concurrent_object_pool",
    hdrs = ["concurrent_object_pool.h"],
    deps = [
        "//modules/base:for_each",
    ],
)

cc_library(
    name = "for_each",
    hdrs = ["for_each.h"],
    deps = [
        "//modules/base:macros",
    ],
)

cc_test(
    name = "for_each_test",
    size = "small",
    srcs = ["for_each_test.cc"],
    deps = [
        "//modules/base:for_each",
        "@com_google_googletest//:gtest_main",
    ],
)

cc_library(
    name = "macros",
    hdrs = ["macros.h"],
)

cc_library(
    name = "object_pool",
    hdrs = ["object_pool.h"],
    deps = [
        "//modules/base:for_each",
        "//modules/base:macros",
    ],
)

cc_test(
    name = "object_pool_test",
    size = "small",
    srcs = ["object_pool_test.cc"],
    linkopts = [
        "-latomic",
    ],
    deps = [
        "//modules/base:concurrent_object_pool",
        "//modules/base:object_pool",
        "@com_google_googletest//:gtest_main",
    ],
)

cc_library(
    name = "reentrant_rw_lock",
    hdrs = ["reentrant_rw_lock.h"],
)

cc_library(
    name = "rw_lock_guard",
    hdrs = ["rw_lock_guard.h"],
)

cc_library(
    name = "signal",
    hdrs = ["signal.h"],
)

cc_test(
    name = "signal_test",
    size = "small",
    srcs = ["signal_test.cc"],
    deps = [
        "//modules/base:signal",
        "@com_google_googletest//:gtest_main",
    ],
)

cc_library(
    name = "thread_pool",
    hdrs = ["thread_pool.h"],
)

cc_library(
    name = "thread_safe_queue",
    hdrs = ["thread_safe_queue.h"],
)

cc_library(
    name = "unbounded_queue",
    hdrs = ["unbounded_queue.h"],
)

cc_test(
    name = "unbounded_queue_test",
    size = "small",
    srcs = ["unbounded_queue_test.cc"],
    deps = [
        "//modules/base:unbounded_queue",
        "@com_google_googletest//:gtest_main",
    ],
)

cc_library(
    name = "wait_strategy",
    hdrs = ["wait_strategy.h"],
)

cpplint()
