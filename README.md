# Cybertron

## Introduction

as an independent toolkit, [`Cybertron`](https://github.com/ApolloAuto/apollo/tree/master/cyber) is used to setup Multi-Input-Multi-Output (MIMO) pipelines. 
It was originally maintained by Baidu CarOS team from legacy Advanced Driving Unit \(ADU\).  
 
Since version 3.5, it has been continuously integrated to [`Apollo.auto`](https://github.com/ApolloAuto/apollo) project by community 
maintainers with a new name `cyber_rt` meaning `Cybertron` for runtime MIMO computing platform.

The application is evolving from original CMake based prototype to tackle some real hard problems for application running in RTOS:

> github.com/ApolloAuto/apollo/issues/3707

To summarize:

- Static allocation of memory
- Intra - Process Communication to replace UDP based communication
- 

Instead of using CMake and internal distributed compiling system BCLOUD -- a distributed compiling system similar to 
`distcc`, Cybertron is built with a new compiling system `Bazel`. Bazel is optimized to 
compile medium and large size of projects. I am also pretty much sure that it works very 
well with existing CMake projects in Linux system.

This repo is a non-official distribution of building blocks of the `Cybertron`. By offering 
three major features, `Cybertron` boosts up real-time computing task performance inside 
RTOS such as QNX and ROS with shumbus. Besides real-time computing system, the `cybertron` 
is also possible to be utilized in offline pipelines:

1. Intra-Process Communiation (IPC) with linux native Xmi shared memory
2. Dynamic loading with Directed Acyclic Graph (DAG) description for multi input and multi output (MIMO) application
3. M:N threads to schedule tasks in user space
4. Sync with `Apollo.auto` main line released-6.0 

### Software dependencies

Details of dependencies can be easily found in `scripts/prepare_for_cyber.sh`: 

```
1. Fast-DDS : 1.5.0
2. protobuf : 3.14
3. LLVM CLANG-10 : clang, libc, libtool
6. perf tools : shellcheck, gperftools
7. lint tools : pyflake, flake8, yapf, autopep8
8. visualizer_deps
9. bazel : 3.7.1
```

Note:

> Successful building uses `.bazelrc` from `Apollo.auto` to configure. The file is used to 
> import `tools/bazel.rc`. If you are building `Cybertron` in customer container or build it
> in host environment, bazel and proto will be installed in /usr/bin, make sure you have
> configured a correct envrionment for bazel to find them

## Build

#### 1. Build from scratch in local environment

First we need to setup development environment:

```
sudo bash scripts/prepare_for_cyber.sh
```

After the environment setup, simply run the following command to build libraries with Bazel:

```
/usr/bin/bazel build --config=cpu --jobs=12 '--local_ram_resources=HOST_RAM*0.7' -- //modules/...
```

Here is the snapshot of building result:

![build cyber from scratch](https://drive.google.com/uc?id=15goHJn-MNSdLOmyaNl_zk3aOUlghJ3xE)

To check the building process, switch to verbose:

```
/usr/bin/bazel build -s --verbose_explanations --explain=see.log --jobs=12 '--local_ram_resources=HOST_RAM*0.7' -- //modules/...
```

#### 2. Verify

Before running the test, if you are not in a container, cp the binaries into "/apollo" for test:

```
sudo ln -s modules /apollo/cyber
sudo cp -r bazel-bin /apollo
```

followed by issuing

```
/usr/bin/bazel test -s --verbose_explanations --explain=see.log --jobs=12 '--local_ram_resources=HOST_RAM*0.7' -- //modules/...
```

Bazel will run and evaluate all gtest cases automatically:

![test_cyber_building](https://drive.google.com/uc?id=1r4wf-RCC1fGzWPAkbmiNOP7tHlyZ2I9w)

#### 3. Build `cyber` image

We want to launch a new docker image with whatever images based on Ubuntu 18.04, and label it a with new 
name `cyber_dev_base`.

To checkout the building environment, it is handy to check docker image building script:

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

The base image of cyber provides nothing useful except for CUDA computing environment. Also
we have modern ways to setup docker with CUDA, CUDNN, NCCL, and TensorRT environment. 

You also opted to login in a new docker container from base image. We provide you the building 
tool `scritps/prepare_for_cyber.sh` in this repository to cover the building steps. Then you
can commit changes to generate cyber image.

The container has already setup the environment to build cyber. Simply run

```
/usr/bin/bazel build --config=cpu --jobs=12 '--local_ram_resources=HOST_RAM*0.7' -- //modules/...
```

#### 4. Pull prebuilt `cyber` image

Similar `Apollo.auto` main line, to pull pre-built cyber image, use `docker/scripts/cyber_start.sh` 

```
(py36) ➜  cybertron git:(master) ✗ bash docker/scripts/cyber_start.sh                              
Done checking host environment.
[INFO] Image apolloauto/apollo:cyber-x86_64-18.04-20200914_0704 found locally, will be used.
[INFO] Removing existing cyber container apollo_cyber_yiak
[INFO] DOCKER_RUN_CMD evaluated to: docker run --gpus all
[INFO] Starting docker container "apollo_cyber_yiak" ...
+ docker run --gpus all -it -d --privileged --name apollo_cyber_yiak -e DISPLAY=:1 -e DOCKER_USER=yiak -e USER=yiak -e DOCKER_USER_ID=1000 -e DOCKER_GRP=yiak -e DOCKER_GRP_ID=1000 -e DOCKER_IMG=apolloauto/apollo:cyber-x86_64-18.04-20200914_0704 -e USE_GPU_HOST=1 -e NVIDIA_VISIBLE_DEVICES=all -e NVIDIA_DRIVER_CAPABILITIES=compute,video,graphics,utility -e OMP_NUM_THREADS=1 -v /home/yiak/WorkSpace/Github/cybertron:/apollo -v /dev:/dev -v /etc/localtime:/etc/localtime:ro -v /dev/null:/dev/raw1394 -v /media:/media -v /tmp/.X11-unix:/tmp/.X11-unix:rw -v /lib/modules:/lib/modules --net host -w /apollo --add-host in-cyber-docker:172.0.0.1 --add-host yiak-Z390-UD:127.0.0.1 --hostname in-cyber-docker --shm-size 2G --pid=host apolloauto/apollo:cyber-x86_64-18.04-20200914_0704 /bin/bash
3cf9546e4c264e772426e3c0dbc318f2c8bb5637690d2e35f48f8e8d5e84563c
+ '[' 0 -ne 0 ']'
+ set +x
Adding group `yiak' (GID 1000) ...
Done.
Adding user `yiak' ...
Adding new user `yiak' (1000) with group `yiak' ...
Creating home directory `/home/yiak' ...
Copying files from `/etc/skel' ...
[ OK ] Congrats, you have successfully finished setting up Apollo cyber docker environment. To login into cyber container, please run the following command:
[ OK ]   bash docker/scripts/cyber_into.sh
[ OK ] Enjoy!

```

The docker image built by `Apollo.auto` requires an old version of `nvidia-container-cli` 
toolkit which has problem to detect cuda (cuda<11.1) and its version correctly. Since we 
are using CUDA 10.2, Set environment variable `NVIDIA_DISABLE_REQUIRE=1` to skip over CUDA 
version check.

After the bootstrap, set the additional container environment variables as with 
[OCI specification](https://github.com/NVIDIA/nvidia-container-runtime) to meet your needs.

Actually, the container has already setup the environment variables to build cyber. Simply 
run:

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

## FQA

1. Will cybertron work with Anaconda python

    Definitely yes. The "third_party/py" was used to handle python, to help bazel find your 
    python correclty, setup your environment variables and change accordingly:

    > source cyber_env.sh 

    ```
    (py36) ➜  cybertron git:(master) ✗ /usr/bin/bazel build --config=cpu --jobs=12 '--local_ram_resources=HOST_RAM*0.7' -- //modules/...
    (23:16:36) INFO: Current date is 2021-08-27
    (23:16:37) DEBUG: /home/yiak/WorkSpace/Github/cybertron/third_party/py/python_configure.bzl:196:10: ctx: <unknown object com.google.devtools.build.lib.bazel.repository.starlark.StarlarkRepositoryContext>
    (23:16:37) DEBUG: /home/yiak/WorkSpace/Github/cybertron/third_party/py/python_configure.bzl:197:10: bin: /bin/bash
    (23:16:37) DEBUG: /home/yiak/WorkSpace/Github/cybertron/third_party/py/python_configure.bzl:198:10: cmd: test -d "/home/yiak/anaconda3/envs/py36/lib/libpython3.6m.so.1.0" -a -x "/home/yiak/anaconda3/envs/py36/lib/libpython3.6m.so.1.0"
    (23:16:37) INFO: Analyzed 688 targets (95 packages loaded, 2321 targets configured).
    (23:16:37) INFO: Found 688 targets...
    (23:18:16) INFO: Elapsed time: 99.700s, Critical Path: 25.01s
    (23:18:16) INFO: 2592 processes: 1606 internal, 986 local.
    (23:18:16) INFO: Build completed successfully, 2592 total actions
    
    ```


2. Could I debug cybertron with GDB ?

    Definitely yes. Pass debug flags to gcc with built_opt:
    
    ```
    /usr/bin/bazel build --compilation_mode=dbg //modules/...
    ```

## Start off

#### Start off with a CMake project

