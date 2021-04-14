load("@rules_cc//cc:defs.bzl", "cc_binary")
load("//tools:cpplint.bzl", "cpplint")
load("//tools/install:install.bzl", "install")

package(default_visibility = ["//visibility:public"])

cc_binary(
    name = "mainboard",
    srcs = [
        "mainboard.cc",
        "module_argument.cc",
        "module_argument.h",
        "module_controller.cc",
        "module_controller.h",
    ],
    linkopts = ["-pthread"],
    linkstatic = False,
    deps = [
        "//modules:cyber_core",
        "//modules/proto:dag_conf_cc_proto",
    ],
)

install(
    name = "install",
    targets = [":mainboard"],
)

cpplint()
