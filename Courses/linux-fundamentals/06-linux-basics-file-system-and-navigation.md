---
type: lesson
course: linux-fundamentals
module: "Module 1: Introduction to Linux"
order: 6
title: "Linux Basics: File System and Navigation"
---

# Linux Basics: File System and Navigation

> 🎥 [Search YouTube for "Linux Basics: File System and Navigation"](https://www.youtube.com/results?search_query=Linux%20Basics%3A%20File%20System%20and%20Navigation%20Linux%20Fundamentals%20tutorial)

# Linux Basics: File System and Navigation

Linux is a Unix-like operating system that uses a hierarchical file system structure. Understanding this structure is essential for navigating and managing files on a Linux system.

## File System Structure

The Linux file system is divided into several directories, each with its own purpose. The most important directories are:

* `/` (root directory): The topmost directory in the file system hierarchy.
* `/bin` (binaries): Contains essential system programs and commands.
* `/boot`: Stores the kernel and other boot-related files.
* `/dev`: Device files, which represent hardware devices.
* `/etc` (etcetera): Configuration files for system-wide settings.
* `/home`: User home directories.
* `/lib` (libraries): Contains system libraries.
* `/media`: Mount points for removable media.
* `/mnt`: Temporary mount points for file systems.
* `/opt` (optional): Installable software packages.
* `/proc`: Process information.
* `/root`: The root user's home directory.
* `/run`: Runtime information.
* `/sbin` (system binaries): Contains system programs and commands.
* `/srv`: Service directories.
* `/tmp`: Temporary files.
* `/usr` (user): User-specific data and applications.
* `/var` (variable): Variable data, such as logs and spool files.

## Navigation

To navigate the Linux file system, you'll use the following commands:

* `cd` (change directory): Changes the current working directory.
* `pwd` (print working directory): Displays the current working directory.
* `ls` (list): Lists the contents of the current directory.
* `mkdir` (make directory): Creates a new directory.
* `rm` (remove): Deletes a file or directory.

### Creating and Navigating Directories

Let's create a new directory and navigate to it using the `cd` command:

```bash
# Create a new directory
mkdir my_directory

# Navigate to the new directory
cd my_directory
```

### Listing Directory Contents

To list the contents of the current directory, use the `ls` command:

```bash
# List the contents of the current directory
ls
```

### Understanding File Permissions

In Linux, file permissions are represented by three digits, each representing a different type of permission:

* `r` (read): Allows the owner, group, or others to read the file.
* `w` (write): Allows the owner, group, or others to write to the file.
* `x` (execute): Allows the owner, group, or others to execute the file.

The file permissions can be combined to represent different levels of access. For example:

* `644`: Owner has read and write permissions, group has read permissions, and others have read permissions.
* `755`: Owner has read and write permissions, group has read and execute permissions, and others have read and execute permissions.

### File System Hierarchy

Here's a Mermaid diagram illustrating the Linux file system hierarchy:
```mermaid
graph TB
  A[Root Directory (/)]
  B[Binaries (/bin)]
  C[Boot Files (/boot)]
  D[Device Files (/dev)]
  E[Configuration Files (/etc)]
  F[Home Directories (/home)]
  G[Libraries (/lib)]
  H[Media (/media)]
  I[Mount Points (/mnt)]
  J[Optional Packages (/opt)]
  K[Process Information (/proc)]
  L[Runtime Information (/run)]
  M[Service Directories (/srv)]
  N[Temporary Files (/tmp)]
  O[User Data (/usr)]
  P[Variable Data (/var)]
```

### File System Navigation

Here's an image illustrating the concept of file system navigation:
![File System Navigation](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Unix_file_system.svg/800px-Unix_file_system.svg.png)

This lesson has covered the basics of the Linux file system structure and navigation. With this knowledge, you'll be able to navigate and manage files on a Linux system.
