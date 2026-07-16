> 🐳 **Docker Mastery — From Zero to Hero** · 3️⃣ Module 3 — Data, Networking & Multi-Container Apps
>
> [⬅️ Prev: Lesson 3.3](./lesson-3-3-docker-networking.md) · [🏠 Course Home](../README.md) · [Next: Lesson 3.5 ➡️](./lesson-3-5-docker-compose.md)

---

# 📙 Lesson 3.4 — Environment Variables & Configuration

🎯 **Goal:** Configure the same image differently per environment — without rebuilding.

### 📖 The Golden Rule

> **Build once, configure everywhere.** The same image should run in dev, staging, and production — only the *configuration* changes.

### 💻 Hands-On

```bash
# Pass single variables
docker run -e NODE_ENV=production -e PORT=3000 my-app

# Pass a whole file of variables
docker run --env-file .env my-app
```

**`.env`**
```
NODE_ENV=production
DB_HOST=mongodb
DB_PASSWORD=supersecret
```

**Set defaults in the Dockerfile:**
```dockerfile
ENV NODE_ENV=production PORT=3000
```

### ⚠️ Security Musts

- 🚫 **Never** hardcode secrets in a Dockerfile — they're baked into image layers forever
- 🚫 **Never** commit `.env` files to Git — add to `.gitignore` AND `.dockerignore`
- ✅ In production, use **Docker secrets** or a vault service instead of env vars for sensitive values

### 🔗 References
- 📄 [Environment Variables — Docker Docs](https://docs.docker.com/reference/cli/docker/container/run/#env)
- 📄 [The Twelve-Factor App: Config](https://12factor.net/config)

### ⚡ Challenge
Make one app image print "Hello DEV" or "Hello PROD" depending on an env var — running the *same image* both ways.

---

[⬅️ Prev: Lesson 3.3](./lesson-3-3-docker-networking.md) · [🏠 Course Home](../README.md) · [Next: Lesson 3.5 ➡️](./lesson-3-5-docker-compose.md)
