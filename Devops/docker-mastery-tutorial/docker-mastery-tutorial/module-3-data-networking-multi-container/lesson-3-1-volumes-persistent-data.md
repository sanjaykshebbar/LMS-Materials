---
title: "📙 Lesson 3.1 — Volumes: Making Data Survive"
category: Devops
tags: [Obsidian-Sync]
---
> 🐳 **Docker Mastery — From Zero to Hero** · 3️⃣ Module 3 — Data, Networking & Multi-Container Apps
>
> [⬅️ Prev: Lesson 2.5](../module-2-images-and-dockerfiles/lesson-2-5-image-optimization-multi-stage-builds.md) · [🏠 Course Home](../README.md) · [Next: Lesson 3.2 ➡️](./lesson-3-2-bind-mounts-live-code-sync.md)

---

# 📙 Lesson 3.1 — Volumes: Making Data Survive

🎯 **Goal:** Persist data even when containers are destroyed.

### 📖 The Concept

Containers are **ephemeral** — delete one and its writable layer (all data written inside) vanishes. 💥 For databases, that's catastrophic. **Volumes** store data *outside* the container, managed by Docker.

### 💻 Hands-On

```bash
# Create a named volume
docker volume create pgdata

# Run Postgres with the volume mounted at its data directory
docker run -d \
  --name db \
  -e POSTGRES_PASSWORD=secret \
  -v pgdata:/var/lib/postgresql/data \
  postgres:16

# Destroy the container completely...
docker rm -f db

# ...run a NEW container with the same volume — data is still there! ✨
docker run -d --name db2 \
  -e POSTGRES_PASSWORD=secret \
  -v pgdata:/var/lib/postgresql/data \
  postgres:16
```

```bash
docker volume ls              # List volumes
docker volume inspect pgdata  # Where is it stored on disk?
docker volume rm pgdata       # Delete (only when no container uses it)
```

### 🔗 References
- 📄 [Volumes — Official Docs](https://docs.docker.com/engine/storage/volumes/)

### ⚡ Challenge
Create a MySQL container with a named volume, create a table in it, destroy the container, and prove the table survives in a new container.

---

[⬅️ Prev: Lesson 2.5](../module-2-images-and-dockerfiles/lesson-2-5-image-optimization-multi-stage-builds.md) · [🏠 Course Home](../README.md) · [Next: Lesson 3.2 ➡️](./lesson-3-2-bind-mounts-live-code-sync.md)
