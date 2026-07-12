# ⚡ Topic 01 — Endpoint & Identity Security (The Eyecatchy Version)

> Your home turf. One picture, three ideas, one reframing table, one checkpoint.

---

## 🔺 THE ONE PICTURE TO HOLD IN YOUR HEAD

```
                    ┌──────────────────────────┐
                    │   User + device sign-in  │
                    └────────────┬─────────────┘
                                 │
                                 ▼
                    ┌──────────────────────────┐
        ┌──────────►│        ENTRA ID          │◄──────────┐
        │           │ Conditional Access       │           │
        │           │ decision engine          │           │
        │           └────────────┬─────────────┘           │
        │                        │                         │
  Compliance                     │                    Risk signal
    signal                       │                         │
        │                        ▼                         │
┌───────┴────────┐   ┌───────────────────────┐   ┌─────────┴─────────┐
│     INTUNE     │   │    ACCESS DECISION    │   │  DEFENDER FOR     │
│ Manages &      │   │ Allow · Require MFA · │   │  ENDPOINT (MDE)   │
│ attests devices│   │ Compliant device ·    │   │ Detects &         │
│                │   │ Block                 │   │ investigates      │
└───────┬────────┘   └───────────────────────┘   └─────────▲─────────┘
        │                                                  │
        └────────── Intune deploys the MDE sensor ─────────┘
```

**🎯 THE MEMORIZE-THIS SENTENCE** (answers ~5 interview questions by itself):

> *"Intune manages and attests device health, Entra ID makes access decisions using that attestation via Conditional Access, and MDE supplies threat and risk signals that feed both."*

---

## 💡 THE THREE IDEAS INTERVIEWERS ACTUALLY TEST

### 1️⃣ Configuration profile vs compliance policy — the classic trap

| | Configuration profile | Compliance policy |
|---|---|---|
| Verb | **ENFORCES** | **EVALUATES** |
| Job | *Makes* the device be X | *Checks* whether the device is X |
| Example | Turn BitLocker on, set password rules | Is encryption on? OS ≥ minimum? |
| Output | Settings applied | ✅ Compliant / ❌ Non-compliant |

**The magic:** the compliant/non-compliant stamp travels to Entra ID, where Conditional Access uses it as a gate — *"no compliant device, no M365."*

🗣️ Say the two verbs — **enforce vs evaluate** — and you've won the question.

### 2️⃣ MDM vs MAM — the BYOD question

| | MDM | MAM |
|---|---|---|
| Scope | Whole device | Corp data **inside apps** |
| Wipe | Full or selective | Selective only (personal photos survive) |
| Best for | Corporate laptops | BYOD phones, contractors |
| Controls | Encryption, PIN, OS version | Block copy/paste to personal apps, app PIN |

🗣️ Answer pattern: *"Corporate devices get full MDM. BYOD gets MAM-only — we protect the data without invading privacy or expanding our management surface."*

### 3️⃣ Your secret weapon — macOS depth 🍎

Most candidates are Windows-only. You've debugged Mac deployments at **script level**. Keep these four loaded:

| Term | What it does | Why it impresses |
|---|---|---|
| **FileVault** | Disk encryption + recovery key escrow via Intune | Encryption control, not just a setting |
| **Gatekeeper** | Blocks unsigned/unnotarized apps | Attack surface reduction |
| **System Extensions** | Approval profiles — *this is how the MDE sensor installs on Mac* | Connect the dots aloud = depth |
| **PPPC profiles** | Pre-grant app privacy permissions | Dropping "PPPC" naturally = instant credibility spike ⚡ |

---

## 🔄 THE REFRAMING TABLE — same work, security vocabulary

| ❌ You say now | ✅ Say instead |
|---|---|
| "I enforce BitLocker/FileVault" | "Data-at-rest **encryption control** — ISO A.8.24" |
| "I deploy patches" | "**Vulnerability remediation** within SLA" |
| "I built remediation scripts" | "**Automated compliance checking** at fleet scale" |
| "I restrict app installs" | "**Attack surface reduction**" |

Same facts. Different frame. Helpdesk vocabulary → L2 analyst vocabulary.

---

## ✅ CHECKPOINT — answer OUT LOUD before moving to Topic 02

1. How does Intune compliance feed Conditional Access?
2. When would you choose MAM over MDM?
3. A macOS device shows non-compliant — first three things you check?

*(Stuck on #3? → Which compliance setting failed in the Intune portal → last check-in time (stale device?) → recent policy changes in Intune audit logs.)*

---

⏭️ **Next: Topic 02 — Email Security.** Your biggest gap, best diagrams, and the topic most likely to be probed deep.
