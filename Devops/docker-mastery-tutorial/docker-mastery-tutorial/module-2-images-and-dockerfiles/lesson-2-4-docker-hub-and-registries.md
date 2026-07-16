> 🐳 **Docker Mastery — From Zero to Hero** · 2️⃣ Module 2 — Images & Dockerfiles
>
> [⬅️ Prev: Lesson 2.3](./lesson-2-3-building-tagging-running.md) · [🏠 Course Home](../README.md) · [Next: Lesson 2.5 ➡️](./lesson-2-5-image-optimization-multi-stage-builds.md)

---

# 📘 Lesson 2.4 — Docker Hub & Registries: Share Your Images

🎯 **Goal:** Push your image to the world (or a private registry).

### 💻 Hands-On

```bash
# 1. Create a free account at hub.docker.com, then:
docker login

# 2. Tag your image with your username
docker tag my-app:1.0 yourusername/my-app:1.0

# 3. Push it! 🚀
docker push yourusername/my-app:1.0

# 4. Anyone, anywhere can now run:
docker run -d -p 3000:3000 yourusername/my-app:1.0
```

### 🏢 Registry Options

| Registry | Best For |
|----------|----------|
| **Docker Hub** | Public images, getting started |
| **GitHub Container Registry (GHCR)** | Projects already on GitHub |
| **AWS ECR / Azure ACR / Google AR** | Cloud production deployments |
| **Harbor / self-hosted** | Enterprise on-prem needs |

> 💡 **Pro tip:** Look for the ✅ **"Docker Official Image"** and **"Verified Publisher"** badges on Docker Hub — random unverified images can contain malware.

### 🔗 References
- 📄 [Docker Hub](https://hub.docker.com/)
- 📄 [Docker Hub Quickstart](https://docs.docker.com/docker-hub/)

### ⚡ Challenge
Push your `my-app` image to Docker Hub, then delete it locally (`docker rmi`) and pull it back down.

---

[⬅️ Prev: Lesson 2.3](./lesson-2-3-building-tagging-running.md) · [🏠 Course Home](../README.md) · [Next: Lesson 2.5 ➡️](./lesson-2-5-image-optimization-multi-stage-builds.md)
