---
title: 📕 Lesson 4.2 — Debugging & Troubleshooting Like a Pro
category: Devops
tags: [Obsidian-Sync]
---
> 🐳 **Docker Mastery — From Zero to Hero** · 4️⃣ Module 4 — Real-World Docker & Production
>
> [⬅️ Prev: Lesson 4.1](./lesson-4-1-dockerizing-full-stack-app.md) · [🏠 Course Home](../README.md) · [Next: Lesson 4.3 ➡️](./lesson-4-3-docker-security-best-practices.md)

---

# 📕 Lesson 4.2 — Debugging & Troubleshooting Like a Pro

🎯 **Goal:** Diagnose any broken container in under 5 minutes.

### 🔍 The Debugging Playbook

**Step 1 — What's the state?**
```bash
docker ps -a          # Is it running, exited, restarting?
```

**Step 2 — What did it say before dying?**
```bash
docker logs --tail 100 <name>
docker logs -f <name>          # Follow live
```

**Step 3 — Why did it exit?**
```bash
docker inspect <name> --format '{{.State.ExitCode}}'
```

| Exit Code | Meaning |
|-----------|---------|
| `0` | Clean exit (maybe your CMD just finished?) |
| `1` | App error — check logs |
| `125` | Docker itself failed (bad flag/command) |
| `137` | Killed — usually **Out Of Memory** 💀 |
| `139` | Segfault |

**Step 4 — Go inside**
```bash
docker exec -it <name> sh      # Poke around a running container
docker run -it --entrypoint sh my-image   # Start a shell instead of the app
```

**Step 5 — Check resources & connectivity**
```bash
docker stats                                  # CPU/RAM live
docker exec -it <name> ping other-container  # DNS/network test
docker port <name>                            # Port mappings
```

### 🧨 Top 5 Beginner Errors & Fixes

| Error | Fix |
|-------|-----|
| `port is already allocated` | Another process uses that port — change the host port |
| Container exits instantly | Your CMD finished/crashed — check `docker logs` |
| `cannot connect to database` | Use the **container name** as host, not `localhost`! |
| Code changes not appearing | You forgot to rebuild: `docker compose up --build` |
| `permission denied` (Linux) | Add yourself to the docker group ([Lesson 1.3](../module-1-docker-foundations/lesson-1-3-installing-docker.md)) |

> 💡 The **#1 beginner mistake:** inside a container, `localhost` means *the container itself* — not your machine, not other containers. Use container/service names.

### ⚡ Challenge
Deliberately break a Compose stack (wrong DB hostname), then find and fix it using only `logs`, `inspect`, and `exec`.

---

[⬅️ Prev: Lesson 4.1](./lesson-4-1-dockerizing-full-stack-app.md) · [🏠 Course Home](../README.md) · [Next: Lesson 4.3 ➡️](./lesson-4-3-docker-security-best-practices.md)
