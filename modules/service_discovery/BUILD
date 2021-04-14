load("@rules_cc//cc:defs.bzl", "cc_library", "cc_test")
load("//tools:cpplint.bzl", "cpplint")

package(default_visibility = ["//visibility:public"])

cc_library(
    name = "topology_manager",
    srcs = ["topology_manager.cc"],
    hdrs = ["topology_manager.h"],
    deps = [
        ":channel_manager",
        ":node_manager",
        ":service_manager",
        "//modules/service_discovery/communication:participant_listener",
        "//modules/transport/rtps:participant",
    ],
)

cc_test(
    name = "topology_manager_test",
    size = "small",
    srcs = ["topology_manager_test.cc"],
    deps = [
        "//modules:cyber",
        "@com_google_googletest//:gtest_main",
    ],
)

cc_library(
    name = "graph",
    srcs = ["container/graph.cc"],
    hdrs = ["container/graph.h"],
    deps = ["//modules/base:atomic_rw_lock"],
)

cc_test(
    name = "graph_test",
    size = "small",
    srcs = ["container/graph_test.cc"],
    deps = [
        "//modules:cyber",
        "@com_google_googletest//:gtest_main",
    ],
)

cc_library(
    name = "multi_value_warehouse",
    srcs = ["container/multi_value_warehouse.cc"],
    hdrs = ["container/multi_value_warehouse.h"],
    deps = [
        ":warehouse_base",
        "//modules/base:atomic_rw_lock",
    ],
)

cc_test(
    name = "multi_value_warehouse_test",
    size = "small",
    srcs = ["container/multi_value_warehouse_test.cc"],
    deps = [
        ":multi_value_warehouse",
        "@com_google_googletest//:gtest_main",
    ],
)

cc_library(
    name = "single_value_warehouse",
    srcs = ["container/single_value_warehouse.cc"],
    hdrs = ["container/single_value_warehouse.h"],
    deps = [
        ":warehouse_base",
        "//modules/base:atomic_rw_lock",
    ],
)

cc_test(
    name = "single_value_warehouse_test",
    size = "small",
    srcs = ["container/single_value_warehouse_test.cc"],
    deps = [
        ":single_value_warehouse",
        "@com_google_googletest//:gtest_main",
    ],
)

cc_library(
    name = "warehouse_base",
    hdrs = ["container/warehouse_base.h"],
    deps = ["role"],
)

cc_library(
    name = "role",
    srcs = ["role/role.cc"],
    hdrs = ["role/role.h"],
    deps = [
        "//modules:binary",
        "//modules/common:log",
        "//modules/common:types",
        "//modules/proto:role_attributes_cc_proto",
    ],
)

cc_test(
    name = "role_test",
    size = "small",
    srcs = ["role/role_test.cc"],
    deps = [
        "//modules:cyber",
        "@com_google_googletest//:gtest_main",
    ],
)

cc_library(
    name = "manager",
    srcs = ["specific_manager/manager.cc"],
    hdrs = ["specific_manager/manager.h"],
    deps = [
        "//modules:state",
        "//modules/base:signal",
        "//modules/message:message_traits",
        "//modules/message:protobuf_factory",
        "//modules/proto:proto_desc_cc_proto",
        "//modules/proto:role_attributes_cc_proto",
        "//modules/proto:topology_change_cc_proto",
        "//modules/service_discovery/communication:subscriber_listener",
        "//modules/time",
        "//modules/transport/qos",
        "//modules/transport/rtps:attributes_filler",
        "//modules/transport/rtps:underlay_message_type",
        "@fastrtps",
    ],
)

cc_library(
    name = "channel_manager",
    srcs = ["specific_manager/channel_manager.cc"],
    hdrs = ["specific_manager/channel_manager.h"],
    deps = [
        ":graph",
        ":manager",
        ":multi_value_warehouse",
        ":single_value_warehouse",
    ],
)

cc_test(
    name = "channel_manager_test",
    size = "small",
    srcs = ["specific_manager/channel_manager_test.cc"],
    deps = [
        "//modules:cyber",
        "//modules/proto:unit_test_cc_proto",
        "@com_google_googletest//:gtest_main",
    ],
)

cc_library(
    name = "node_manager",
    srcs = ["specific_manager/node_manager.cc"],
    hdrs = ["specific_manager/node_manager.h"],
    deps = [
        ":manager",
        ":multi_value_warehouse",
        ":single_value_warehouse",
    ],
)

cc_test(
    name = "node_manager_test",
    size = "small",
    srcs = ["specific_manager/node_manager_test.cc"],
    deps = [
        "//modules:cyber",
        "@com_google_googletest//:gtest_main",
    ],
)

cc_library(
    name = "service_manager",
    srcs = ["specific_manager/service_manager.cc"],
    hdrs = ["specific_manager/service_manager.h"],
    deps = [
        ":manager",
        ":multi_value_warehouse",
        ":single_value_warehouse",
    ],
)

cc_test(
    name = "service_manager_test",
    size = "small",
    srcs = ["specific_manager/service_manager_test.cc"],
    deps = [
        "//modules:cyber",
        "@com_google_googletest//:gtest_main",
    ],
)

cpplint()
