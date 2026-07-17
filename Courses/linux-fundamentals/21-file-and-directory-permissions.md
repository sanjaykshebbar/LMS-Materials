---
type: lesson
course: linux-fundamentals
module: "Module 4: User Accounts and Permissions"
order: 21
title: File and Directory Permissions
---

# File and Directory Permissions

> 🎥 [Search YouTube for "File and Directory Permissions"](https://www.youtube.com/results?search_query=File%20and%20Directory%20Permissions%20Linux%20Fundamentals%20tutorial)

**File and Directory Permissions**
=====================================

In Linux, permissions determine who can read, write, or execute files and directories. Understanding file and directory permissions is crucial for managing access control and ensuring data security.

### What are File and Directory Permissions?

File and directory permissions are used to control access to files and directories. They are represented by a set of three numbers, known as the **permissions triplet**, which describe the permissions for the owner, group, and others.

### Permissions Triplet

The permissions triplet is a three-digit number that represents the permissions for the owner, group, and others. The digits are as follows:

* The first digit represents the permissions for the **owner** (user who owns the file or directory).
* The second digit represents the permissions for the **group** (group that owns the file or directory).
* The third digit represents the permissions for **others** (everyone else).

Each digit is composed of three parts:

* **Read (r)**: 4
* **Write (w)**: 2
* **Execute (x)**: 1

### Permissions Notation

Permissions can be represented using a notation that combines the three digits. For example:

* `rwx` represents read, write, and execute permissions (7)
* `rw-` represents read and write permissions (6)
* `r--` represents read-only permission (4)

### Setting Permissions

Permissions can be set using the `chmod` command. The `chmod` command takes two arguments: the permissions notation and the file or directory path.

```bash
# Set read, write, and execute permissions for the owner
chmod 700 file.txt

# Set read and write permissions for the group
chmod 660 file.txt

# Set read-only permission for others
chmod 444 file.txt
```

### Directory Permissions

Directory permissions work similarly to file permissions. However, directories have an additional permission: **execute**. This permission allows the directory to be traversed.

```bash
# Set execute permission for the owner
chmod 711 directory

# Set execute permission for the group
chmod 755 directory
```

### Mermaid Diagram: Permissions Flowchart

```mermaid
graph LR
    A[User] -->|owns file|> B[File]
    B -->|has permissions|> C[Permissions Triplet]
    C -->|owner|> D[Owner Permissions]
    C -->|group|> E[Group Permissions]
    C -->|others|> F[Others Permissions]
    D -->|read|> G[Read]
    D -->|write|> H[Write]
    D -->|execute|> I[Execute]
    E -->|read|> G
    E -->|write|> H
    E -->|execute|> I
    F -->|read|> G
    F -->|write|> H
    F -->|execute|> I
```

### Example Use Case

Suppose you have a file `secret.txt` that contains sensitive information. You want to set permissions so that only the owner can read and write the file, while others can only read it.

```bash
# Set permissions for the owner
chmod 600 secret.txt

# Set read-only permission for others
chmod 444 secret.txt
```

This will ensure that only the owner can modify the file, while others can only read it.

### Image: Permissions Diagram

![Permissions Diagram](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Unix_permissions_diagram.svg/800px-Unix_permissions_diagram.svg.png)

Note: This image is a diagram of the permissions triplet and is used to illustrate the concept of permissions.
