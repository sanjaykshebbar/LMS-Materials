---
title: 📘 Lesson 2.2 — Writing Your First Dockerfile
category: Devops
tags: [Obsidian-Sync]
---
> 🐳 **Docker Mastery — From Zero to Hero** · 2️⃣ Module 2 — Images & Dockerfiles
>
> [⬅️ Prev: Lesson 2.1](./lesson-2-1-images-and-layers.md) · [🏠 Course Home](../README.md) · [Next: Lesson 2.3 ➡️](./lesson-2-3-building-tagging-running.md)

---

# 📘 Lesson 2.2 — Writing Your First Dockerfile

🎯 **Goal:** Write a Dockerfile from scratch and understand every instruction.

### 💻 Hands-On — Dockerize a Node.js App

**`app.js`**
```javascript
const http = require('http');
http.createServer((req, res) => {
  res.end('🐳 Hello from inside a container!');
}).listen(3000);
console.log('Server running on port 3000');
```

**`Dockerfile`**
```dockerfile
# 1. Base image — start from official Node
FROM node:20-alpine

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy dependency manifest first (cache trick! see Lesson 2.5)
COPY package*.json ./

# 4. Install dependencies
RUN npm install

# 5. Copy the rest of the source code
COPY . .

# 6. Document the port the app listens on
EXPOSE 3000

# 7. Command to run when the container starts
CMD ["node", "app.js"]
```

### 🧠 Instruction Reference

| Instruction | Purpose |
|-------------|---------|
| `FROM` | Base image to build on |
| `WORKDIR` | `cd` into a folder (creates it if missing) |
| `COPY` | Copy files from your machine into the image |
| `RUN` | Execute a command **at build time** |
| `EXPOSE` | Documentation of the listening port |
| `CMD` | Default command **at run time** (only the last one counts) |
| `ENTRYPOINT` | Like CMD, but harder to override — good for CLI tools |

> 💡 **RUN vs CMD:** `RUN` happens while *building* the image (e.g., installing packages). `CMD` happens when the *container starts* (e.g., launching your server).

### 🔗 References
- 📄 [Dockerfile Reference — Official](https://docs.docker.com/reference/dockerfile/)
- 📄 [Dockerfile Best Practices](https://docs.docker.com/build/building/best-practices/)

### ⚡ Challenge
Write a Dockerfile for a Python app that installs from `requirements.txt` and runs `main.py`.

---

[⬅️ Prev: Lesson 2.1](./lesson-2-1-images-and-layers.md) · [🏠 Course Home](../README.md) · [Next: Lesson 2.3 ➡️](./lesson-2-3-building-tagging-running.md)
