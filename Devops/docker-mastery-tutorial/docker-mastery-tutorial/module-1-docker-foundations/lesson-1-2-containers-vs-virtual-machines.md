> 🐳 **Docker Mastery — From Zero to Hero** · 1️⃣ Module 1 — Docker Foundations
>
> [⬅️ Prev: Lesson 1.1](./lesson-1-1-what-is-docker.md) · [🏠 Course Home](../README.md) · [Next: Lesson 1.3 ➡️](./lesson-1-3-installing-docker.md)

---

# 📗 Lesson 1.2 — Containers vs Virtual Machines

🎯 **Goal:** Know exactly why containers are faster and lighter than VMs.

### 📖 The Concept

```
┌─────────────────────────┐    ┌─────────────────────────┐
│      VIRTUAL MACHINE     │    │        CONTAINER         │
├─────────────────────────┤    ├─────────────────────────┤
│  App A   │   App B       │    │  App A   │   App B      │
│  Libs    │   Libs        │    │  Libs    │   Libs       │
│  Guest OS│   Guest OS    │    ├─────────────────────────┤
├─────────────────────────┤    │      Docker Engine       │
│       Hypervisor         │    ├─────────────────────────┤
├─────────────────────────┤    │        Host OS           │
│        Host OS           │    ├─────────────────────────┤
├─────────────────────────┤    │       Hardware           │
│       Hardware           │    └─────────────────────────┘
└─────────────────────────┘
```

The core difference: a **VM virtualizes hardware** and boots a full guest operating system (gigabytes, minutes to boot). A **container virtualizes only the application layer** and shares the host OS kernel (megabytes, starts in milliseconds).

| Feature | Virtual Machine 🖥️ | Container 🐳 |
|---------|-------------------|--------------|
| Size | GBs | MBs |
| Boot time | Minutes | Seconds/ms |
| OS | Full guest OS each | Shares host kernel |
| Isolation | Very strong (hardware level) | Strong (process level) |
| Density | Few per host | Hundreds per host |

> 💡 **They're not enemies!** In the cloud, containers usually run *inside* VMs — you get the best of both.

### 🔗 References
- 📄 [Containers vs VMs — Docker Blog](https://www.docker.com/blog/containers-vs-vms/)

### ⚡ Challenge
List two scenarios where you'd still choose a VM over a container.

---

[⬅️ Prev: Lesson 1.1](./lesson-1-1-what-is-docker.md) · [🏠 Course Home](../README.md) · [Next: Lesson 1.3 ➡️](./lesson-1-3-installing-docker.md)
