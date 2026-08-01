---
type: lesson
course: docker-fundamentals
module: "Module 2: Containerization"
order: 6
title: Container Networking
---

# Container Networking

> 🎥 [Search YouTube for "Container Networking"](https://www.youtube.com/results?search_query=Container%20Networking%20Docker%20Fundamentals%20tutorial)

**Container Networking**
=======================

Container networking is a crucial aspect of containerization, allowing containers to communicate with each other and the outside world. In this lesson, we'll explore the basics of container networking and how to configure it.

### Introduction

Container networking is built on top of the Linux networking stack, which provides a robust and flexible way to manage network connections. When a container is created, a new network namespace is created for it, isolating it from the host system and other containers. This allows containers to have their own IP addresses, routing tables, and network interfaces.

### Networking Modes

There are several networking modes available in Docker, each with its own set of benefits and trade-offs.

*   **bridge**: This is the default networking mode, where containers are connected to a virtual bridge network. Each container has its own IP address on this network, and containers can communicate with each other.
*   **host**: In this mode, containers share the same network stack as the host system. This can be useful for development and testing, but it also means that containers are not isolated from the host.
*   **none**: This mode disables networking for a container, which can be useful for applications that don't need to communicate with the outside world.

### Container Networking with Docker

To configure container networking with Docker, you can use the `docker network` command. Here's an example:

```bash
docker network create my-net
```

This creates a new network with the name `my-net`. You can then use this network when creating a container:

```bash
docker run -it --net my-net my-container
```

### **Mermaid Diagram**

```mermaid
graph LR
    A[Container] -->|networking|> B[Host]
    B -->|networking|> C[Container]
    C -->|networking|> D[Container]
    D -->|networking|> E[Container]
```

This diagram illustrates the flow of network traffic between containers and the host system.

### **Image: Container Networking**

![Container Networking](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Container_networking.svg/800px-Container_networking.svg.png)

This image shows the different components involved in container networking, including the container, the host system, and the network stack.

### Conclusion

Container networking is a powerful tool for managing network connections between containers and the outside world. By understanding the different networking modes and how to configure container networking with Docker, you can create more efficient and scalable containerized applications.
