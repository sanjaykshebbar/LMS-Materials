---
title: "03 — GRC: Risk, ISO 27001, PCI-DSS, NIST, CIS, SOC"
category: "InfoSec, Risk & Compliance Analyst"
tags: [Obsidian-Sync]
---
# 03 — GRC: Risk, ISO 27001, PCI-DSS, NIST, CIS, SOC

> Covers roadmap Block 5 — the "mindset" half of the job title. JD mapping: "GRC Alignment & Audit Support", "R&C Business Support", "Action Item Tracking".

---

## PART A — BEGINNER: The language of risk

### Core definitions (memorize cold)
| Term | Definition | Example |
|---|---|---|
| **Asset** | Anything of value | Customer card data, laptop, source code |
| **Threat** | Potential cause of harm | Phishing actor, insider, ransomware |
| **Vulnerability** | Weakness a threat can exploit | Unpatched server, weak password policy |
| **Risk** | Likelihood × Impact of threat exploiting vulnerability | "High likelihood phishing × high impact of account takeover" |
| **Control** | Measure that reduces risk | MFA, encryption, training |
| **Residual risk** | Risk remaining AFTER controls | Even with MFA, some takeover risk remains |
| **Inherent risk** | Risk BEFORE controls | |
| **Risk appetite** | How much risk leadership accepts | |

### The 4 risk treatment options (guaranteed question)
```
                    +----------- MITIGATE (apply controls)
                    |
   RISK  -----------+----------- TRANSFER (insurance, contract to vendor)
 identified         |
                    +----------- AVOID (stop the risky activity)
                    |
                    +----------- ACCEPT (documented, owner-approved, time-bound)
```

### Control taxonomy
- **By function:** Preventive (MFA, firewall) / Detective (SIEM alerts, audits) / Corrective (restore from backup, patching)
- **By type:** Technical / Administrative (policy, training) / Physical (badges, locks)
- **Compensating control:** alternative control when the primary one can't be applied (e.g., can't patch → network isolation + enhanced monitoring)

### The risk exception lifecycle (the JD says you'll OWN this — drill it)
```
REQUEST                 "Sales needs Dropbox unblocked"
   |
ASSESS                  business justification + risk analysis
   |                    (what data? what exposure? likelihood/impact?)
   v
COMPENSATE              can we reduce risk? (scoped users, DLP monitoring,
   |                     sanctioned alternative offered first)
   v
APPROVE                 RISK OWNER signs off (the BUSINESS owns risk;
   |                     security ADVISES — never security's lone call)
   v
REGISTER                logged in risk register with expiry date (30/90 days)
   |
   v
REVIEW at expiry        renew with re-justification, or close & re-block
```
**Never**: open-ended exceptions, verbal approvals, security accepting risk on the business's behalf.

---

## PART B — INTERMEDIATE: ISO/IEC 27001

### What it is
The international standard for an **ISMS — Information Security Management System**. Certifiable. It is a *management system* (how you run security: risk assessment, leadership, improvement), not a control checklist. Built on **Plan–Do–Check–Act**.

### Structure
```
CLAUSES 4–10 (the mandatory management system)
  4 Context of the organization      7 Support (resources, awareness, docs)
  5 Leadership & commitment          8 Operation (run the risk process)
  6 Planning (risk assessment,       9 Performance evaluation (audit, mgmt review)
    risk treatment, objectives)     10 Improvement (nonconformities, CAPA)

ANNEX A (2022) — 93 controls in 4 themes:
  Organizational (37) | People (8) | Physical (14) | Technological (34)
```

### Key documents & terms
- **SoA — Statement of Applicability**: declares which Annex A controls apply, justification, implementation status. Auditors live in this document. Fluency test word.
- **Risk register, risk treatment plan, ISMS scope statement.**
- **Certification cycle:** Stage 1 audit (documentation) → Stage 2 (implementation evidence) → certificate valid 3 years with **annual surveillance audits** → recertification.
- **Internal audit** (required by clause 9.2) vs **external/certification audit**.
- **Nonconformity** (major/minor) → corrective action plan (CAPA).

