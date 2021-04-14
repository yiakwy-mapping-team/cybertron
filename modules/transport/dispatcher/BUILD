load("@rules_cc//cc:defs.bzl", "cc_library", "cc_test")
load("//tools:cpplint.bzl", "cpplint")

package(default_visibility = ["//visibility:public"])

cc_library(
    name = "dispatcher",
    srcs = ["dispatcher.cc"],
    hdrs = ["dispatcher.h"],
    deps = [
        "//modules/common",
        "//modules/message:message_traits",
        "//modules/proto:role_attributes_cc_proto",
        "//modules/transport/message:listener_handler",
        "//modules/transport/message:message_info",
    ],
)

cc_test(
    name = "dispatcher_test",
    size = "small",
    srcs = ["dispatcher_test.cc"],
    deps = [
        "//modules:cyber_core",
        "//modules/proto:unit_test_cc_proto",
        "@com_google_googletest//:gtest_main",
    ],
)

cc_library(
    name = "intra_dispatcher",
    srcs = ["intra_dispatcher.cc"],
    hdrs = ["intra_dispatcher.h"],
    deps = [
        ":dispatcher",
        "//modules/message:message_traits",
        "//modules/proto:role_attributes_cc_proto",
    ],
)

cc_test(
    name = "intra_dispatcher_test",
    size = "small",
    srcs = ["intra_dispatcher_test.cc"],
    deps = [
        "//modules:cyber_core",
        "//modules/proto:unit_test_cc_proto",
        "@com_google_googletest//:gtest_main",
    ],
)

cc_library(
    name = "rtps_dispatcher",
    srcs = ["rtps_dispatcher.cc"],
    hdrs = ["rtps_dispatcher.h"],
    deps = [
        ":dispatcher",
        "//modules/message:message_traits",
        "//modules/proto:role_attributes_cc_proto",
        "//modules/transport/rtps:attributes_filler",
        "//modules/transport/rtps:participant",
        "//modules/transport/rtps:sub_listener",
    ],
)

cc_test(
    name = "rtps_dispatcher_test",
    size = "small",
    srcs = ["rtps_dispatcher_test.cc"],
    deps = [
        "//modules:cyber_core",
        "//modules/proto:unit_test_cc_proto",
        "@com_google_googletest//:gtest",
    ],
)

cc_library(
    name = "shm_dispatcher",
    srcs = ["shm_dispatcher.cc"],
    hdrs = ["shm_dispatcher.h"],
    deps = [
        ":dispatcher",
        "//modules/message:message_traits",
        "//modules/proto:proto_desc_cc_proto",
        "//modules/scheduler:scheduler_factory",
        "//modules/transport/shm:notifier_factory",
        "//modules/transport/shm:readable_info",
        "//modules/transport/shm:segment_factory",
    ],
)

cc_test(
    name = "shm_dispatcher_test",
    size = "small",
    srcs = ["shm_dispatcher_test.cc"],
    deps = [
        "//modules:cyber_core",
        "//modules/proto:unit_test_cc_proto",
        "@com_google_googletest//:gtest_main",
    ],
)

cpplint()
