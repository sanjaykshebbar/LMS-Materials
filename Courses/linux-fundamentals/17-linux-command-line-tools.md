---
type: lesson
course: linux-fundamentals
module: "Module 3: Linux Commands and Syntax"
order: 17
title: Linux Command-Line Tools
---

# Linux Command-Line Tools

> 🎥 [Search YouTube for "Linux Command-Line Tools"](https://www.youtube.com/results?search_query=Linux%20Command-Line%20Tools%20Linux%20Fundamentals%20tutorial)

## Linux Command-Line Tools

Linux provides a vast array of command-line tools that can be used to manage files, navigate directories, and execute tasks. These tools are essential for any Linux user, and mastering them will make you a more efficient and effective user.

### Essential Tools

*   **cd**: Changes the current directory to the specified path.
*   **mkdir**: Makes a new directory.
*   **rm**: Removes a file or directory.
*   **cp**: Copies a file or directory.
*   **mv**: Moves or renames a file or directory.
*   **ls**: Lists the contents of the current directory.

### File Management

Linux provides several tools for managing files. The `cp` command is used to copy files, and the `mv` command is used to move or rename files. The `rm` command is used to delete files.

```bash
# Copy a file
cp source.txt destination.txt

# Move a file
mv source.txt destination.txt

# Delete a file
rm file.txt
```

### Navigation

The `cd` command is used to change the current directory. You can use the `cd` command with a directory path to navigate to a specific directory.

```bash
# Change to the home directory
cd ~

# Change to the Documents directory
cd ~/Documents
```

### File Information

The `ls` command is used to list the contents of the current directory. You can use the `ls` command with options to display detailed information about files.

```bash
# List the contents of the current directory
ls

# List the contents of the current directory in a long format
ls -l
```

### File Permissions

The `chmod` command is used to change the permissions of a file. You can use the `chmod` command with options to set the permissions.

```bash
# Change the permissions of a file
chmod 755 file.txt
```

### **File System Hierarchy**

The Linux file system hierarchy is structured in the following way:

```mermaid
graph LR
    subgraph /dev
        /dev/null
        /dev/zero
        /dev/full
        /dev/tty
        /dev/random
        /dev/urandom
    end

    subgraph /proc
        /proc/cpuinfo
        /proc/meminfo
        /proc/stat
        /proc/loadavg
        /proc/[pid]/stat
        /proc/[pid]/status
    end

    subgraph /sys
        /sys/class
        /sys/class/net
        /sys/class/scsi_device
        /sys/class/scsi_disk
    end

    subgraph /
        /bin
        /boot
        /dev
        /etc
        /home
        /lib
        /lib64
        /media
        /mnt
        /opt
        /proc
        /root
        /run
        /sbin
        /srv
        /sys
        /tmp
        /usr
        /var
    end
```

### **File System Structure**

The Linux file system structure is as follows:

![Linux File System Structure](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Linux_file_system_structure.svg/800px-Linux_file_system_structure.svg)

This lesson has covered the essential tools for managing files and navigating directories in Linux. It has also covered the file system hierarchy and structure. With these tools and concepts, you will be able to efficiently manage files and navigate directories in Linux.
