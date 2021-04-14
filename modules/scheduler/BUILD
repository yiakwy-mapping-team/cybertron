load("@rules_cc//cc:defs.bzl", "cc_library", "cc_test")
load("//tools:cpplint.bzl", "cpplint")

package(default_visibility = ["//visibility:public"])

cc_library(
    name = "processor",
    srcs = ["processor.cc"],
    hdrs = ["processor.h"],
    deps = [
        "//modules/data",
        "//modules/scheduler:processor_context",
    ],
)

cc_library(
    name = "processor_context",
    srcs = ["processor_context.cc"],
    hdrs = ["processor_context.h"],
    deps = [
        "//modules/croutine",
        "//modules/data",
    ],
)

cc_library(
    name = "scheduler",
    srcs = ["scheduler.cc"],
    hdrs = ["scheduler.h"],
    deps = [
        "//modules/croutine",
        "//modules/scheduler:mutex_wrapper",
        "//modules/scheduler:pin_thread",
        "//modules/scheduler:processor",
    ],
)

cc_library(
    name = "mutex_wrapper",
    hdrs = ["common/mutex_wrapper.h"],
)

cc_library(
    name = "cv_wrapper",
    hdrs = ["common/cv_wrapper.h"],
)

cc_library(
    name = "pin_thread",
    srcs = ["common/pin_thread.cc"],
    hdrs = ["common/pin_thread.h"],
    deps = [
        "//modules/common:log",
    ],
)

cc_library(
    name = "scheduler_factory",
    srcs = ["scheduler_factory.cc"],
    hdrs = ["scheduler_factory.h"],
    deps = [
        "//modules/proto:component_conf_cc_proto",
        "//modules/scheduler:scheduler_choreography",
        "//modules/scheduler:scheduler_classic",
    ],
)

cc_library(
    name = "scheduler_choreography",
    srcs = ["policy/scheduler_choreography.cc"],
    hdrs = ["policy/scheduler_choreography.h"],
    deps = [
        "//modules/scheduler",
        "//modules/scheduler:choreography_context",
        "//modules/scheduler:classic_context",
    ],
)

cc_library(
    name = "scheduler_classic",
    srcs = ["policy/scheduler_classic.cc"],
    hdrs = ["policy/scheduler_classic.h"],
    deps = [
        "//modules/scheduler",
        "//modules/scheduler:classic_context",
    ],
)

cc_library(
    name = "choreography_context",
    srcs = ["policy/choreography_context.cc"],
    hdrs = ["policy/choreography_context.h"],
    deps = [
        "//modules/croutine",
        "//modules/proto:choreography_conf_cc_proto",
        "//modules/scheduler:processor",
    ],
)

cc_library(
    name = "classic_context",
    srcs = ["policy/classic_context.cc"],
    hdrs = ["policy/classic_context.h"],
    deps = [
        "//modules/croutine",
        "//modules/proto:classic_conf_cc_proto",
        "//modules/scheduler:cv_wrapper",
        "//modules/scheduler:mutex_wrapper",
        "//modules/scheduler:processor",
    ],
)

cc_test(
    name = "scheduler_test",
    size = "small",
    srcs = ["scheduler_test.cc"],
    deps = [
        "//modules:cyber",
        "//modules/scheduler:scheduler_factory",
        "@com_google_googletest//:gtest_main",
    ],
)

cc_test(
    name = "scheduler_classic_test",
    size = "small",
    srcs = ["scheduler_classic_test.cc"],
    deps = [
        "//modules:cyber",
        "//modules/scheduler:scheduler_factory",
        "@com_google_googletest//:gtest_main",
    ],
)

cc_test(
    name = "scheduler_choreo_test",
    size = "small",
    srcs = ["scheduler_choreo_test.cc"],
    deps = [
        "//modules:cyber",
        "//modules/scheduler:scheduler_factory",
        "@com_google_googletest//:gtest_main",
    ],
)

cc_test(
    name = "processor_test",
    size = "small",
    srcs = ["processor_test.cc"],
    deps = [
        "//modules:cyber",
        "//modules/scheduler:processor",
        "@com_google_googletest//:gtest_main",
    ],
)

cc_test(
    name = "pin_thread_test",
    size = "small",
    srcs = ["common/pin_thread_test.cc"],
    deps = [
        "//modules:cyber",
        "//modules/scheduler:pin_thread",
        "@com_google_googletest//:gtest_main",
    ],
)

cpplint()
