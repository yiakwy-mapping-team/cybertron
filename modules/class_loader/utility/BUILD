load("@rules_cc//cc:defs.bzl", "cc_library")
load("//tools:cpplint.bzl", "cpplint")

package(default_visibility = ["//visibility:public"])

cc_library(
    name = "class_factory",
    srcs = ["class_factory.cc"],
    hdrs = ["class_factory.h"],
)

cc_library(
    name = "class_loader_utility",
    srcs = ["class_loader_utility.cc"],
    hdrs = ["class_loader_utility.h"],
    deps = [
        ":class_factory",
        "//modules/class_loader/shared_library",
        "//modules/common:log",
    ],
)

cpplint()
