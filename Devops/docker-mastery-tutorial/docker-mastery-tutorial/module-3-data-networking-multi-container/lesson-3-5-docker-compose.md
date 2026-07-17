---
title: "📙 Lesson 3.5 — Docker Compose: One File to Rule Them All"
category: Devops
tags: [Obsidian-Sync]
---
> 🐳 **Docker Mastery — From Zero to Hero** · 3️⃣ Module 3 — Data, Networking & Multi-Container Apps
>
> [⬅️ Prev: Lesson 3.4](./lesson-3-4-environment-variables-and-config.md) · [🏠 Course Home](../README.md) · [Next: Lesson 4.1 ➡️](../module-4-real-world-and-production/lesson-4-1-dockerizing-full-stack-app.md)

---

# 📙 Lesson 3.5 — Docker Compose: One File to Rule Them All

🎯 **Goal:** Define and launch a full multi-container stack with a single command.

### 📖 The Concept

Those long `docker run` commands from [Lesson 3.3](./lesson-3-3-docker-networking.md)? **Docker Compose** replaces them all with one declarative YAML file. Networks are created automatically, and services find each other by name.

### 💻 Hands-On

**`compose.yaml`**
```yaml
services:
  web:
    build: .                 # Build from local Dockerfile
    ports:
      - "3000:3000"
    environment:
      - DB_HOST=mongodb
    depends_on:
      - mongodb              # Start the DB first

  mongodb:
    image: mongo:7
    environment:
      - MONGO_INITDB_ROOT_USERNAME=admin
      - MONGO_INITDB_ROOT_PASSWORD=secret
    volumes:
      - mongo-data:/data/db  # Named volume for persistence

volumes:
  mongo-data:
```

```bash
docker compose up -d       # 🚀 Start EVERYTHING
docker compose ps          # Status of all services
docker compose logs -f web # Follow one service's logs
docker compose down        # Stop & remove containers (volumes survive)
docker compose down -v     # ...and delete volumes too ⚠️
docker compose up -d --build  # Rebuild after code changes
```

### 🎥 Deep-Dive Course (Compose Section Included)

[![Docker Tutorial for Beginners — freeCodeCamp](https://img.youtube.com/vi/fqMOX6JJhGo/0.jpg)](https://www.youtube.com/watch?v=fqMOX6JJhGo)

> ▶️ **[Docker Full DevOps Course (with Compose + hands-on labs) — freeCodeCamp](https://www.youtube.com/watch?v=fqMOX6JJhGo)**

### 🔗 References
- 📄 [Docker Compose — Official Docs](https://docs.docker.com/compose/)
- 📄 [Compose File Reference](https://docs.docker.com/reference/compose-file/)
- 🏆 [Awesome Compose — Sample Stacks for Everything](https://github.com/docker/awesome-compose)

### ⚡ Challenge
Rebuild [Lesson 3.3's](./lesson-3-3-docker-networking.md) MongoDB + Mongo Express setup as a `compose.yaml` and launch it with one command.


---

[⬅️ Prev: Lesson 3.4](./lesson-3-4-environment-variables-and-config.md) · [🏠 Course Home](../README.md) · [Next: Lesson 4.1 ➡️](../module-4-real-world-and-production/lesson-4-1-dockerizing-full-stack-app.md)
