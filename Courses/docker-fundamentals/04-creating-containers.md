---
type: lesson
course: docker-fundamentals
module: "Module 2: Containerization"
order: 4
title: Creating Containers
---

# Creating Containers

> 🎥 [Search YouTube for "Creating Containers"](https://www.youtube.com/results?search_query=Creating%20Containers%20Docker%20Fundamentals%20tutorial)

# Creating Containers
=======================

Creating a container is the first step in containerization. A container is a lightweight and portable package that includes everything an application needs to run, including the code, libraries, and dependencies. In this lesson, we will learn how to create and run Docker containers.

## What is a Container?
------------------------

A container is a **self-contained** environment that includes the application code, libraries, and dependencies. Containers are **lightweight** and **portable**, making them ideal for development, testing, and production environments.

## Creating a Container
------------------------

To create a container, we need to create a **Dockerfile**, which is a text file that contains instructions for building a Docker image. A Dockerfile typically includes the following:

* **FROM**: specifies the base image to use for the container
* **COPY**: copies files from the host machine into the container
* **RUN**: executes a command to install dependencies or perform other setup tasks
* **CMD**: specifies the default command to run when the container starts

Here is an example of a simple Dockerfile:
```dockerfile
# Use the official Python image as the base
FROM python:3.9-slim

# Copy the application code into the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Set the default command to run when the container starts
CMD ["python", "app.py"]
```
## Building a Container Image
--------------------------------

Once we have a Dockerfile, we can build a container image using the following command:
```bash
docker build -t my-container .
```
This command tells Docker to build an image with the tag `my-container` using the instructions in the Dockerfile.

## Running a Container
-------------------------

To run a container, we need to start a container from the image we just built. We can do this using the following command:
```bash
docker run -p 8000:8000 my-container
```
This command tells Docker to start a container from the `my-container` image and map port 8000 on the host machine to port 8000 in the container.

## Mermaid Diagram: Container Creation
-----------------------------------------

```mermaid
graph LR
    A[Create Dockerfile] --> B[Build Image]
    B --> C[Create Container]
    C --> D[Run Container]
    D --> E[Container Running]
```
## Illustrative Image
----------------------

[Image of a container ship](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Container_ship_%28cropped%29.jpg/800px-Container_ship_%28cropped%29.jpg)

In this image, a container ship is shown carrying containers. This is a metaphor for the containerization process, where containers are carried and transported between environments.

## Conclusion
----------

In this lesson, we learned how to create and run Docker containers. We created a Dockerfile, built a container image, and ran a container from that image. We also saw a Mermaid diagram illustrating the container creation process. With this knowledge, we can start building and running our own containers for development, testing, and production environments.
