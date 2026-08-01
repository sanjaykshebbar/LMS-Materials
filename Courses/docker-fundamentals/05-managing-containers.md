---
type: lesson
course: docker-fundamentals
module: "Module 2: Containerization"
order: 5
title: Managing Containers
---

# Managing Containers

> 🎥 [Search YouTube for "Managing Containers"](https://www.youtube.com/results?search_query=Managing%20Containers%20Docker%20Fundamentals%20tutorial)

# Managing Containers
======================

Managing containers is a crucial aspect of Docker, as it allows you to control and monitor the containers running on your system. In this lesson, we will cover the basics of managing containers, including how to list, start, stop, and remove containers.

## Container States

A container can be in one of the following states:

* **Created**: The container has been created but not started.
* **Running**: The container is currently running.
* **Paused**: The container is running but its processes are suspended.
* **Stopped**: The container is not running, but it still exists.
* **Exited**: The container has finished executing and has exited.

## Listing Containers

To list all containers on your system, you can use the `docker ps` command:
```bash
docker ps
```
This will display a list of all containers, including their IDs, names, and statuses.

## Starting and Stopping Containers

To start a container, you can use the `docker start` command:
```bash
docker start <container_id>
```
To stop a container, you can use the `docker stop` command:
```bash
docker stop <container_id>
```
## Removing Containers

To remove a container, you can use the `docker rm` command:
```bash
docker rm <container_id>
```
You can also remove all stopped containers at once using the `docker system prune` command:
```bash
docker system prune
```
## Monitoring Container Resources

To monitor the resources used by a container, you can use the `docker stats` command:
```bash
docker stats <container_id>
```
This will display a list of the container's resource usage, including CPU, memory, and network I/O.

### Container Resource Usage

```mermaid
graph LR
    A[Container] -->|CPU|> B[Host CPU]
    A -->|Memory|> C[Host Memory]
    A -->|Network|> D[Host Network]
```

### Container Resource Limits

To set resource limits for a container, you can use the `docker run` command with the `---cpu-shares` and `--memory` options:
```bash
docker run -it --cpu-shares 1024 --memory 512m <image_name>
```
This will set the CPU shares and memory limits for the container.

### Container Logs

To view the logs of a container, you can use the `docker logs` command:
```bash
docker logs <container_id>
```
This will display a list of the container's log messages.

### Container Network

To view the network connections of a container, you can use the `docker inspect` command:
```bash
docker inspect <container_id>
```
This will display a list of the container's network connections.

![Docker Container Network](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Docker_network.svg/800px-Docker_network.svg)

### Container File System

To view the file system of a container, you can use the `docker inspect` command:
```bash
docker inspect <container_id>
```
This will display a list of the container's file system.

![Docker Container File System](https://placehold.co/800x400?text=Container+File+System)

### Container Environment Variables

To view the environment variables of a container, you can use the `docker inspect` command:
```bash
docker inspect <container_id>
```
This will display a list of the container's environment variables.

![Docker Container Environment Variables](https://placehold.co/800x400?text=Container+Environment+Variables)

### Container Network Ports

To view the network ports of a container, you can use the `docker inspect` command:
```bash
docker inspect <container_id>
```
This will display a list of the container's network ports.

![Docker Container Network Ports](https://placehold.co/800x400?text=Container+Network+Ports)

### Container Process Tree

To view the process tree of a container, you can use the `docker top` command:
```bash
docker top <container_id>
```
This will display a list of the container's processes.

![Docker Container Process Tree](https://placehold.co/800x400?text=Container+Process+Tree)

### Container Resource Usage Graph

```mermaid
graph LR
    A[Container] -->|CPU|> B[Host CPU]
    A -->|Memory|> C[Host Memory]
    A -->|Network|> D[Host Network]
    B -->|CPU Usage|> E[Container CPU Usage]
    C -->|Memory Usage|> F[Container Memory Usage]
    D -->|Network Usage|> G[Container Network Usage]
```

By following this lesson, you should now have a good understanding of how to manage and troubleshoot Docker containers.
