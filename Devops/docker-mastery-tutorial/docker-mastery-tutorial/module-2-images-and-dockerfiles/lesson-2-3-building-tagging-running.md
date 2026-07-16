> 🐳 **Docker Mastery — From Zero to Hero** · 2️⃣ Module 2 — Images & Dockerfiles
>
> [⬅️ Prev: Lesson 2.2](./lesson-2-2-writing-your-first-dockerfile.md) · [🏠 Course Home](../README.md) · [Next: Lesson 2.4 ➡️](./lesson-2-4-docker-hub-and-registries.md)

---

# 📘 Lesson 2.3 — Building, Tagging & Running Your Image

🎯 **Goal:** Master the build → tag → run workflow.

### 💻 Hands-On

```bash
# Build an image from the Dockerfile in the current folder (.)
docker build -t my-app:1.0 .

# List it
docker images

# Run it!
docker run -d -p 3000:3000 --name app my-app:1.0
```

Visit **http://localhost:3000** 🎉

### 🏷️ Tagging Rules

```
  registry/username/repository:tag
  └──────┬──────┘ └────┬────┘ └┬┘
     (optional)      name    version
```

```bash
docker build -t my-app:1.0 .        # Version tag
docker build -t my-app:latest .     # "latest" tag (default)
docker tag my-app:1.0 my-app:stable # Add another tag to same image
```

> ⚠️ **`latest` is a lie!** It's just a default tag name — it does NOT automatically mean the newest version. In production, always pin exact versions like `node:20.11-alpine`, never `node:latest`.

### ⚡ Challenge
Build your [Lesson 2.2](./lesson-2-2-writing-your-first-dockerfile.md) app, change the message in `app.js`, rebuild as `my-app:2.0`, and run both versions side by side on different ports.

---

[⬅️ Prev: Lesson 2.2](./lesson-2-2-writing-your-first-dockerfile.md) · [🏠 Course Home](../README.md) · [Next: Lesson 2.4 ➡️](./lesson-2-4-docker-hub-and-registries.md)
