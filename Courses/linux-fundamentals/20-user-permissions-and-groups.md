---
type: lesson
course: linux-fundamentals
module: "Module 4: User Accounts and Permissions"
order: 20
title: User Permissions and Groups
---

# User Permissions and Groups

> 🎥 [Search YouTube for "User Permissions and Groups"](https://www.youtube.com/results?search_query=User%20Permissions%20and%20Groups%20Linux%20Fundamentals%20tutorial)

User permissions and groups are fundamental concepts in Linux that determine what actions a user can perform on a system. Understanding these concepts is crucial for managing and securing your Linux system.

## User Permissions

In Linux, user permissions determine what actions a user can perform on a file or directory. There are three types of permissions:

* **Read** (r): allows the user to view the contents of a file or directory
* **Write** (w): allows the user to modify the contents of a file or directory
* **Execute** (x): allows the user to run a file as a program

Permissions are represented by three digits, with each digit representing the permissions for the owner, group, and others, respectively. For example, the permission `755` means:

* The owner has read, write, and execute permissions (7)
* The group has read and execute permissions (5)
* Others have read and execute permissions (5)

### Permission Modes

There are three permission modes:

* **User** (u): permissions for the owner of the file
* **Group** (g): permissions for the group that owns the file
* **Other** (o): permissions for all users not in the group

### Groups

Groups are a way to organize users with similar access requirements. A group is a collection of users who share the same permissions. Groups are used to simplify permission management and make it easier to apply permissions to multiple users.

```mermaid
graph LR
    A[User] -->|belongs to|> B[Group]
    B -->|has permissions|> C[File]
    C -->|owned by|> D[Group]
    D -->|has permissions|> E[Other]
```

### Managing Groups

To manage groups, you can use the following commands:

* `groupadd`: adds a new group
* `groupdel`: deletes a group
* `groupmod`: modifies a group
* `groups`: displays the groups a user belongs to

```bash
# Add a new group
sudo groupadd developers

# Delete a group
sudo groupdel developers

# Modify a group
sudo groupmod -g 1001 developers

# Display groups for the current user
groups
```

### Real-World Example

Imagine you have a web server with multiple users who need to edit files in the `/var/www` directory. You can create a group called `www-data` and add all the users to this group. Then, you can set the permissions for the `/var/www` directory to `775`, allowing the owner (the web server) to have read, write, and execute permissions, the group to have read and execute permissions, and others to have read and execute permissions.

```bash
sudo chgrp www-data /var/www
sudo chmod 775 /var/www
```

![Group Permissions](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Linux_file_permissions.svg/800px-Linux_file_permissions.svg.png)

This is a basic overview of user permissions and groups in Linux. Understanding these concepts is essential for managing and securing your Linux system.
