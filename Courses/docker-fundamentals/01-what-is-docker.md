---
type: lesson
course: docker-fundamentals
module: "Module 1: Introduction to Docker"
order: 1
title: What is Docker?
---

# What is Docker?

> 🎥 [Search YouTube for "What is Docker?"](https://www.youtube.com/results?search_query=What%20is%20Docker%3F%20Docker%20Fundamentals%20tutorial)

## What is Docker?

Docker is a containerization platform that allows developers to package, ship, and run applications in containers. Containers are lightweight and portable, making it easy to deploy applications consistently across different environments.

### Containerization: A New Era in Application Deployment

Traditionally, applications were deployed on virtual machines (VMs), which were heavy, resource-intensive, and difficult to manage. With the rise of containerization, applications can now be deployed in a more efficient and flexible way.

### How Containerization Works

Here's a high-level overview of the containerization process:

### **Containerization vs. Virtualization**

|  | Virtualization | Containerization |
| --- | --- | --- |
| **Environment** | VMs, separate OS instances | Shared host OS, containerized apps |
| **Resource Utilization** | Overhead of separate OS instances | Lightweight, shared host OS |
| **Portability** | Difficult to move between environments | Easy to move between environments |
| **Scalability** | Challenging to scale | Easy to scale |

### **The Docker Ecosystem**

Docker is not just a container runtime; it's a full-fledged platform that includes:

*   **Docker Engine**: The core container runtime.
*   **Docker Hub**: A registry for container images.
*   **Docker Compose**: A tool for defining and running multi-container applications.

### **Docker Architecture**

```mermaid
graph LR
    A[Host OS] -->|shared|> B[Container Runtime]
    B -->|containerized|> C[Application]
    C -->|network|> D[Container Network]
    D -->|shared|> E[Container]
```

### **Why Docker?**

Docker provides a number of benefits, including:

*   **Lightweight**: Containers are much lighter than VMs, making them ideal for development and testing.
*   **Portable**: Containers are easy to move between environments, making it simple to deploy applications consistently.
*   **Scalable**: Containers can be easily scaled up or down, making it simple to handle changes in application demand.

![Containerization](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Containerization.svg/800px-Containerization.svg)

### **Getting Started with Docker**

To get started with Docker, you'll need to:

1.  **Install Docker**: Download and install the Docker Engine from the official Docker website.
2.  **Pull a Docker Image**: Use the `docker pull` command to download a Docker image from Docker Hub.
3.  **Run a Docker Container**: Use the `docker run` command to start a new container from the downloaded image.

```bash
# Install Docker
sudo apt-get update
sudo apt-get install docker.io

# Pull a Docker image
docker pull ubuntu

# Run a Docker container
docker run -it ubuntu
```

By following these steps, you'll be well on your way to understanding the basics of Docker and containerization.
