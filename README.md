# pytorch-poc
pytorch nvidia framework for docker

## Need nvidia gpu drivers and cuda toolkit
### Find more info 
https://towardsdatascience.com/setting-up-your-pc-workstation-for-deep-learning-tensorflow-and-pytorch-windows-9099b96035cb

## Pytorch nvidia framework for docker
https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch

PyTorch es un marco computacional tensorial acelerado por GPU.
La funcionalidad se puede ampliar con bibliotecas comunes de Python como NumPy y SciPy. 
La diferenciación automática se realiza con un sistema basado en cinta en los niveles de capa de red funcional y neuronal.

## Realases documentation (for version compativility and more)
https://docs.nvidia.com/deeplearning/frameworks/pytorch-release-notes

## Matrix version compatibility
https://docs.nvidia.com/deeplearning/frameworks/support-matrix/index.html#framework-matrix-2021

## Getting started
https://docs.nvidia.com/deeplearning/frameworks/index.html

## Setup git
git config credential.helper store
git config user.name "Alvaro Hernandez"
git config user.email "alvherrey@gmail.com"
git config --list

git config --list --global

## Docker
### docker build image
docker build -t pytorch-poc .

### docker create container and run in foreground (sin gpu)
docker run --name pytorch-poc pytorch-poc
### docker create container and run in background (sin gpu)
docker run --name pytorch-poc -d pytorch-poc
### docker delete container
docker rm -f pytorch-poc

### docker create container and run nvidia-smi after delete container (con gpu)
docker run --rm --gpus all --ipc=host --name pytorch-poc pytorch-poc:latest nvidia-smi

### docker create container and run in foreground (con gpu)
docker run --gpus all --ipc=host --name pytorch-poc pytorch-poc:latest


## Docker tensorflow test
### docker build image
docker build -t pytorch-tf-poc .

### docker create container and run in foreground (sin gpu)
docker run --name pytorch-tf-poc pytorch-tf-poc
### docker create container and run in background (sin gpu)
docker run --name pytorch-tf-poc -d pytorch-tf-poc
### docker delete container
docker rm -f pytorch-tf-poc

### docker create container and run nvidia-smi after delete container (con gpu)
docker run --rm --gpus all --ipc=host --name pytorch-tf-poc pytorch-tf-poc:latest nvidia-smi

### docker create container and run in foreground (con gpu)
docker run --gpus all --ipc=host --name pytorch-tf-poc pytorch-tf-poc:latest