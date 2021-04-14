load("@rules_python//python:defs.bzl", "py_binary")

package(
    default_visibility = ["//visibility:public"],
)

py_binary(
    name = "cyber_node",
    srcs = ["cyber_node.py"],
    deps = [
        "//modules/python/cyber_py3:cyber",
        "//modules/proto:role_attributes_py_pb2"
    ],
)
