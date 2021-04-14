load("@rules_cc//cc:defs.bzl", "cc_binary", "cc_library")
load("//tools/install:install.bzl", "install")
load("//tools:cpplint.bzl", "cpplint")

package(default_visibility = ["//visibility:public"])

install(
    name = "install",
    targets = [
      ":cyber_recorder",
    ],
)

cc_binary(
    name = "cyber_recorder",
    srcs = ["main.cc"],
    linkopts = ["-pthread"],
    deps = [
        ":info",
        ":recorder",
        ":recoverer",
        ":spliter",
        "//modules:init",
        "//modules/common:file",
        "//modules/common:time_conversion",
        "//modules/tools/cyber_recorder/player",
    ],
)

cc_library(
    name = "info",
    srcs = ["info.cc"],
    hdrs = ["info.h"],
    deps = [
        "//modules/common:time_conversion",
        "//modules/proto:record_cc_proto",
        "//modules/record:record_file_reader",
        "//modules/record:record_message",
    ],
)

cc_library(
    name = "recorder",
    srcs = ["recorder.cc"],
    hdrs = ["recorder.h"],
    deps = [
        "//modules:cyber",
        "//modules/common:log",
        "//modules/proto:record_cc_proto",
        "@fastrtps",
    ],
)

cc_library(
    name = "recoverer",
    srcs = ["recoverer.cc"],
    hdrs = ["recoverer.h"],
    deps = [
        "//modules/base:for_each",
        "//modules/common:log",
        "//modules/proto:record_cc_proto",
        "//modules/record:header_builder",
        "//modules/record:record_file_reader",
        "//modules/record:record_writer",
    ],
)

cc_library(
    name = "spliter",
    srcs = ["spliter.cc"],
    hdrs = ["spliter.h"],
    deps = [
        "//modules/common:log",
        "//modules/proto:record_cc_proto",
        "//modules/record:header_builder",
        "//modules/record:record_file_reader",
        "//modules/record:record_writer",
    ],
)

cpplint()
