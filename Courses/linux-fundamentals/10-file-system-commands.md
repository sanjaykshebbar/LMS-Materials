---
type: lesson
course: linux-fundamentals
module: "Module 2: Linux File System and Navigation"
order: 10
title: File System Commands
---

# File System Commands

> 🎥 [Search YouTube for "File System Commands"](https://www.youtube.com/results?search_query=File%20System%20Commands%20Linux%20Fundamentals%20tutorial)

### File System Commands

Linux file system commands are essential for managing files and directories on your system. In this lesson, we will cover the basic file system commands and their usage.

#### Introduction

The Linux file system is a hierarchical structure that consists of files and directories. Files are stored in directories, and directories are stored in other directories. The root directory `/` is the topmost directory in the file system hierarchy. Understanding file system commands is crucial for navigating and managing files and directories on your Linux system.

#### Basic File System Commands

Here are some basic file system commands that you should know:

* **`cd`**: Change Directory. This command is used to navigate to a different directory.
* **`mkdir`**: Make Directory. This command is used to create a new directory.
* **`rmdir`**: Remove Directory. This command is used to delete an empty directory.
* **`ls`**: List. This command is used to display the contents of a directory.
* **`cp`**: Copy. This command is used to copy files and directories.
* **`mv`**: Move. This command is used to move or rename files and directories.
* **`rm`**: Remove. This command is used to delete files and directories.

#### Using `cd` and `ls` Commands

Here's an example of how to use the `cd` and `ls` commands:

```bash
# Navigate to the home directory
cd ~

# List the contents of the home directory
ls
```

This will display the contents of the home directory.

#### Using `mkdir` and `rmdir` Commands

Here's an example of how to use the `mkdir` and `rmdir` commands:

```bash
# Create a new directory called "mydir"
mkdir mydir

# List the contents of the current directory
ls

# Remove the "mydir" directory
rmdir mydir
```

This will create a new directory called "mydir", list the contents of the current directory, and then remove the "mydir" directory.

#### Using `cp` and `mv` Commands

Here's an example of how to use the `cp` and `mv` commands:

```bash
# Copy a file called "file.txt" to a new location
cp file.txt new_location

# Move a file called "file.txt" to a new location
mv file.txt new_location
```

This will copy the "file.txt" file to a new location and then move the "file.txt" file to a new location.

#### Mermaid Diagram: File System Hierarchy

```mermaid
graph LR
    A[Root Directory (/)] --> B[Home Directory (~)]
    B --> C[Documents Directory]
    B --> D[Pictures Directory]
    C --> E[Text Files]
    C --> F[Spreadsheets]
    D --> G[Photos]
    D --> H[Videos]
```

This diagram shows the file system hierarchy, with the root directory `/` at the top and the home directory `~` below it.

#### Conclusion

In this lesson, we covered the basic file system commands and their usage. We learned how to navigate to different directories using the `cd` command, list the contents of a directory using the `ls` command, create a new directory using the `mkdir` command, remove an empty directory using the `rmdir` command, copy files and directories using the `cp` command, move or rename files and directories using the `mv` command, and delete files and directories using the `rm` command.

[Image: A diagram of a file system hierarchy. Source: https://commons.wikimedia.org/wiki/File:File_system_hierarchy.svg]

Note: The image is a diagram of a file system hierarchy, which illustrates the concept of a hierarchical file system structure.
