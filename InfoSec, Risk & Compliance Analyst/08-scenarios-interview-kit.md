# 08 — Scenario Drills, Behavioral Stories & Interview Kit

> Covers roadmap Blocks 6, 12, 13. This file is practiced ALOUD, not read.

---

## PART A — The universal scenario skeleton
Answer every "what would you do if..." with this spine:
```
ASSESS  ->  CONTAIN/ACT  ->  COMMUNICATE  ->  DOCUMENT  ->  PREVENT RECURRENCE
(scope,     (stop the       (stakeholders,   (ticket,      (root cause,
 severity,   bleeding)       users, mgmt)     evidence,     control/policy
 data class)                                  register)     change)
```
End technical answers with the governance beat: *"...and I'd log it as a finding with an owner and an SLA."* End GRC answers with a technical example. That bridge IS the role.

---

## PART B — The six drills (3–5 minutes aloud, each)

### Drill 1 — Phishing campaign with clicks
*"40 users received a phish; 3 clicked."*
- Assess: Threat Explorer → full recipient list, verdicts, who clicked (Safe Links click data), was it credential harvesting or malware?
- Contain: purge campaign from mailboxes; block sender/URL/IoCs (tenant block list); for the 3 clickers → reset passwords + **revoke sessions/refresh tokens** (resetting alone doesn't kill live sessions — saying this = depth), check Identity Protection risky sign-ins, MDE scan their devices.
- Communicate: warn recipients, brief helpdesk, notify manager/CISO thread if credentials were entered.
- Document: incident record, IoCs, timeline.
- Prevent: tune anti-phish/impersonation policy, submission to Microsoft, targeted awareness nudge; simulation for that pattern later.

### Drill 2 — Risk exception request
*"Sales VP wants Dropbox unblocked for one client."*
- Understand the actual need (receive files? send? size?).
- **Offer the sanctioned path first** (OneDrive external sharing / secure transfer) — exceptions are the last resort, alternatives are the first.
- If unavoidable: scope tightly (named users, monitored, DLP applied), compensating controls, **risk owner signs** (VP's org owns the risk), 90-day expiry, risk register entry, review at expiry.
- Tone: partner, not blocker. "Yes, safely" beats "no."

### Drill 3 — Audit evidence gap
*"Auditor wants 12 months of access reviews; you find 9."*
- Provide the 9 honestly, completeness-checked.
- The 3-month gap = **finding**. Root cause (owner left? process not scheduled?).
- Remediation plan: assign owner, calendarize reviews, automate export.
- **Never backfill/fabricate.** Integrity is the answer being tested.

### Drill 4 — Mass non-compliance event
*"200 macOS devices non-compliant overnight."*
- Triage: what changed? (Intune audit logs: policy edited? new OS release tripping min-version? cert expiry? service incident — check M365 health.)
- Communicate early to helpdesk (ticket wave incoming) + status note to IT channel.
- Fix root cause; force re-evaluation in rings; verify recovery curve.
- Post-incident: change-control gap? alerting on compliance-rate drop?
- *(You have real adjacent stories — swap one in.)*

### Drill 5 — Missed remediation SLAs
*"DevOps has 15 criticals past SLA."*
- Verify data first (rescan — some may be fixed but unverified).
- Meet the team: blockers? (dependency, freeze, resourcing.)
- Escalate **with data, not blame**: aging report, risk framing, options.
- Interim compensating controls on the exposed assets.
- If truly stuck: formal risk acceptance by their leadership — makes risk visible and owned. *(Your dashboard/escalation muscle — flex it.)*

### Drill 6 — Business pushback on security
*"Sales says MFA is slowing deals; they want it off."*
- Hear the friction specifically (which flow? how often prompted?).
- Reframe risk in business terms: account takeover → client data → regulatory + reputational + deal damage.
- **Offer alternatives, not a flat no:** phishing-resistant but low-friction methods (passkeys/Windows Hello), risk-based CA (prompt only on risky sign-ins), sign-in frequency tuning on compliant devices.
- If they insist: that's a risk acceptance decision for THEIR leadership, documented — usually ends the request.

---

## PART C — Your STAR story bank (fill in, then rehearse)

| # | Prompt it answers | Your story | The GRC punchline |
|---|---|---|---|
| 1 | "Found a gap in a process" | Intern→FTE access SOP analysis: missing IT step, no owner, no trigger, no SLA for access blocking | "Access control gap in a JML process — I identified it, proposed the control, assigned ownership" |
| 2 | "Automated something manual" | Intune Proactive Remediation pkg (detection+remediation scripts, Graph API); root-caused set -e/grep and CRLF failures | "Continuous control monitoring + why script review matters" |
| 3 | "Drove items to closure" | Freshservice SLA dashboard: aging, breach tracking, escalation | "The exact tracking discipline this role owns for vulns and audit gaps" |
| 4 | "Cross-functional coordination" | New office IT setup / convened HR-Infosec-IT meeting | "Translated between business and technical teams; drove decisions to owners" |
| 5 | "Assessed third-party risk" | 58-question vendor evaluation incl. security sections | "Vendor risk assessment — patching, data handling, integration security" |
| 6 | "Handled pressure / debugging" | eksctl script failure root-cause under time pressure | "Methodical isolation; fail-safe vs fail-open lesson" |

Format each aloud: 1 line situation → 1 line task → 3 lines action → 1 line measurable result → 1 line GRC angle. 90 seconds max.

---

## PART D — Rapid-fire technical Q bank (self-quiz; answers in files 01–07)
1. Compliance policy vs configuration profile?
2. Five baseline CA policies?
3. Sign-in risk vs user risk?
4. Why block legacy auth?
5. SPF/DKIM/DMARC one-liner + what alignment means?
6. p=none → p=reject rollout?
7. Safe Links vs gateway URL filtering?
8. Four risk treatments?
9. What's an SoA? SOC 2 Type I vs II?
10. CDE and how segmentation shrinks PCI scope?
11. Firewall audit checklist (8 points)?
12. PSK vs 802.1X?
13. Shared responsibility, IaaS vs SaaS?
14. How to audit IAM (8 points)?
15. VA vs PT + PCI cadence?
16. Prioritizing vulns beyond CVSS?
17. DLP rollout ladder?
18. Script review checklist?
19. Top enterprise AI risk + control?
20. Walk through a phishing response end-to-end.

---

## PART E — Openers and closers

### "Tell me about yourself" (90 seconds — the spine)
Current role at a banking-tech company → operate the Microsoft security-adjacent stack daily (Intune across Windows/macOS, Entra, Zscaler zero-trust) → keep gravitating to the governance side: SOP gap analysis, SLA/aging dashboards, vendor assessments, cross-team remediation chasing → this role formalizes exactly that bridge → currently scheduled for SC-900 *(schedule it so this is true)* → what you bring day one: fleet-scale endpoint/identity operations + tracking discipline + business translation.

### Your questions for them (pick 3)
1. "How mature is the risk register today — established or being built?"
2. "Which audit is the biggest lift this year — ISO surveillance, PCI, or SOC 2?"
3. "How does the role split between hands-on technical work and GRC work, week to week?"
4. "What does success look like at 90 days?"
5. "What's the biggest open remediation theme right now?" *(bold, memorable)*

### Handling the cert question
"I don't hold one of the listed certs yet — I've scheduled SC-900 for [date] and I'm sitting the ISC² CC right after. Given that I operate Intune, Entra, and Defender daily, the exam content maps to my working knowledge, so I'm treating it as formalization rather than new learning."

### Handling the firewall-depth question
"My perimeter experience is on the modern side — Zscaler ZIA/ZPA in production, which is SASE/zero-trust. On traditional NGFWs I'm strong on rule-base auditing and governance and I've started Fortinet's NSE track. For an assess/monitor/audit mandate, I can contribute immediately; for deep configuration I'll cross-train fast — I've done it before with [example]."

---

## Final pre-interview ritual (day of)
1. Read only your one-page cheat sheet (roadmap Block 13).
2. Say the SPF/DKIM/DMARC one-liner + exception lifecycle aloud once.
3. Skim your 6 STAR keywords.
4. Three questions for them chosen.
5. Water. Breathe. You operate this stack every day — the interview is a translation exercise, and you've done the translation work.
