# 01 — Endpoint & Identity Security (Intune, Entra ID, Defender for Endpoint)

> Covers roadmap Blocks 1–3. JD mapping: "Endpoint & Identity Security" bullet.

---

## PART A — BEGINNER: The foundations

### What is endpoint security?
An **endpoint** is any device that connects to the corporate network — laptops, desktops, phones, servers. Endpoint security = the controls that keep those devices trustworthy: encryption, patching, malware protection, configuration hardening, and the ability to detect/respond when something goes wrong.

### What is identity security?
Modern security assumes the network perimeter is gone (cloud, remote work). **Identity becomes the new perimeter** — who you are + what device you're on + how risky the sign-in looks decides what you can access. Microsoft Entra ID (formerly Azure AD) is the identity platform in the Microsoft world.

### The three tools of this file, in one line each
| Tool | What it is | One-line job |
|---|---|---|
| **Intune** | MDM/MAM platform | Manage & secure device configuration and apps |
| **Entra ID** | Cloud identity provider | Authenticate users, enforce access conditions |
| **Defender for Endpoint (MDE)** | EDR platform | Detect, investigate, respond to endpoint threats |

### How they connect (the picture to hold in your head)

```
   [User + Device] 
        |
        |  sign-in attempt
        v
+---------------------+     device compliance      +------------------+
|      ENTRA ID       | <------------------------- |      INTUNE      |
|  (authentication)   |        signal              |  (device mgmt)   |
+---------------------+                            +------------------+
        |                                                   |
        | Conditional Access decision                       | deploys sensor
        v                                                   v
   ALLOW / BLOCK /                                 +------------------+
   REQUIRE MFA /                                   |       MDE        |
   REQUIRE COMPLIANT DEVICE                        | (threat signals) |
                                                   +------------------+
                                                            |
                                                   risk signals feed back
                                                   into compliance & CA
```

The exam-grade sentence: **"Intune manages and attests device health, Entra ID makes access decisions using that attestation via Conditional Access, and MDE supplies threat and risk signals that feed both."**

---

## PART B — INTERMEDIATE: Intune in depth

### MDM vs MAM
| | MDM (device management) | MAM (app protection) |
|---|---|---|
| Scope | Whole device | Corporate data inside apps |
| Enrollment | Device enrolled | No enrollment needed |
| Typical use | Corporate-owned laptops | BYOD phones, contractors |
| Wipe | Full or selective | Selective only (corp data) |
| Example controls | Encryption, PIN, OS version, app deployment | Block copy/paste to personal apps, app-level PIN, encrypt app data |

**Interview answer pattern:** "Corporate devices get full MDM. BYOD gets MAM-only App Protection Policies so we protect data without touching personal content — that respects privacy AND reduces our management surface."

### Configuration profile vs compliance policy (THE classic question)
```
CONFIGURATION PROFILE                COMPLIANCE POLICY
"Make the device be X"               "Check whether the device is X"
     |                                       |
     v                                       v
 Enforces settings                   Evaluates & reports state
 (BitLocker on, password             (Is encryption on? OS version
  rules, Wi-Fi, certs)                >= minimum? Jailbroken?)
                                             |
                                             v
                                    COMPLIANT / NON-COMPLIANT
                                             |
                                             v
                                  Signal consumed by CONDITIONAL
                                  ACCESS -> gates access to M365
```

### Key Intune objects to know
- **Compliance policies** — per-platform rules; non-compliance actions (mark non-compliant immediately or grace period, notify user, retire device).
- **Configuration profiles** — settings catalog, templates (device restrictions, endpoint protection), custom (OMA-URI for Windows, .mobileconfig for macOS).
- **Proactive Remediations / Remediation scripts** — detection script + remediation script pairs, run on schedule. *You have real experience here — lead with it.*
- **Windows Autopilot / Apple ADE (DEP)** — zero-touch provisioning. Security angle: devices are corporate-trusted from first boot.
- **App deployment types** — required, available, uninstall; Win32 apps via .intunewin packaging.
- **Enrollment restrictions** — block personal devices, block unsupported OS versions.

