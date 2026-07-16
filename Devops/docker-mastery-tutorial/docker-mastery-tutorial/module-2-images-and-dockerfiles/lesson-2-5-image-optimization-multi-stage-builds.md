> 🐳 **Docker Mastery — From Zero to Hero** · 2️⃣ Module 2 — Images & Dockerfiles
>
> [⬅️ Prev: Lesson 2.4](./lesson-2-4-docker-hub-and-registries.md) · [🏠 Course Home](../README.md) · [Next: Lesson 3.1 ➡️](../module-3-data-networking-multi-container/lesson-3-1-volumes-persistent-data.md)

---

# 📘 Lesson 2.5 — Image Optimization & Multi-Stage Builds

🎯 **Goal:** Shrink a 1 GB image to 50 MB like a pro.

### 📖 The Concept

Big images = slow deploys, more attack surface, higher costs. Four weapons to fight bloat:

**1️⃣ Use slim base images**
```dockerfile
FROM node:20          # ~1.1 GB 😱
FROM node:20-slim     # ~200 MB 🙂
FROM node:20-alpine   # ~130 MB 😍
```

**2️⃣ Order layers for caching** — put rarely-changing steps first:
```dockerfile
COPY package*.json ./   # Changes rarely → cached
RUN npm install         # Only re-runs if package.json changed
COPY . .                # Changes often → last
```

**3️⃣ Use `.dockerignore`**
```
node_modules
.git
*.log
.env
```

**4️⃣ Multi-stage builds** — build with heavy tools, ship only the result:
```dockerfile
# ── Stage 1: BUILD (has compilers, dev deps) ──
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# ── Stage 2: RUNTIME (tiny, production-only) ──
FROM node:20-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
CMD ["node", "dist/index.js"]
```

The final image contains **only Stage 2** — all the build tooling is thrown away. For compiled languages (Go, Rust), final images can shrink below **20 MB**.

### 🎥 Level-Up Video

[![100+ Docker Concepts You Need to Know — Fireship](https://img.youtube.com/vi/rIrNIzy6U_g/0.jpg)](https://www.youtube.com/watch?v=rIrNIzy6U_g)

> ▶️ **[100+ Docker Concepts You Need to Know — Fireship](https://www.youtube.com/watch?v=rIrNIzy6U_g)**

### 🔗 References
- 📄 [Multi-Stage Builds — Official Docs](https://docs.docker.com/build/building/multi-stage/)

### ⚡ Challenge
Take any Dockerfile and reduce the final image size by at least 50% using the techniques above. Compare with `docker images`.


---

[⬅️ Prev: Lesson 2.4](./lesson-2-4-docker-hub-and-registries.md) · [🏠 Course Home](../README.md) · [Next: Lesson 3.1 ➡️](../module-3-data-networking-multi-container/lesson-3-1-volumes-persistent-data.md)
