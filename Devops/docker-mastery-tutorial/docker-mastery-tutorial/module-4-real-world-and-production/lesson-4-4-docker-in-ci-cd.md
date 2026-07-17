---
title: "📕 Lesson 4.4 — Docker in CI/CD: Automate Everything"
category: Devops
tags: [Obsidian-Sync]
---
> 🐳 **Docker Mastery — From Zero to Hero** · 4️⃣ Module 4 — Real-World Docker & Production
>
> [⬅️ Prev: Lesson 4.3](./lesson-4-3-docker-security-best-practices.md) · [🏠 Course Home](../README.md) · [Next: Lesson 4.5 ➡️](./lesson-4-5-orchestration-and-next-steps.md)

---

# 📕 Lesson 4.4 — Docker in CI/CD: Automate Everything

🎯 **Goal:** Automatically build, test, and publish images on every git push.

### 📖 The Concept

Docker + CI/CD is a match made in heaven: your pipeline builds an image **once**, tests that exact image, and ships that exact image to production. No more "but it passed in CI!"

### 💻 GitHub Actions Example

**`.github/workflows/docker.yml`**
```yaml
name: Build & Push Docker Image

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Log in to Docker Hub
        uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}

      - name: Build and push
        uses: docker/build-push-action@v6
        with:
          context: .
          push: true
          tags: |
            yourusername/my-app:latest
            yourusername/my-app:${{ github.sha }}
```

### 🧠 CI/CD Golden Rules

- 🏷️ **Tag with the git SHA** — every image traceable to an exact commit
- 🧪 **Test the image itself** — run your test suite *inside* the built image
- 🚀 **Deploy the tested artifact** — the same image goes from CI → staging → prod
- 🔐 **Registry credentials live in CI secrets**, never in the repo

### 🔗 References
- 📄 [docker/build-push-action](https://github.com/docker/build-push-action)
- 📄 [Docker + GitHub Actions Guide](https://docs.docker.com/build/ci/github-actions/)

### ⚡ Challenge
Set up a GitHub Actions workflow that builds your [Module 2](../module-2-images-and-dockerfiles/lesson-2-1-images-and-layers.md) app and pushes it to Docker Hub on every push to `main`.

---

[⬅️ Prev: Lesson 4.3](./lesson-4-3-docker-security-best-practices.md) · [🏠 Course Home](../README.md) · [Next: Lesson 4.5 ➡️](./lesson-4-5-orchestration-and-next-steps.md)
