load("@rules_python//python:defs.bzl", "py_binary")

package(
    default_visibility = ["//visibility:public"],
)

py_binary(
    name = "cyber_channel",
    srcs = ["cyber_channel.py"],
    deps = [
        "//modules/proto:role_attributes_py_pb2",
        "//modules/python/cyber_py3:cyber",
        "//modules/python/cyber_py3:cyber_time",
    ],
)
