---
type: lesson
course: linux-fundamentals
module: "Module 3: Linux Commands and Syntax"
order: 15
title: Command-Line Editing and Navigation
---

# Command-Line Editing and Navigation

> 🎥 [Search YouTube for "Command-Line Editing and Navigation"](https://www.youtube.com/results?search_query=Command-Line%20Editing%20and%20Navigation%20Linux%20Fundamentals%20tutorial)

Command-Line Editing and Navigation
=====================================

As you become more comfortable with the Linux command line, you'll want to learn how to edit and navigate within the terminal. This lesson will cover the basics of command-line editing and navigation, including how to move around the command line, delete and insert text, and use the command history.

### Command-Line Navigation

Navigation is a crucial part of using the command line. You'll use various keys to move around the terminal, select text, and execute commands.

#### Moving Around the Command Line

To move around the command line, you'll use the following keys:

*   **Home**: Move the cursor to the beginning of the line.
*   **End**: Move the cursor to the end of the line.
*   **Left Arrow**: Move the cursor one character to the left.
*   **Right Arrow**: Move the cursor one character to the right.
*   **Ctrl + A**: Move the cursor to the beginning of the line.
*   **Ctrl + E**: Move the cursor to the end of the line.
*   **Ctrl + F**: Move the cursor one character to the right.
*   **Ctrl + B**: Move the cursor one character to the left.

#### Selecting Text

To select text, you'll use the following keys:

*   **Shift + Left Arrow**: Select one character to the left.
*   **Shift + Right Arrow**: Select one character to the right.
*   **Shift + Home**: Select from the cursor to the beginning of the line.
*   **Shift + End**: Select from the cursor to the end of the line.

### Command-Line Editing

Editing is an essential part of using the command line. You'll use various keys to delete and insert text.

#### Deleting Text

To delete text, you'll use the following keys:

*   **Backspace**: Delete the character to the left of the cursor.
*   **Ctrl + H**: Delete the character to the left of the cursor.
*   **Ctrl + K**: Delete from the cursor to the end of the line.
*   **Ctrl + U**: Delete from the cursor to the beginning of the line.

#### Inserting Text

To insert text, you'll use the following keys:

*   **Insert**: Toggle insert mode on and off.
*   **Ctrl + V**: Paste text from the clipboard.
*   **Ctrl + Y**: Paste text from the clipboard (alternative to Ctrl + V).

### Command History

The command history is a list of previous commands you've entered. You can use the following keys to navigate and execute commands from the history:

*   **Up Arrow**: Move up one command in the history.
*   **Down Arrow**: Move down one command in the history.
*   **Ctrl + R**: Search the command history.
*   **Ctrl + P**: Execute the previous command.
*   **Ctrl + N**: Execute the next command.

```mermaid
graph LR
    A[Insert text] -->|Ctrl + V| B[Paste text]
    A -->|Ctrl + Y| C[Paste text (alternative)]
    B -->|Ctrl + K| D[Delete from cursor to end]
    C -->|Ctrl + U| E[Delete from cursor to beginning]
    D -->|Backspace| F[Delete character to left]
    E -->|Ctrl + H| G[Delete character to left]
```

### Tips and Tricks

*   Use the `history` command to view the command history.
*   Use the `!!` command to execute the last command.
*   Use the `!$` command to execute the last argument of the previous command.

[Image: A screenshot of a terminal with the command line editing and navigation keys highlighted.](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Linux_terminal.png/800px-Linux_terminal.png)

### Conclusion

In this lesson, you've learned the basics of command-line editing and navigation. You can now move around the command line, select text, delete and insert text, and use the command history. Practice these skills to become more comfortable with the command line.