### Annex A controls YOU can map your real work to (interview ammo)
| Control | Your evidence |
|---|---|
| A.5.15 / A.5.18 Access control & access rights | Intern→FTE access SOP gap analysis; access reviews |
| A.8.8 Management of technical vulnerabilities | Patch management evaluation, remediation tracking |
| A.8.9 Configuration management | Intune baselines & compliance policies |
| A.8.24 Use of cryptography | BitLocker/FileVault enforcement |
| A.8.7 Protection against malware | MDE deployment across fleet |
| A.6.3 Awareness training | Phishing simulations, onboarding security briefings |
| A.5.19–5.22 Supplier relationships | Vendor security questionnaire work |

---

## PART C — INTERMEDIATE: PCI-DSS (you're in fintech — expect depth here)

### Basics
- Applies to any org that **stores, processes, or transmits cardholder data (CHD)**. Contractual (card brands via acquirers), not law — but breaches trigger fines + loss of processing rights.
- Current version: **4.0 / 4.0.1** (v3.2.1 retired March 2024; future-dated 4.0 requirements became mandatory March 2025).
- **CHD** = PAN (+ name, expiry, service code when stored with PAN). **SAD** (sensitive auth data: CVV, full track, PIN block) — **never storable after authorization**, even encrypted.

### The 12 requirements by theme
```
Build & maintain secure network      1. Network security controls (firewalls)
                                     2. Secure configurations (no defaults)
Protect account data                 3. Protect stored CHD (encryption, retention)
                                     4. Encrypt CHD in transit over public nets
Vulnerability management             5. Anti-malware
                                     6. Secure systems & software (patching, SDLC)
Access control                       7. Need-to-know access restriction
                                     8. Identify users & authenticate (MFA!)
                                     9. Physical access restriction
Monitor & test                      10. Log & monitor all access
                                    11. Test security (scans, pen tests, FIM)
Policy                              12. Security policy & program
```

### Scoping — the concept interviewers probe
- **CDE (Cardholder Data Environment)** = systems that store/process/transmit CHD **+ anything connected to or that can affect them**.
- **Segmentation** shrinks the CDE → smaller audit scope, smaller attack surface. Segmentation effectiveness must be **tested** (pen test).
- Reduce scope further: **tokenization** (replace PAN with token), **P2PE** (point-to-point encryption), never storing PAN at all.

### Assessment machinery
| Term | Meaning |
|---|---|
| **QSA** | Qualified Security Assessor (external auditor) |
| **ISA** | Internal Security Assessor |
| **ROC** | Report on Compliance (Level 1 merchants/providers) |
| **SAQ** | Self-Assessment Questionnaire (A, A-EP, D... by channel) |
| **AOC** | Attestation of Compliance (the summary you give partners) |
| **ASV scans** | Quarterly external scans by an Approved Scanning Vendor |
| Pen test | At least annually + after significant change; internal + external; segmentation test |

### Control → evidence mapping (the JD's exact skill)
| PCI Req | Technical control | Audit evidence |
|---|---|---|
| 8 (authN) | Entra MFA + CA policies | Policy export, screenshots, MFA registration report |
| 5 (anti-malware) | MDE on all endpoints | Intune/MDE deployment & health report |
| 10 (logging) | Log retention + SIEM | Retention config, sample alerts, review records |
| 6 (patching) | Patch SLAs | Vulnerability scan trend, remediation tickets |
| 7 (need-to-know) | RBAC + access reviews | Access review completion records, JML tickets |

**Evidence discipline:** timestamped exports/screenshots, ticket trails, sampling, an evidence tracker per control per period. **Never fabricate or backfill evidence — a gap is a finding with a remediation plan.** (Integrity answers get noticed.)

---

## PART D — Framework quick reference (name-recognition level)

