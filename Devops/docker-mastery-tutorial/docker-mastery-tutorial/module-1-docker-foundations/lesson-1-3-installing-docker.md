> 🐳 **Docker Mastery — From Zero to Hero** · 1️⃣ Module 1 — Docker Foundations
>
> [⬅️ Prev: Lesson 1.2](./lesson-1-2-containers-vs-virtual-machines.md) · [🏠 Course Home](../README.md) · [Next: Lesson 1.4 ➡️](./lesson-1-4-your-first-container.md)

---

# 📗 Lesson 1.3 — Installing Docker on Any OS

🎯 **Goal:** Get Docker running on your machine.

### 💻 Installation

**🪟 Windows / 🍎 macOS — Docker Desktop**
1. Download **Docker Desktop** from the official site
2. Install and launch it (Windows needs WSL 2 enabled)
3. Verify in a terminal:

```bash
docker --version
docker run hello-world
```

**🐧 Linux (Ubuntu/Debian) — Docker Engine**

```bash
# Official convenience script
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Run docker without sudo (log out & back in after)
sudo usermod -aG docker $USER

# Verify
docker run hello-world
```

If you see **"Hello from Docker!"** — congratulations, your setup works end-to-end! 🎉

### 🔗 References
- 📄 [Install Docker Desktop](https://docs.docker.com/desktop/)
- 📄 [Install Docker Engine on Linux](https://docs.docker.com/engine/install/)
- 🧪 [Play with Docker — free browser playground, no install needed](https://labs.play-with-docker.com/)

### ⚡ Challenge
Run `docker info` and find: how many containers exist on your machine, and what storage driver is in use.

---

[⬅️ Prev: Lesson 1.2](./lesson-1-2-containers-vs-virtual-machines.md) · [🏠 Course Home](../README.md) · [Next: Lesson 1.4 ➡️](./lesson-1-4-your-first-container.md)
