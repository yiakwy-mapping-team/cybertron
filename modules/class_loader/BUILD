load("@rules_cc//cc:defs.bzl", "cc_library", "cc_test")
load("//tools:cpplint.bzl", "cpplint")

package(default_visibility = ["//visibility:public"])

cc_library(
    name = "class_loader",
    srcs = ["class_loader.cc"],
    hdrs = ["class_loader.h"],
    deps = [
        ":class_loader_register_macro",
        "//modules:init",
        "//modules/class_loader/shared_library",
        "//modules/class_loader/utility:class_factory",
        "//modules/class_loader/utility:class_loader_utility",
        "//modules/common:log",
    ],
)

cc_library(
    name = "class_loader_register_macro",
    hdrs = ["class_loader_register_macro.h"],
    deps = [
        "//modules/class_loader/utility:class_loader_utility",
    ],
)

cc_library(
    name = "class_loader_manager",
    srcs = ["class_loader_manager.cc"],
    hdrs = ["class_loader_manager.h"],
    deps = [
        ":class_loader",
    ],
)

cc_test(
    name = "class_loader_test",
    size = "small",
    srcs = ["class_loader_test.cc"],
    data = [
        "//modules/class_loader/test:plugin1",
        "//modules/class_loader/test:plugin2",
    ],
    deps = [
        "//modules:cyber",
        "//modules/class_loader/test:base",
        "//modules/proto:unit_test_cc_proto",
        "@com_google_googletest//:gtest",
    ],
)

cpplint()
