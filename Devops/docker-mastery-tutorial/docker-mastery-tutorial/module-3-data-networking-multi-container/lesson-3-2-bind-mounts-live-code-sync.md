> 🐳 **Docker Mastery — From Zero to Hero** · 3️⃣ Module 3 — Data, Networking & Multi-Container Apps
>
> [⬅️ Prev: Lesson 3.1](./lesson-3-1-volumes-persistent-data.md) · [🏠 Course Home](../README.md) · [Next: Lesson 3.3 ➡️](./lesson-3-3-docker-networking.md)

---

# 📙 Lesson 3.2 — Bind Mounts: Live Code Sync for Development

🎯 **Goal:** Edit code on your machine, see changes instantly inside the container.

### 📖 The Concept

A **bind mount** maps a specific folder on *your machine* directly into the container. Perfect for development — save a file in VS Code, and the container sees it immediately.

| | Named Volume | Bind Mount |
|---|---|---|
| Managed by | Docker | You (exact host path) |
| Best for | **Production data** (databases) | **Development** (live code) |
| Syntax | `-v myvolume:/path` | `-v $(pwd):/path` |

### 💻 Hands-On

```bash
# Serve your current folder with Nginx — edit index.html and refresh!
docker run -d -p 8080:80 \
  -v $(pwd):/usr/share/nginx/html \
  nginx

# Node.js dev with hot reload (nodemon watches your local files)
docker run -it -p 3000:3000 \
  -v $(pwd):/app \
  -w /app \
  node:20-alpine \
  npx nodemon app.js
```

> 💡 On Windows PowerShell use `${PWD}` instead of `$(pwd)`.

### 🔗 References
- 📄 [Bind Mounts — Official Docs](https://docs.docker.com/engine/storage/bind-mounts/)

### ⚡ Challenge
Set up a live-reload dev environment for a simple HTML page: edit locally → refresh browser → see changes, no rebuild.

---

[⬅️ Prev: Lesson 3.1](./lesson-3-1-volumes-persistent-data.md) · [🏠 Course Home](../README.md) · [Next: Lesson 3.3 ➡️](./lesson-3-3-docker-networking.md)
