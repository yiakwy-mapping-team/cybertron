load("@rules_cc//cc:defs.bzl", "cc_library", "cc_test")
load("//tools:cpplint.bzl", "cpplint")

package(default_visibility = ["//visibility:public"])

cc_library(
    name = "node",
    srcs = ["node.cc"],
    hdrs = ["node.h"],
    deps = [
        ":node_channel_impl",
        ":node_service_impl",
    ],
)

cc_library(
    name = "node_channel_impl",
    hdrs = ["node_channel_impl.h"],
    deps = [
        ":reader",
        ":writer",
        "//modules/blocker:intra_reader",
        "//modules/blocker:intra_writer",
        "//modules/common:global_data",
        "//modules/message:message_traits",
        "//modules/proto:run_mode_conf_cc_proto",
    ],
)

cc_test(
    name = "node_channel_impl_test",
    size = "small",
    srcs = ["node_channel_impl_test.cc"],
    deps = [
        "//modules:cyber",
        "//modules/proto:unit_test_cc_proto",
        "@com_google_googletest//:gtest_main",
    ],
)

cc_library(
    name = "node_service_impl",
    hdrs = ["node_service_impl.h"],
    deps = [
        ":reader",
        ":writer",
        "//modules/common:global_data",
        "//modules/service",
        "//modules/service:client",
        "//modules/service_discovery:topology_manager",
    ],
)

cc_test(
    name = "node_test",
    size = "small",
    srcs = ["node_test.cc"],
    deps = [
        "//modules:cyber",
        "//modules/proto:unit_test_cc_proto",
        "@com_google_googletest//:gtest_main",
    ],
)

cc_library(
    name = "reader",
    hdrs = ["reader.h"],
    deps = [
        ":reader_base",
        "//modules/blocker",
        "//modules/common:global_data",
        "//modules/croutine:routine_factory",
        "//modules/data:data_visitor",
        "//modules/proto:topology_change_cc_proto",
        "//modules/scheduler",
        "//modules/service_discovery:topology_manager",
        "//modules/time",
        "//modules/transport",
    ],
)

cc_library(
    name = "reader_base",
    hdrs = ["reader_base.h"],
    deps = [
        "//modules/event:perf_event_cache",
        "//modules/transport",
    ],
)

cc_test(
    name = "reader_test",
    size = "small",
    srcs = ["reader_test.cc"],
    deps = [
        "//modules:cyber",
        "//modules/proto:unit_test_cc_proto",
        "@com_google_googletest//:gtest",
    ],
)

cc_library(
    name = "writer",
    hdrs = ["writer.h"],
    deps = [
        ":writer_base",
        "//modules/common:log",
        "//modules/proto:topology_change_cc_proto",
        "//modules/service_discovery:topology_manager",
        "//modules/transport",
    ],
)

cc_library(
    name = "writer_base",
    hdrs = ["writer_base.h"],
    deps = [
        "//modules/common:macros",
        "//modules/common:util",
        "//modules/proto:role_attributes_cc_proto",
    ],
)

cc_test(
    name = "writer_reader_test",
    size = "small",
    srcs = ["writer_reader_test.cc"],
    deps = [
        "//modules:cyber",
        "//modules/proto:unit_test_cc_proto",
        "@com_google_googletest//:gtest",
    ],
)

cc_test(
    name = "writer_test",
    size = "small",
    srcs = ["writer_test.cc"],
    deps = [
        "//modules:cyber",
        "//modules/node:writer_base",
        "//modules/proto:unit_test_cc_proto",
        "@com_google_googletest//:gtest",
    ],
)

cpplint()
