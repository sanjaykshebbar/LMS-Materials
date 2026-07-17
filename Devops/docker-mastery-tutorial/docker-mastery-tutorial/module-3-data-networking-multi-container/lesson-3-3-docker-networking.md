---
title: "📙 Lesson 3.3 — Docker Networking: Containers Talking to Each Other"
category: Devops
tags: [Obsidian-Sync]
---
> 🐳 **Docker Mastery — From Zero to Hero** · 3️⃣ Module 3 — Data, Networking & Multi-Container Apps
>
> [⬅️ Prev: Lesson 3.2](./lesson-3-2-bind-mounts-live-code-sync.md) · [🏠 Course Home](../README.md) · [Next: Lesson 3.4 ➡️](./lesson-3-4-environment-variables-and-config.md)

---

# 📙 Lesson 3.3 — Docker Networking: Containers Talking to Each Other

🎯 **Goal:** Connect containers by name on custom networks.

### 📖 The Concept

Docker's killer networking feature: on a **user-defined network**, containers can reach each other **by container name** — Docker provides built-in DNS. No IP addresses needed!

### 💻 Hands-On

```bash
# 1. Create a network
docker network create my-net

# 2. Run MongoDB on it
docker run -d --name mongodb --network my-net \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=secret \
  mongo

# 3. Run Mongo Express (a web UI) on the SAME network
docker run -d --name mongo-ui --network my-net -p 8081:8081 \
  -e ME_CONFIG_MONGODB_ADMINUSERNAME=admin \
  -e ME_CONFIG_MONGODB_ADMINPASSWORD=secret \
  -e ME_CONFIG_MONGODB_SERVER=mongodb \
  mongo-express
```

Notice: `ME_CONFIG_MONGODB_SERVER=mongodb` — the UI finds the database **by its container name**. 🪄

### 🧠 Network Types

| Network | What It Does |
|---------|-------------|
| `bridge` (default) | Private network on one host — but no name-based DNS! |
| **user-defined bridge** ⭐ | Same, PLUS DNS by container name — always use this |
| `host` | Container shares the host's network directly (no port mapping) |
| `none` | No networking at all (max isolation) |

### 🔗 References
- 📄 [Docker Networking — Official Docs](https://docs.docker.com/engine/network/)

### ⚡ Challenge
Create a network with a Redis container and an Alpine container. From inside Alpine, install `redis-cli` and ping Redis by name.

---

[⬅️ Prev: Lesson 3.2](./lesson-3-2-bind-mounts-live-code-sync.md) · [🏠 Course Home](../README.md) · [Next: Lesson 3.4 ➡️](./lesson-3-4-environment-variables-and-config.md)
