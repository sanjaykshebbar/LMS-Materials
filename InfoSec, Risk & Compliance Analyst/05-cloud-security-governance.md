# 05 — Cloud Security Governance: AWS, Azure, CSPM, IAM Auditing

> Covers roadmap Block 9. JD mapping: "Cloud Security Governance" bullet — govern, enforce best practices, monitor posture (CSPM), audit IAM, secure storage.

---

## PART A — BEGINNER: Cloud security fundamentals

### The Shared Responsibility Model (non-negotiable knowledge)
```
+--------------------------------------------------------------+
| CUSTOMER: "security IN the cloud"                            |
|  data | identities & access | app config | network rules |   |
|  OS patching (IaaS) | encryption choices                     |
+--------------------------------------------------------------+
| PROVIDER: "security OF the cloud"                            |
|  physical DCs | hardware | hypervisor | managed-service infra|
+--------------------------------------------------------------+

The split shifts with service model:
IaaS  (VMs)        -> customer owns most (OS up)
PaaS  (App Service)-> provider owns OS; customer owns app+data+config
SaaS  (M365)       -> customer owns data, identities, and configuration
```
**The stat that frames every answer:** the overwhelming majority of cloud breaches come from **customer misconfiguration** (public buckets, exposed keys, permissive IAM) — not provider compromise. That's why *governance* is the job.

### CSPM — Cloud Security Posture Management
Continuously scans cloud configuration against benchmarks (CIS AWS/Azure Foundations) and flags misconfigurations:
- Public storage buckets/containers
- Security groups open to 0.0.0.0/0 (especially SSH/RDP)
- Unencrypted storage/databases
- Root/global-admin without MFA
- Over-privileged identities, stale keys

Products: **Microsoft Defender for Cloud** (multi-cloud: Azure + AWS + GCP), AWS Security Hub, Wiz / Prisma Cloud / Orca (name-drop tier). CNAPP = CSPM + workload protection + IAM analysis converged (buzzword awareness).

---

## PART B — INTERMEDIATE: AWS security essentials

### IAM
- **Users** (avoid for humans — federate instead), **Groups**, **Roles** (assumable, temporary creds — the right pattern), **Policies** (JSON allow/deny documents).
- **Root account**: MFA mandatory, no access keys, never used day-to-day — break-glass only. (Parallel to Entra break-glass — draw that comparison aloud.)
- Least privilege: no `"Action": "*"` / `"Resource": "*"`; use IAM Access Analyzer to find external exposure & unused permissions.

### S3 security (the famous breach class)
```
Defense layers for a bucket:
1. Block Public Access (account-level ON by default — verify, don't assume)
2. Bucket policies / no public ACLs
3. Default encryption (SSE-S3 or SSE-KMS)
4. Versioning + MFA delete for critical data
5. Access logging -> audit trail
```

### The services table
| Service | Job | Interview one-liner |
|---|---|---|
| **CloudTrail** | API audit log | "The evidence source — who did what, when, from where" |
| **GuardDuty** | Threat detection | ML on CloudTrail/VPC/DNS logs |
| **AWS Config** | Config compliance | Rules + timeline of resource changes |
| **Security Hub** | Findings aggregator / CSPM | CIS benchmark scores |
| **KMS** | Key management | Envelope encryption, key policies |
| **Security Groups vs NACLs** | Instance vs subnet firewall | SG = stateful; NACL = stateless |
| **SCPs** | Org-wide guardrails | "Preventive control at the org level — e.g., deny disabling CloudTrail" |

---

## PART C — INTERMEDIATE: Azure security essentials (your home ecosystem)

### Identity & access
- **Entra ID** is the identity plane (you know it — say so).
- **RBAC scopes**: Management group → Subscription → Resource group → Resource. Assign at the narrowest scope.
- **PIM** for just-in-time Azure roles (same story as directory roles).

