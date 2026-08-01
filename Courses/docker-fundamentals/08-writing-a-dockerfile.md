---
type: lesson
course: docker-fundamentals
module: "Module 3: Dockerfiles and Build"
order: 8
title: Writing a Dockerfile
---

# Writing a Dockerfile

> 🎥 [Search YouTube for "Writing a Dockerfile"](https://www.youtube.com/results?search_query=Writing%20a%20Dockerfile%20Docker%20Fundamentals%20tutorial)

Writing a Dockerfile
================

A Dockerfile is a text file that contains instructions for building a Docker image. It's a recipe for creating a Docker image that can be used to deploy your application. The Dockerfile is used by the `docker build` command to create a new image from the instructions in the file.

### What is a Dockerfile?

A Dockerfile is a text file that contains a series of instructions, one per line, that are executed in order to create a Docker image. The instructions in a Dockerfile are used to specify the base image, copy files into the image, install dependencies, and set environment variables.

### Basic Dockerfile Instructions

Here are some basic Dockerfile instructions:

* `FROM`: Specifies the base image to use for the new image.
* `RUN`: Executes a command in a new layer on top of the current image.
* `COPY`: Copies files or directories from the current directory into the new image.
* `WORKDIR`: Sets the working directory in the new image.
* `EXPOSE`: Exposes a port from the container so that it can be accessed from the host machine.
* `CMD`: Specifies the default command to run when the container is started.

### Example Dockerfile

Here's an example Dockerfile that creates a simple web server:
```dockerfile
# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose the port
EXPOSE 8000

# Run the command to start the web server
CMD ["python", "app.py"]
```
### Building an Image from a Dockerfile

To build an image from a Dockerfile, you can use the `docker build` command. Here's an example:
```bash
docker build -t my-web-server .
```
This will build an image with the tag `my-web-server` from the instructions in the Dockerfile in the current directory.

### Mermaid Diagram: Dockerfile Workflow

```mermaid
graph LR
    A[Create Dockerfile] -->|specify instructions|> B[Build Image]
    B -->|use base image|> C[Install Dependencies]
    C -->|copy files|> D[Set Environment Variables]
    D -->|expose port|> E[Run Container]
    E -->|start web server|> F[Access Web Server]
```
### Best Practices for Writing a Dockerfile

Here are some best practices to keep in mind when writing a Dockerfile:

* Use a consistent naming convention for your images and tags.
* Use the `FROM` instruction to specify the base image.
* Use the `RUN` instruction to install dependencies and execute commands.
* Use the `COPY` instruction to copy files and directories into the image.
* Use the `WORKDIR` instruction to set the working directory.
* Use the `EXPOSE` instruction to expose ports from the container.
* Use the `CMD` instruction to specify the default command to run when the container is started.

### Image: Dockerfile Structure

![Dockerfile Structure](https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Dockerfile_Structure.svg/800px-Dockerfile_Structure.svg.png)

Note: This image illustrates the basic structure of a Dockerfile, including the FROM, RUN, COPY, WORKDIR, EXPOSE, and CMD instructions.
