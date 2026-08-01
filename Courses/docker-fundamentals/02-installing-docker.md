---
type: lesson
course: docker-fundamentals
module: "Module 1: Introduction to Docker"
order: 2
title: Installing Docker
---

# Installing Docker

> 🎥 [Search YouTube for "Installing Docker"](https://www.youtube.com/results?search_query=Installing%20Docker%20Docker%20Fundamentals%20tutorial)

# Installing Docker
## Introduction
Docker is a containerization platform that allows you to package, ship, and run applications in a consistent and reliable manner. To get started with Docker, you'll need to install it on your local machine. In this lesson, we'll walk through the process of installing Docker on a Linux or macOS system.

## Prerequisites
Before installing Docker, make sure you have the following:
* A Linux or macOS system with a compatible architecture (x86-64 or ARM64)
* A stable internet connection
* Administrative privileges (sudo or root access)

## Installing Docker on Linux
To install Docker on Linux, follow these steps:

1. Update the package index:
```bash
sudo apt update
```
2. Install the Docker package:
```bash
sudo apt install docker.io
```
3. Start the Docker service:
```bash
sudo systemctl start docker
```
4. Verify the installation by running:
```bash
docker --version
```

## Installing Docker on macOS
To install Docker on macOS, you'll need to use the official Docker Desktop installation package. Follow these steps:

1. Download the Docker Desktop package from the official Docker website:
```bash
curl -fsSL https://download.docker.com/mac/latest/dockerd-mac-amd64.zip -o /tmp/dockerd-mac-amd64.zip
```
2. Extract the package:
```bash
unzip /tmp/dockerd-mac-amd64.zip -d /tmp
```
3. Install the package:
```bash
sudo installer -package /tmp/Docker\ Desktop.pkg -target /
```
4. Start the Docker service:
```bash
brew services start docker
```

## Verifying the Installation
Once you've installed Docker, verify the installation by running:
```bash
docker run -it --rm alpine /bin/ash
```
This command will download the Alpine Linux image and run a shell inside it. If Docker is installed correctly, you should see a shell prompt.

## Architecture
Here's a high-level architecture of the Docker installation process:
```mermaid
graph LR
    A[Local Machine] -->|Install|> B[Docker Package]
    B -->|Extract|> C[Docker Binaries]
    C -->|Run|> D[Docker Service]
    D -->|Verify|> E[Docker CLI]
    E -->|Use|> F[Docker Containers]
```
In this architecture, we have the local machine (A) installing the Docker package (B), which extracts the Docker binaries (C). The Docker service is then run (D), and the Docker CLI is verified (E). Finally, we can use the Docker CLI to create and manage containers (F).

## Conclusion
Installing Docker on your local machine is a straightforward process. By following the steps outlined in this lesson, you should now have Docker installed and ready to use. In the next lesson, we'll explore the basics of Docker and how to create and manage containers.