### macOS specifics (differentiator territory)
- **FileVault** — full disk encryption; Intune can enforce + escrow recovery keys.
- **Gatekeeper** — blocks unsigned/unnotarized apps.
- **System Extensions / Kernel Extensions** — need admin approval; Intune profiles pre-approve them (this is how MDE's macOS sensor gets its permissions).
- **PPPC (Privacy Preferences Policy Control)** — grants apps access to disk/screen recording etc. without user prompts.
- **Platform SSO / SSO extension** — Entra sign-in integration on Mac.

### Advanced Intune topics
- **Graph API automation** — pull compliance reports, assign policies, automate evidence collection. (Your Proactive Remediation + Graph work = talk about it.)
- **Filters vs dynamic groups** — filters evaluate at check-in (faster) vs Entra dynamic group membership (slower, but reusable).
- **Compliance as code / baselines** — Security Baselines (Microsoft-published hardened defaults), CIS Benchmark alignment.
- **Co-management** — ConfigMgr + Intune workloads split (legacy estates).

---

## PART C — INTERMEDIATE: Entra ID, Conditional Access, Identity Protection

### Conditional Access mental model
```
        SIGNALS (IF...)                      CONTROLS (THEN...)
 +--------------------------+          +---------------------------+
 | User / group             |          | Block access              |
 | Cloud app targeted       |          | Grant + require MFA       |
 | Device platform          |  ---->   | Grant + compliant device  |
 | Device compliance state  |          | Grant + hybrid joined     |
 | Location (named/IP)      |          | Session: sign-in freq,    |
 | Sign-in risk (IP)        |          |  app-enforced restrictions|
 | User risk (IP)           |          +---------------------------+
 +--------------------------+
```

### The 5 baseline policies every mature org runs
1. **Require MFA for all users** (exclude break-glass accounts)
2. **Block legacy authentication** — POP/IMAP/basic SMTP bypass MFA entirely; classic attack path
3. **Require compliant device** for M365 access
4. **Require MFA (or phishing-resistant MFA) for admins**
5. **Geo-restrictions** — block/step-up from unexpected countries

### Operational maturity signals (say these!)
- **Report-only mode first** — measure impact before enforcing.
- **Break-glass accounts** — 2 cloud-only emergency admins, excluded from all CA, long random passwords, sign-in alerts on use.
- **Staged rollout** — pilot group → department → org.
- **Documented exclusions = risk exceptions** with owner + expiry.

### Identity Protection
| Concept | Sign-in risk | User risk |
|---|---|---|
| Question | Is THIS sign-in suspicious? | Is this ACCOUNT compromised? |
| Examples | Impossible travel, anonymous IP/Tor, password spray, unfamiliar properties | Leaked credentials found online, sustained anomalous behavior |
| Typical CA response | Medium+ → require MFA | High → require secure password change |
| Self-remediation | MFA success lowers risk | Password change lowers risk |

### Advanced identity topics
- **PIM (Privileged Identity Management)** — just-in-time role activation, approval workflows, time-boxed. Phrase: *"eliminate standing privilege."*
- **Access Reviews** — periodic recertification of group/role membership. This is audit evidence gold (maps to ISO A.5.18, PCI Req 7).
- **Phishing-resistant MFA** — FIDO2 keys, passkeys, Windows Hello for Business vs phishable push/OTP. Know **MFA fatigue attacks** (push bombing) and the fix (number matching).
- **Authentication methods policy**, SSPR, temporary access pass (TAP) for onboarding.
- **Hybrid identity** — Entra Connect sync, password hash sync vs pass-through auth vs federation (one line each).
- **Workload identities** — service principals & managed identities; audit for over-privileged app registrations, expiring secrets.
- Licensing: Identity Protection + PIM need **Entra ID P2**.

---

## PART D — INTERMEDIATE/ADVANCED: Defender for Endpoint

### What MDE is
EDR (Endpoint Detection & Response) + Threat & Vulnerability Management + Attack Surface Reduction + auto-investigation. Sensor is built into Windows 10/11; macOS/Linux deploy via Intune (system extension + PPPC + onboarding blob — you understand this pipeline).

### The investigation flow
```
ALERT fires
   |
   v
INCIDENT (correlated alerts, MITRE ATT&CK tags)
   |
   v
DEVICE TIMELINE  ---- what process spawned what (process tree)
   |                  network connections, file & registry writes
   v
SCOPE CHECK  -------- Advanced Hunting (KQL) across the fleet:
   |                  same hash? same IP? same command line elsewhere?
   v
RESPONSE ACTIONS ---- isolate device (network cut, MDE link stays)
   |                  collect investigation package, AV scan,
   |                  stop & quarantine file, add IoC block
   v
DOCUMENT & CLOSE ---- ticket, IoCs recorded, root cause, lessons
```

### Vocabulary you must own
- **IoC / IoA** — indicator of compromise (artifact) vs indicator of attack (behavior)
- **Process tree** — parent-child chain; malicious Word spawning PowerShell is the classic
- **LOLBins** — living-off-the-land binaries (powershell.exe, certutil, mshta abused by attackers)
- **ASR rules** — attack surface reduction (block Office spawning child processes, block credential stealing from LSASS)
- **Tamper protection** — prevents attackers disabling Defender
- **Lateral movement, persistence, C2 (command & control)**

### KQL starter kit (Advanced Hunting)
Main tables: `DeviceProcessEvents`, `DeviceNetworkEvents`, `DeviceLogonEvents`, `DeviceFileEvents`, `EmailEvents`, `IdentityLogonEvents`.

```kql
// Encoded PowerShell in the last 24h
DeviceProcessEvents
| where Timestamp > ago(24h)
| where FileName =~ "powershell.exe"
| where ProcessCommandLine has "-enc"
| project Timestamp, DeviceName, AccountName, InitiatingProcessFileName, ProcessCommandLine
| sort by Timestamp desc
```

```kql
// Which devices talked to a suspicious IP?
DeviceNetworkEvents
| where RemoteIP == "203.0.113.66"
| summarize count(), min(Timestamp), max(Timestamp) by DeviceName
```

```kql
// Failed logons by account (brute-force hunting)
DeviceLogonEvents
| where ActionType == "LogonFailed"
| summarize Failures = count() by AccountName, DeviceName
| where Failures > 10
| order by Failures desc
```

Operators to know: `where`, `project`, `summarize ... by`, `count()`, `ago()`, `has`/`contains`, `join`, `order by`.

### MDE Vulnerability Management
Exposure score, security recommendations, software inventory, CVE mapping per device. This is where "track open vulnerabilities to closure" (JD) meets tooling — export recommendations → assign owners → chase → verify.

---

## PART E — Interview questions with model answer skeletons

1. **"How does Intune compliance feed Conditional Access?"** → Compliance policy evaluates device → marks compliant/non-compliant in Entra → CA policy requires compliant device for M365 → non-compliant device is blocked or remediated. Mention grace periods and user notification flow.
2. **"A macOS device shows non-compliant. Triage?"** → Check which compliance setting failed (Intune portal → device → compliance details) → common causes: OS below minimum, FileVault off, stale check-in → verify device actually checked in recently → fix root cause or re-sync → confirm re-evaluation → if widespread, check for policy change (Intune audit logs).
3. **"MAM vs MDM — when?"** → (table above; answer with the BYOD/privacy framing.)
4. **"Walk me through investigating a suspicious PowerShell alert."** → (use the investigation flow diagram; end with documentation + prevention: ASR rule, IoC block.)
5. **"What is a break-glass account and why exclude it from CA?"** → Emergency access if CA misconfiguration or MFA outage locks admins out; controls: 2 accounts, long random creds, cloud-only, monitored sign-ins, excluded from all CA.
6. **"Sign-in risk vs user risk?"** → (table above; give one example each + the CA remediation pairing.)
7. **"How would you roll out a new CA policy safely?"** → Report-only → analyze sign-in log impact → pilot group → staged → document exclusions as time-boxed risk exceptions.

---

## Self-test checklist (all must be YES before leaving this file)
- [ ] I can draw the Intune ↔ Entra ↔ MDE triangle from memory
- [ ] I can explain compliance policy vs configuration profile in 2 sentences
- [ ] I can list 5 baseline CA policies and why legacy auth is blocked
- [ ] I can define sign-in risk vs user risk with examples
- [ ] I can narrate the MDE investigation flow end-to-end
- [ ] I can write a basic KQL query from memory
- [ ] I have 3 lines of my own Intune work restated as security controls
