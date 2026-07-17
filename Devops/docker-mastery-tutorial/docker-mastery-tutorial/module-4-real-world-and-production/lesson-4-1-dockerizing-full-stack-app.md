---
title: 📕 Lesson 4.1 — Dockerizing a Real Full-Stack Application
category: Devops
tags: [Obsidian-Sync]
---
> 🐳 **Docker Mastery — From Zero to Hero** · 4️⃣ Module 4 — Real-World Docker & Production
>
> [⬅️ Prev: Lesson 3.5](../module-3-data-networking-multi-container/lesson-3-5-docker-compose.md) · [🏠 Course Home](../README.md) · [Next: Lesson 4.2 ➡️](./lesson-4-2-debugging-and-troubleshooting.md)

---

# 📕 Lesson 4.1 — Dockerizing a Real Full-Stack Application

🎯 **Goal:** Containerize a complete frontend + backend + database + cache stack.

### 💻 The Production-Style Compose Stack

```yaml
services:
  frontend:
    build: ./frontend
    ports:
      - "80:80"
    depends_on:
      - backend

  backend:
    build: ./backend
    environment:
      - DATABASE_URL=postgresql://app:secret@db:5432/appdb
      - REDIS_URL=redis://cache:6379
    depends_on:
      db:
        condition: service_healthy   # Wait until DB is truly ready

  db:
    image: postgres:16-alpine
    environment:
      - POSTGRES_USER=app
      - POSTGRES_PASSWORD=secret
      - POSTGRES_DB=appdb
    volumes:
      - db-data:/var/lib/postgresql/data
    healthcheck:                      # Compose can wait on this
      test: ["CMD-SHELL", "pg_isready -U app"]
      interval: 5s
      retries: 5

  cache:
    image: redis:7-alpine

volumes:
  db-data:
```

### 🧠 Real-World Patterns Used Here

- ✅ **Healthchecks** — `depends_on: condition: service_healthy` prevents the classic "backend crashes because DB isn't ready yet" bug
- ✅ **One process per container** — frontend, backend, DB, cache all separate
- ✅ **Internal-only services** — DB and cache have **no `ports:`** — they're reachable only inside the Compose network 🔒
- ✅ **Named volumes** for anything stateful

### 🔗 References
- 📄 [Compose Healthchecks](https://docs.docker.com/reference/compose-file/services/#healthcheck)
- 🏆 [Awesome Compose sample apps](https://github.com/docker/awesome-compose)

### ⚡ Challenge
Pick any tutorial project you've built before (any language) and fully dockerize it with Compose, including a database with a healthcheck.

---

[⬅️ Prev: Lesson 3.5](../module-3-data-networking-multi-container/lesson-3-5-docker-compose.md) · [🏠 Course Home](../README.md) · [Next: Lesson 4.2 ➡️](./lesson-4-2-debugging-and-troubleshooting.md)
