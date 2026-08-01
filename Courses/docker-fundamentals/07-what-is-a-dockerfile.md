---
type: lesson
course: docker-fundamentals
module: "Module 3: Dockerfiles and Build"
order: 7
title: What is a Dockerfile?
---

# What is a Dockerfile?

> 🎥 [Search YouTube for "What is a Dockerfile?"](https://www.youtube.com/results?search_query=What%20is%20a%20Dockerfile%3F%20Docker%20Fundamentals%20tutorial)

## What is a Dockerfile?

A Dockerfile is a text file that contains a series of instructions, or commands, used to build a Docker image. It is essentially a recipe that tells Docker how to create a new image from a base image, including any necessary configuration, dependencies, and settings.

### Purpose of a Dockerfile

The primary purpose of a Dockerfile is to automate the process of creating a consistent and reliable environment for your application. By using a Dockerfile, you can ensure that your application is deployed in the same way every time, regardless of the environment it's deployed in.

### Structure of a Dockerfile

A Dockerfile typically consists of a series of instructions, or commands, that are executed in order. These instructions can include:

* **FROM**: specifies the base image to use for the new image
* **RUN**: executes a command in the new image
* **COPY**: copies files from the current directory into the new image
* **CMD**: specifies the default command to run when the container is started
* **ENV**: sets an environment variable in the new image

```mermaid
graph LR
    A[FROM] --> B[Base Image]
    B --> C[RUN]
    C --> D[Copy Files]
    D --> E[CMD]
    E --> F[Container]
```

### Example Dockerfile

Here's an example Dockerfile for a simple web server:
```dockerfile
# Use the official Ubuntu image as the base image
FROM ubuntu:latest

# Set the working directory to /app
WORKDIR /app

# Copy the current directory into the new image
COPY . /app

# Install the required packages
RUN apt-get update && apt-get install -y nginx

# Expose the port that the web server will listen on
EXPOSE 80

# Specify the default command to run when the container is started
CMD ["nginx", "-g", "daemon off;"]
```

### Benefits of Using a Dockerfile

Using a Dockerfile provides several benefits, including:

* **Consistency**: ensures that your application is deployed in the same way every time
* **Repeatability**: allows you to easily recreate the same environment on different machines
* **Efficiency**: reduces the time and effort required to set up and deploy your application

![Dockerfile](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Dockerfile.svg/800px-Dockerfile.svg)

By understanding the purpose and structure of a Dockerfile, you can create consistent and reliable environments for your applications, and streamline your development and deployment processes.
