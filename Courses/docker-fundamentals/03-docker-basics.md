---
type: lesson
course: docker-fundamentals
module: "Module 1: Introduction to Docker"
order: 3
title: Docker Basics
---

# Docker Basics

> 🎥 [Search YouTube for "Docker Basics"](https://www.youtube.com/results?search_query=Docker%20Basics%20Docker%20Fundamentals%20tutorial)

**Introduction to Docker**
==========================

Docker is a containerization platform that allows developers to package, ship, and run applications in containers. Containers are lightweight and portable, making them an ideal choice for deploying applications in cloud-native environments. In this lesson, we will cover the basic Docker commands and how to use them to manage containers.

### What is Docker?

Docker is a containerization platform that uses a container runtime to create and manage containers. Containers are isolated from each other and from the host system, providing a consistent and reliable way to deploy applications.

### Key Concepts

* **Container**: A lightweight and portable package of an application and its dependencies.
* **Image**: A snapshot of a container that can be used to create new containers.
* **Dockerfile**: A text file that contains instructions for building a Docker image.
* **Container Runtime**: The software that runs containers on a host system.

### Basic Docker Commands

Here are some basic Docker commands that you should know:

* **docker ps**: Lists all running containers.
* **docker ps -a**: Lists all containers, including stopped ones.
* **docker run**: Runs a new container from an image.
* **docker stop**: Stops a running container.
* **docker rm**: Removes a stopped container.
* **docker rmi**: Removes an image.

### Creating a Docker Container

To create a Docker container, you need to run the `docker run` command followed by the name of the image you want to use. For example:
```bash
docker run -it ubuntu /bin/bash
```
This will create a new container from the official Ubuntu image and open a bash shell in it.

### Docker Architecture

Here is a high-level architecture of the Docker ecosystem:
```mermaid
graph LR
    A[Host System] -->|Container Runtime|> B[Container]
    B -->|Image|> C[Docker Image]
    C -->|Dockerfile|> D[Dockerfile]
```
In this diagram, the host system runs the container runtime, which in turn runs the container. The container is created from a Docker image, which is built from a Dockerfile.

### Example Use Case

Let's say you want to deploy a web application that uses Node.js and MongoDB. You can create a Dockerfile that installs Node.js and MongoDB, copies the application code into the container, and sets up the environment variables. You can then build the Docker image and run a new container from it.

Here is an example Dockerfile:
```dockerfile
FROM node:14

# Install dependencies
RUN npm install

# Copy application code
COPY . /app

# Expose port 3000
EXPOSE 3000

# Run the application
CMD ["node", "app.js"]
```
You can then build the image with the following command:
```bash
docker build -t my-web-app .
```
And run a new container with:
```bash
docker run -p 3000:3000 my-web-app
```
This will start the web application and make it available on port 3000.

### Conclusion

In this lesson, we covered the basic Docker commands and how to use them to manage containers. We also covered the key concepts of containers, images, and Dockerfiles. We then walked through an example use case of deploying a web application using Docker.

[Image: A simple diagram of a container running on a host system. Source: https://commons.wikimedia.org/wiki/File:Containerization.svg]
