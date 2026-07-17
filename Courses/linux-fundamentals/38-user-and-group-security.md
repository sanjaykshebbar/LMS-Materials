---
type: lesson
course: linux-fundamentals
module: "Module 7: Linux Security and Access Control"
order: 38
title: User and Group Security
---

# User and Group Security

> 🎥 [Search YouTube for "User and Group Security"](https://www.youtube.com/results?search_query=User%20and%20Group%20Security%20Linux%20Fundamentals%20tutorial)

User and Group Security
======================

In Linux, security is a top priority, and user and group security play a crucial role in maintaining system integrity. Understanding how users and groups work is essential for managing access control, permissions, and system security.

### User Security

A **user** is an entity that interacts with the system, and each user has a unique **username** and **UID** (User ID). The UID is a numerical value that identifies a user and is used to manage permissions and access control.

#### User Types

There are two primary types of users:

*   **Regular users**: These are users who interact with the system for everyday tasks, such as users who log in to their accounts.
*   **System users**: These are users who are used for system administration tasks, such as **root** (UID 0) and other system accounts.

### Group Security

A **group** is a collection of users who share similar permissions and access control settings. Groups are used to simplify user management and improve security.

#### Group Types

There are two primary types of groups:

*   **Primary groups**: These are the default group assigned to a user when they are created.
*   **Secondary groups**: These are additional groups that a user can be a member of, beyond their primary group.

### User and Group Management

To manage users and groups, you can use the following commands:

```bash
# Create a new user
sudo useradd -m -s /bin/bash newuser

# Create a new group
sudo groupadd newgroup

# Add a user to a group
sudo usermod -aG newgroup newuser

# Remove a user from a group
sudo usermod -rG newgroup newuser
```

### Access Control

Access control is managed through file permissions, which are set using the `chmod` command. The `chmod` command uses a three-digit octal code to set permissions:

```bash
# Set permissions for a file
sudo chmod 755 filename
```

### User and Group Security Best Practices

*   Use strong passwords for all users and groups.
*   Limit user privileges to the minimum required for their tasks.
*   Use groups to simplify user management and improve security.
*   Regularly review and update user and group permissions.

### Mermaid Diagram

```mermaid
graph LR
    A[User] -->|UID| B[Group]
    B -->|GID| C[File]
    C -->|Permissions| D[Access Control]
    D -->|chmod| E[File System]
```

### Example Use Case

Suppose you have a web server with a user `www-data` and a group `www-data`. You want to set permissions for the web server's files to allow read and write access for the `www-data` group. You can use the following command:

```bash
sudo chmod 775 /var/www/html
```

This sets the permissions for the `/var/www/html` directory to allow read, write, and execute access for the owner, read and execute access for the group, and read access for others.

### Image

![User and Group Security](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Linux_user_groups.svg/1200px-Linux_user_groups.svg.png)

This diagram illustrates the relationship between users, groups, and file permissions in Linux.
