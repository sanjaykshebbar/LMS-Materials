> 🐳 **Docker Mastery — From Zero to Hero** · 4️⃣ Module 4 — Real-World Docker & Production
>
> [⬅️ Prev: Lesson 4.2](./lesson-4-2-debugging-and-troubleshooting.md) · [🏠 Course Home](../README.md) · [Next: Lesson 4.4 ➡️](./lesson-4-4-docker-in-ci-cd.md)

---

# 📕 Lesson 4.3 — Docker Security Best Practices

🎯 **Goal:** Harden your images and containers against real attacks.

### 🛡️ The Security Checklist

**1️⃣ Don't run as root**
```dockerfile
FROM node:20-alpine
RUN addgroup -S app && adduser -S app -G app
USER app
```

**2️⃣ Pin versions & use minimal bases**
```dockerfile
FROM node:20.11-alpine   # ✅ pinned + small attack surface
FROM node:latest         # ❌ unpredictable + huge
```

**3️⃣ Scan images for vulnerabilities**
```bash
docker scout cves my-app:1.0     # Built into Docker
trivy image my-app:1.0           # Popular open-source scanner
```

**4️⃣ Never bake in secrets**
- ❌ `ENV API_KEY=sk-12345` in a Dockerfile — visible forever in layers
- ✅ Runtime env vars / Docker secrets / cloud secret managers

**5️⃣ Limit resources & drop privileges**
```bash
docker run --memory=512m --cpus=1 \
  --read-only \
  --cap-drop=ALL \
  my-app
```

**6️⃣ Only pull trusted images** — Official ✅ / Verified Publisher badges on Docker Hub

### 🔗 References
- 📄 [Docker Security — Official Docs](https://docs.docker.com/engine/security/)
- 📄 [Docker Scout](https://docs.docker.com/scout/)
- 📄 [Trivy Scanner](https://github.com/aquasecurity/trivy)
- 📄 [OWASP Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)

### ⚡ Challenge
Scan one of your images with `docker scout cves`, then fix at least one finding (usually by updating the base image) and re-scan.

---

[⬅️ Prev: Lesson 4.2](./lesson-4-2-debugging-and-troubleshooting.md) · [🏠 Course Home](../README.md) · [Next: Lesson 4.4 ➡️](./lesson-4-4-docker-in-ci-cd.md)
