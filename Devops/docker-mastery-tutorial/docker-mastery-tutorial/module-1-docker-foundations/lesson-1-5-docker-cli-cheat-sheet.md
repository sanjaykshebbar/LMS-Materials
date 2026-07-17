---
title: 📗 Lesson 1.5 — The Essential Docker CLI Cheat Sheet
category: Devops
tags: [Obsidian-Sync]
---
> 🐳 **Docker Mastery — From Zero to Hero** · 1️⃣ Module 1 — Docker Foundations
>
> [⬅️ Prev: Lesson 1.4](./lesson-1-4-your-first-container.md) · [🏠 Course Home](../README.md) · [Next: Lesson 2.1 ➡️](../module-2-images-and-dockerfiles/lesson-2-1-images-and-layers.md)

---

# 📗 Lesson 1.5 — The Essential Docker CLI Cheat Sheet

🎯 **Goal:** Memorize the 15 commands you'll use every single day.

### 💻 The Daily Drivers

```bash
# ── IMAGES ────────────────────────────────
docker pull ubuntu:22.04      # Download an image
docker images                 # List local images
docker rmi ubuntu:22.04       # Delete an image

# ── CONTAINERS ────────────────────────────
docker run -it ubuntu bash    # Run interactively with a shell
docker ps                     # Running containers
docker ps -a                  # ALL containers (incl. stopped)
docker stop <name>            # Graceful stop
docker start <name>           # Restart a stopped container
docker rm <name>              # Remove a container
docker rm -f <name>           # Force remove (running too)

# ── INSPECT & DEBUG ───────────────────────
docker logs -f <name>         # Follow live logs
docker exec -it <name> sh     # Shell into a container
docker inspect <name>         # Full JSON details
docker stats                  # Live CPU/RAM usage

# ── CLEANUP 🧹 ────────────────────────────
docker system prune -a        # Remove ALL unused images/containers
```

> ⚠️ **Careful:** `docker system prune -a` deletes everything not currently in use. Great for reclaiming disk space, dangerous if you wanted to keep those images.

### 🎥 Full Beginner Course (Bookmark This!)

[![Docker Tutorial for Beginners — TechWorld with Nana](https://img.youtube.com/vi/3c-iBn73dDE/0.jpg)](https://www.youtube.com/watch?v=3c-iBn73dDE)

> ▶️ **[Docker Tutorial for Beginners (Full 3-Hour Course) — TechWorld with Nana](https://www.youtube.com/watch?v=3c-iBn73dDE)**

### 🔗 References
- 📄 [Docker CLI Reference](https://docs.docker.com/reference/cli/docker/)

### ⚡ Challenge
Without looking: write the commands to (1) run Redis in the background, (2) view its logs, (3) shell into it, (4) remove it.


---

[⬅️ Prev: Lesson 1.4](./lesson-1-4-your-first-container.md) · [🏠 Course Home](../README.md) · [Next: Lesson 2.1 ➡️](../module-2-images-and-dockerfiles/lesson-2-1-images-and-layers.md)
