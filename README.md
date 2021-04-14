# Cybertron

## Introduction

`Cybertron` as an independent toolkit is to setup Multi-Input-Multi-Output (MIMO) pipeline. It was originally maintained by
Baidu CarOS team from legacy Advanced Driving Unit \(ADU\), and since version 3.5, it is continuously integrated to `Apollo.auto` project by community 
maintainers with a new name `cyber_rt`.

Instead of using BCLOUD, they build it with a new compiling system `Bazel`. Bazel is optimized to compile medium and large
size projects. I am also pretty much sure that it works well with existing CMake project in Linux sytem.

The building blocks of software offers three major features to boost up development for realtime computing was optimized 
for RTOS, but it is also possible to be utilized in offline pipelines:

1. \#
2. \##
3. \###

### Software dependencies

Details can be found in `scripts/prepare_for_cyber.sh`. To summarize up, 

```
1. Fast-DDS : 1.5.0
2. protobuf : 3.1.4
3. LLVM CLANG-10 : clang, libc, libtool
6. perf tools : shellcheck, gperftools
7. lint tools : pyflake, flake8, yapf, autopep8
8. visualizer_deps
9. bazel : 3.7.1
```

Note:

> Successful building uses `.bazelrc` to configure, which imports `tools/bazel.rc`

## Build
#### Build from scratch

after setting up the environment, simply run:

> bazel build --config=cpu --jobs=12 '--local_ram_resources=HOST_RAM*0.7' -- //modules/...

![build cyber from scratch](https://drive.google.com/uc?id=15goHJn-MNSdLOmyaNl_zk3aOUlghJ3xE)

To check the building process, switch to verbose :

> bazel build -s --verbose_explanations --explain=see.log --jobs=12 '--local_ram_resources=HOST_RAM*0.7' -- //modules/...

#### verify building

> bazel test -s --verbose_explanations --explain=see.log --jobs=12 '--local_ram_resources=HOST_RAM*0.7' -- //modules/...

Bazel will run and evaluate all gtest cases.

#### Verify third party dependencies

Launch a new docker container with whatever Ubuntu 18.04 based images you have and label it a new name `cyber_dev_base`.

To checkout the building environment, it is handy to check docker image buiding script:

```
[Docker-cyber_dev_base] yiakwy@yiakwy-XPS-15-9500:~/WorkSpace/Github/cyber_rt/docker/build$ bash build_docker.sh --dry -m build -f cyber.x86_64.dockerfile -g cn
Build all packages from source
Docker image built w/ CN based mirrors.
Stable Docker image will be built.
=====.=====.===== Docker Build Preview for cyber =====.=====.=====
|  Generated image: apolloauto/apollo:cyber-x86_64-18.04-20210412_0808
|  FROM image: apolloauto/apollo:cuda11.1-cudnn8-trt7-devel-18.04-x86_64
|  Dockerfile: cyber.x86_64.dockerfile
|  TARGET_ARCH=x86_64, HOST_ARCH=x86_64
|  INSTALL_MODE=build, GEOLOC=cn, APOLLO_DIST=stable
=====.=====.=====.=====.=====.=====.=====.=====.=====.=====.=====.=====.=====
```

It seems that the base image of cyber provides nothing useful except for CUDA comuting environment. Also
we have modern ways to setup docker with CUDA, CUDNN, NCCL, and TensorRT environment. 

Go ahead, and find the dockerfile `cyber-x86_64-18.04-*`, repeat the relevant steps in terminal. We also
provide you a tool `prepare_for_cyber.sh` in our new repository to cover the building steps.


#### Testing build with prebuilt image

Pull prebuilt docker image and start a container binded with current user:

> bash docker/scripts/dev_start.sh

```bash
+ set +x
Adding group `yiakwy' (GID 1000) ...
Done.
Adding user `yiakwy' ...
Adding new user `yiakwy' (1000) with group `yiakwy' ...
Creating home directory `/home/yiakwy' ...
Copying files from `/etc/skel' ...
[ OK ] Congratulations! You have successfully finished setting up Apollo Dev Environment.
[ OK ] To login into the newly created apollo_dev_yiakwy container, please run the following command:
[ OK ]   bash docker/scripts/dev_into.sh
[ OK ] Enjoy!
yiakwy@yiakwy-XPS-15-9500:~/WorkSpace/Github/cyber_rt$
```

The docker image built by Apollo.auto requires an old version of `nvidia-container-cli` toolkit which has problem to detect
cuda (cuda<11.1) and its version correctly. Since we are using CUDA 10.2 Set environment variable `NVIDIA_DISABLE_REQUIRE=1`
to skip over CUDA version check.

After the boostrap, set the environment variables according to [OCI specification](https://github.com/NVIDIA/nvidia-container-runtime).

The container has already setup the environment to build cyber. Simply run

```
[yiakwy@in-dev-docker:/apollo]$ bazel build --config=cpu --jobs=12 '--local_ram_resources=HOST_RAM*0.7' -- //modules/...
(05:52:35) INFO: Invocation ID: 18cee5ab-6424-4424-8da1-78b4c9a324cd
(05:52:35) INFO: Current date is 2021-04-13
(05:52:36) DEBUG: /apollo/third_party/gpus/cuda_configure.bzl:835:10: find_cuda_config_script: /apollo/third_party/gpus/find_cuda_config.py.gz.base64
(05:52:36) INFO: Analyzed 704 targets (2 packages loaded, 2024 targets configured).
(05:52:36) INFO: Found 704 targets...
(05:54:49) INFO: Elapsed time: 133.984s, Critical Path: 38.06s
(05:54:49) INFO: 1878 processes: 880 internal, 998 local.
(05:54:49) INFO: Build completed successfully, 1878 total actions
[yiakwy@in-dev-docker:/apollo]$
```

## Start off

#### Start off with a CMake project