### The services table
| Service | Job |
|---|---|
| **Microsoft Defender for Cloud** | CSPM + workload protection; **Secure Score** = quantified posture (drop this term) |
| **Azure Policy** | Preventive guardrails — audit/deny/deployIfNotExists (e.g., "deny public storage accounts", "require encryption") |
| **NSGs** | Subnet/NIC firewall rules |
| **Azure Firewall** | Managed NGFW for hub-spoke networks |
| **Key Vault** | Secrets/keys/certs; RBAC + access policies; purge protection |
| **Activity Log / Log Analytics** | Control-plane audit trail + query workspace |
| **Microsoft Sentinel** | Cloud SIEM/SOAR — **uses KQL** (same language as MDE hunting — one skill, two tools!) |

### Storage account security checklist
Disable public blob access → require private endpoints/firewall rules → enforce TLS 1.2+ → encryption (platform or CMK) → SAS tokens time-boxed & scoped → diagnostic logging on.

---

## PART D — ADVANCED: Governance patterns & IAM auditing

### The governance loop (say this structure in interviews)
```
PREVENT                DETECT               RESPOND              EVIDENCE
Azure Policy / SCPs -> CSPM findings,    -> ticket w/ owner   -> CloudTrail /
guardrails, IaC        GuardDuty/          + SLA, remediate,     Activity Log
scanning               Defender alerts     verify fix            exports, Config
                                                                 history -> auditors
```

### How to audit IAM (memorize as a checklist)
```
1. Privileged inventory      who has admin/owner? is each justified?
2. MFA coverage              privileged first, then all; root/GA especially
3. Stale credentials         keys/users unused 90+ days -> disable
4. Wildcard policies         "*" actions/resources -> tighten
5. Standing vs JIT access    PIM / assume-role instead of permanent rights
6. Service principals        app registrations: owners, secret expiry, permissions
7. Access reviews            recertification cadence + completion records
8. Separation of duties      no single identity requests AND approves
```

### Multi-cloud governance answer
"Single pane where possible (Defender for Cloud covers AWS too), common control framework mapped to CIS benchmarks per cloud, IaC scanning (Terraform/Bicep) so misconfigurations are caught pre-deployment (shift-left), and drift detection after."

### Advanced name-drops (one line each)
- **IMDSv2** — instance metadata hardening (SSRF credential theft mitigation).
- **Confused deputy / cross-account role abuse** — external ID on assume-role.
- **CIEM** — cloud infrastructure entitlement management (IAM right-sizing at scale).
- **Landing zones** — pre-governed subscription/account vending.

---

## PART E — Scenario walkthrough (rehearse aloud)

**"CSPM flags a publicly accessible storage bucket with customer data. Go."**
```
1. VALIDATE   is it truly public? what data class is inside? (regulated? CHD/PII?)
2. CONTAIN    enable Block Public Access / disable public blob access NOW
              (containment beats root-cause order here)
3. ASSESS     access logs: was it READ by external IPs? since when?
              if yes -> incident process, possible breach notification path
4. ROOT CAUSE who created it, via what (console? IaC? script?), why
5. PREVENT    Azure Policy/SCP deny-public-storage; IaC pipeline check
6. DOCUMENT   finding -> owner -> closure evidence; lessons learned
```

---

## PART F — Interview questions
1. **Shared responsibility with an example.** (IaaS vs SaaS contrast)
2. **What is CSPM and what does it catch?** (benchmark drift; top misconfigs list)
3. **How do you audit IAM?** (8-point checklist)
4. **What's CloudTrail and why do auditors care?** (immutable API history = evidence)
5. **Azure Policy vs RBAC?** (what you CAN do vs what resources MUST look like — complementary)
6. **Prevent developers from creating public buckets — how?** (SCP/Azure Policy deny + IaC scanning + CSPM detection as backstop — prevent/detect layering)
7. **What is Secure Score?** (Defender for Cloud posture metric; trend it in reporting)

## Self-test checklist
- [ ] Shared responsibility across IaaS/PaaS/SaaS from memory
- [ ] 8-point IAM audit checklist
- [ ] Public bucket scenario in the 6-step order (contain before root-cause)
- [ ] 5 AWS + 5 Azure security services with one-liners
- [ ] Prevent → Detect → Respond → Evidence loop articulated
