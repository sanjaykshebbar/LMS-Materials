---
type: lesson
course: linux-fundamentals
module: "Module 2: Linux File System and Navigation"
order: 9
title: File Permissions and Ownership
---

# File Permissions and Ownership

> 🎥 [Search YouTube for "File Permissions and Ownership"](https://www.youtube.com/results?search_query=File%20Permissions%20and%20Ownership%20Linux%20Fundamentals%20tutorial)

**Understanding File Permissions and Ownership in Linux**
=====================================================

Linux is a multi-user operating system, which means that multiple users can share the same system and access its resources. To ensure that each user can manage their own files and data securely, Linux uses a system of file permissions and ownership. In this lesson, we will explore the basics of file permissions and ownership in Linux.

### What are File Permissions?

File permissions determine who can read, write, and execute files on a Linux system. Each file has three types of permissions:

* **Read (r)**: allows a user to view the contents of a file
* **Write (w)**: allows a user to modify a file
* **Execute (x)**: allows a user to run a file as a program

These permissions are represented by three sets of letters: `rwx` for the owner, `rwx` for the group, and `rwx` for others. For example, if a file has the permissions `rw-`, it means the owner has read and write permissions, but others do not have any permissions.

### What is Ownership?

Ownership refers to the user or group that has control over a file. In Linux, each file has an owner, a group, and a set of permissions. The owner is the user who created the file, and the group is a collection of users who share the same permissions.

```bash
# Display file ownership and permissions
ls -l filename
```

### Understanding File Permissions with a Mermaid Diagram
```mermaid
graph LR
    A[File] -->|Owner|> B[User]
    B -->|Group|> C[Group]
    C -->|Others|> D[Others]
    A -->|Permissions|> E[rwx]
    E -->|Read|> F[r]
    F -->|Write|> G[w]
    G -->|Execute|> H[x]
```

### Setting File Permissions

To set file permissions, you can use the `chmod` command. The `chmod` command takes a three-digit number that represents the permissions for the owner, group, and others. For example, to set the permissions to `rw-`, you would use the command:

```bash
chmod 640 filename
```

You can also use symbolic notation to set permissions. For example, to set the permissions to `rw-`, you would use the command:

```bash
chmod u=rw,g=,o= filename
```

### Best Practices for File Permissions

* Always use the `chmod` command to set file permissions, rather than using the `chown` command to change ownership.
* Use symbolic notation to set permissions for clarity and readability.
* Be mindful of file permissions when sharing files with others to prevent unauthorized access.

### Image: File Permissions Diagram
![File Permissions Diagram](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/File_permissions.svg/800px-File_permissions.svg.png)

In this lesson, we have covered the basics of file permissions and ownership in Linux. Understanding file permissions and ownership is crucial for managing files securely and efficiently on a Linux system.
