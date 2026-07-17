---
title: 📗 Lesson 1.1 — What is Docker & Why Should You Care?
category: Devops
tags: [Obsidian-Sync]
---
> 🐳 **Docker Mastery — From Zero to Hero** · 1️⃣ Module 1 — Docker Foundations
>
> [🏠 Course Home](../README.md) · [Next: Lesson 1.2 ➡️](./lesson-1-2-containers-vs-virtual-machines.md)

---

# 📗 Lesson 1.1 — What is Docker & Why Should You Care?

🎯 **Goal:** Understand the problem Docker solves.

### 📖 The Concept

Docker is a **containerization platform**. It packages your application together with *everything it needs to run* — code, runtime, libraries, system tools, and configuration — into a single portable unit called a **container**.

**The pain before Docker:**
- 😫 App works on the developer's laptop, breaks on the server
- 😫 "Install Node 14, Postgres 12, Redis 6... oh wait, wrong versions"
- 😫 Two apps on one server need conflicting library versions
- 😫 Onboarding a new developer takes days of environment setup

**With Docker:**
- ✅ One command (`docker run`) starts the entire app with all dependencies
- ✅ Identical behavior on your laptop, a teammate's Mac, and a cloud server
- ✅ Isolated apps can't conflict with each other
- ✅ Onboarding = install Docker + run one command

### 🧠 Key Terms

| Term | Meaning |
|------|---------|
| **Image** | A read-only blueprint/template (like a class in programming) |
| **Container** | A running instance of an image (like an object) |
| **Docker Hub** | The public "app store" for images |
| **Docker Engine** | The background service that builds and runs containers |

### 🔗 References
- 📄 [Docker Overview — Official Docs](https://docs.docker.com/get-started/docker-overview/)
- 📄 [What is a Container? — Docker](https://www.docker.com/resources/what-container/)

### ⚡ Challenge
Explain Docker to a friend in one sentence without using the word "container."

---

[🏠 Course Home](../README.md) · [Next: Lesson 1.2 ➡️](./lesson-1-2-containers-vs-virtual-machines.md)
