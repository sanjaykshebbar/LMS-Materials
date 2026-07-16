> 🐳 **Docker Mastery — From Zero to Hero** · 2️⃣ Module 2 — Images & Dockerfiles
>
> [⬅️ Prev: Lesson 1.5](../module-1-docker-foundations/lesson-1-5-docker-cli-cheat-sheet.md) · [🏠 Course Home](../README.md) · [Next: Lesson 2.2 ➡️](./lesson-2-2-writing-your-first-dockerfile.md)

---

# 📘 Lesson 2.1 — Understanding Images & Layers

🎯 **Goal:** Learn how images are built from stacked, cached layers.

### 📖 The Concept

A Docker image is not one big file — it's a **stack of read-only layers**. Each instruction in a Dockerfile creates a new layer:

```
┌───────────────────────────┐
│  Layer 4: COPY app code   │  ← changes often (top)
├───────────────────────────┤
│  Layer 3: RUN npm install │
├───────────────────────────┤
│  Layer 2: COPY package.json│
├───────────────────────────┤
│  Layer 1: FROM node:20    │  ← rarely changes (bottom)
└───────────────────────────┘
```

**Why layers matter:**
- 🚀 **Caching** — unchanged layers are reused, so rebuilds are fast
- 💾 **Sharing** — 10 images based on `node:20` share that base layer once on disk
- 📦 **Small pushes** — only changed layers upload to registries

When a container runs, Docker adds one thin **writable layer** on top. Delete the container → that layer is gone (this is why we need volumes — [Module 3](../module-3-data-networking-multi-container/lesson-3-1-volumes-persistent-data.md)!).

```bash
docker history nginx    # See every layer of an image
```

### 🔗 References
- 📄 [Docker Image Layers Explained](https://docs.docker.com/get-started/docker-concepts/building-images/understanding-image-layers/)

### ⚡ Challenge
Run `docker history python:3.12` and count the layers. Which one is the largest?

---

[⬅️ Prev: Lesson 1.5](../module-1-docker-foundations/lesson-1-5-docker-cli-cheat-sheet.md) · [🏠 Course Home](../README.md) · [Next: Lesson 2.2 ➡️](./lesson-2-2-writing-your-first-dockerfile.md)
