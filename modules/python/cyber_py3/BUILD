load("@rules_python//python:defs.bzl", "py_library")

package(default_visibility = ["//visibility:public"])

py_library(
    name = "cyber_time",
    srcs = ["cyber_time.py"],
    data = [
        "//modules/python/internal:_cyber_time_wrapper.so",
        "//modules/python/internal:_cyber_wrapper.so",
    ],
)

py_library(
    name = "cyber_timer",
    srcs = ["cyber_timer.py"],
    data = [
        "//modules/python/internal:_cyber_timer_wrapper.so",
    ],
)

py_library(
    name = "cyber",
    srcs = ["cyber.py"],
    data = [
        "//modules/python/internal:_cyber_wrapper.so",
    ],
)

py_library(
    name = "parameter",
    srcs = ["parameter.py"],
    data = [
        "//modules/python/internal:_cyber_parameter_wrapper.so",
    ],
)

py_library(
    name = "record",
    srcs = ["record.py"],
    data = [
        "//modules/python/internal:_cyber_record_wrapper.so",
    ],
)
