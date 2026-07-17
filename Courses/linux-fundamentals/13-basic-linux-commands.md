---
type: lesson
course: linux-fundamentals
module: "Module 3: Linux Commands and Syntax"
order: 13
title: Basic Linux Commands
---

# Basic Linux Commands

> 🎥 [Search YouTube for "Basic Linux Commands"](https://www.youtube.com/results?search_query=Basic%20Linux%20Commands%20Linux%20Fundamentals%20tutorial)

### Basic Linux Commands

Linux commands are the backbone of any Linux system. They allow users to interact with the system, perform tasks, and manage files and directories. In this lesson, we will cover some of the most basic Linux commands that you should know.

#### Navigation Commands

Navigation commands are used to move around the file system and perform tasks related to file management.

* **cd** (change directory): used to change the current working directory.
```bash
cd ~
```
* **pwd** (print working directory): used to print the current working directory.
```bash
pwd
```
* **ls** (list): used to list the files and directories in the current working directory.
```bash
ls -l
```
* **mkdir** (make directory): used to create a new directory.
```bash
mkdir mydir
```
* **rmdir** (remove directory): used to remove an empty directory.
```bash
rmdir mydir
```

#### File and Directory Management Commands

File and directory management commands are used to create, delete, and manage files and directories.

* **touch**: used to create a new empty file.
```bash
touch myfile.txt
```
* **rm** (remove): used to delete a file or directory.
```bash
rm myfile.txt
```
* **cp** (copy): used to copy a file or directory.
```bash
cp myfile.txt mydir
```
* **mv** (move): used to move or rename a file or directory.
```bash
mv myfile.txt mydir
```

#### Viewing and Editing Commands

Viewing and editing commands are used to view and edit files.

* **cat**: used to view the contents of a file.
```bash
cat myfile.txt
```
* **less**: used to view the contents of a file one page at a time.
```bash
less myfile.txt
```
* **nano** or **vim**: used to edit a file.
```bash
nano myfile.txt
```

#### System Information Commands

System information commands are used to view system information.

* **uname** (Unix name): used to view system information.
```bash
uname -a
```
* **hostname**: used to view the system hostname.
```bash
hostname
```
* **date**: used to view the current date and time.
```bash
date
```

### Mermaid Diagram: File System Navigation

```mermaid
graph LR
    A[Home Directory] -->|cd|> B[Current Working Directory]
    B -->|pwd|> C[Print Working Directory]
    C -->|ls|> D[List Files and Directories]
    D -->|mkdir|> E[Create New Directory]
    E -->|rmdir|> F[Remove Empty Directory]
```

### Image: File System Structure

![File System Structure](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Linux_file_system_structure.svg/800px-Linux_file_system_structure.svg.png)

This diagram shows the basic structure of a Linux file system. The root directory (`/`) is the topmost directory, and all other directories are located under it. The `home` directory is where user home directories are located, and the `bin` directory contains executable files.
