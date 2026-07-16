> 🐳 **Docker Mastery — From Zero to Hero** · 1️⃣ Module 1 — Docker Foundations
>
> [⬅️ Prev: Lesson 1.3](./lesson-1-3-installing-docker.md) · [🏠 Course Home](../README.md) · [Next: Lesson 1.5 ➡️](./lesson-1-5-docker-cli-cheat-sheet.md)

---

# 📗 Lesson 1.4 — Your First Container

🎯 **Goal:** Run, inspect, and stop real containers.

### 💻 Hands-On

```bash
# Run an Nginx web server, mapping port 8080 (your PC) → 80 (container)
docker run -d -p 8080:80 --name my-web nginx
```

Open **http://localhost:8080** — you're serving a website from a container! 🎉

**Breaking down the command:**

| Flag | Meaning |
|------|---------|
| `-d` | Detached mode (runs in background) |
| `-p 8080:80` | Map host port 8080 → container port 80 |
| `--name my-web` | Give the container a friendly name |
| `nginx` | The image to run (auto-pulled from Docker Hub) |

```bash
docker ps                  # See running containers
docker logs my-web         # View container output
docker exec -it my-web sh  # Get a shell INSIDE the container 🤯
docker stop my-web         # Stop it
docker rm my-web           # Remove it
```

> 💡 `docker exec -it <name> sh` is your #1 debugging tool — it drops you into a terminal *inside* the running container.

### 🎥 Watch & Code Along

[![Learn Docker in 7 Easy Steps — Fireship](https://img.youtube.com/vi/gAkwW2tuIqE/0.jpg)](https://www.youtube.com/watch?v=gAkwW2tuIqE)

> ▶️ **[Learn Docker in 7 Easy Steps — Fireship](https://www.youtube.com/watch?v=gAkwW2tuIqE)**

### ⚡ Challenge
Run two Nginx containers at the same time on ports 8080 and 8081, then stop and remove both.

---

[⬅️ Prev: Lesson 1.3](./lesson-1-3-installing-docker.md) · [🏠 Course Home](../README.md) · [Next: Lesson 1.5 ➡️](./lesson-1-5-docker-cli-cheat-sheet.md)