| Framework | One-liner | Key structure |
|---|---|---|
| **NIST CSF 2.0** | Voluntary risk framework | 6 functions: **Govern**, Identify, Protect, Detect, Respond, Recover |
| **NIST 800-53** | Federal control catalog | Control families (AC, AU, IR...) |
| **CIS Controls v8** | Prioritized safeguards | 18 controls, IG1/IG2/IG3 implementation groups |
| **CIS Benchmarks** | Per-OS hardening baselines | Feed into Intune/GPO baselines |
| **SOC 1** | Controls over financial reporting | For service orgs affecting customers' financials |
| **SOC 2** | Trust Services Criteria | Security (mandatory) + Availability, Confidentiality, Processing Integrity, Privacy |
| SOC Type I vs II | Design at a point in time vs **operating effectiveness over 6–12 months** | Customers want Type II |
| **ISO 27017/27018** | Cloud security / cloud PII extensions to 27001 | |
| **DPDP Act (India)** | India's data protection law | Awareness level for an India fintech |
| **RBI guidelines** | Indian banking cyber requirements | Zeta context — worth one line of awareness |

```
How they relate:

  ISO 27001  = certify your MANAGEMENT SYSTEM
  SOC 2      = attest your controls to CUSTOMERS
  PCI-DSS    = comply because you touch CARD DATA
  NIST CSF   = organize your PROGRAM thinking
  CIS        = concrete technical BASELINES to implement
        --> One control (e.g., MFA) maps into ALL of them.
        --> Mature orgs build a COMMON CONTROL FRAMEWORK and map outward.
```
That last line ("common control framework, map outward, collect evidence once") is an advanced-sounding, absolutely-true thing to say.

---

## PART E — GRC operations (the daily job)

### Audit support workflow
```
Auditor request list (PBC) --> assign owners --> gather evidence
  --> QC (complete? timestamped? sampled correctly?) --> submit
  --> auditor follow-ups --> findings draft --> management response
  --> remediation plan with dates --> track to closure --> verify
```

### Action item tracking (your superpower — say it in their language)
- Every finding/vulnerability/exception gets: **owner, severity, due date (SLA), status, evidence-of-closure**.
- Weekly aging review; escalate by data, not blame ("15 criticals >30 days in team X" beats "team X is slow").
- Metrics that impress: % closed within SLA, mean time to remediate, aging buckets, repeat findings rate.
- *Your Freshservice SLA dashboard is literally this discipline — present it that way.*

### Risk register anatomy
| ID | Risk description | Owner | L | I | Rating | Treatment | Controls | Residual | Review date |
|---|---|---|---|---|---|---|---|---|---|
| R-042 | Unmanaged BYOD accessing mail | IT Dir | 4 | 3 | High | Mitigate | MAM policies, CA block unmanaged | Medium | 2026-09-01 |

---

## PART F — Interview questions
1. **The 4 risk treatments?** (mitigate/transfer/avoid/accept — with accept's conditions)
2. **Walk me through handling a risk exception request.** (full lifecycle; emphasize business owns risk, time-bound, register)
3. **What is an SoA?** (Annex A applicability declaration; auditor's map)
4. **ISO 27001 vs SOC 2?** (certify ISMS vs attest controls to customers; Type I/II)
5. **How do you scope a PCI assessment?** (CDE definition, segmentation, tokenization to shrink scope, segmentation testing)
6. **Map MFA to frameworks.** (ISO A.5.17/A.8.5 authentication, PCI Req 8, CIS Control 6, NIST Protect — plus evidence for each)
7. **Auditor asks for 12 months of access reviews; you have 9. What do you do?** (present the 9 honestly, gap = finding, root cause, remediation plan with owner/date — never backfill)
8. **How do you get engineering teams to fix findings on time?** (SLAs agreed up front, data-driven escalation, compensating controls meanwhile, exec reporting — your dashboard story)

## Self-test checklist
- [ ] 4 treatments + exception lifecycle from memory
- [ ] ISO: ISMS, PDCA, clauses 4–10, 93 controls / 4 themes, SoA, cert cycle
- [ ] PCI: CDE, segmentation, 12 requirement themes, QSA/ROC/SAQ/ASV, SAD rules
- [ ] I can map ONE control (MFA) across 4 frameworks with evidence
- [ ] SOC 2 Type I vs Type II in one sentence
- [ ] I can describe my dashboard/SOP work in GRC vocabulary
