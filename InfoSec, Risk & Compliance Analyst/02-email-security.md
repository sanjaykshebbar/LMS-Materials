# 02 — Email Security: SPF, DKIM, DMARC & Defender for Office 365

> Covers roadmap Block 4 — your highest-priority technical gap. JD mapping: "Email Security & Gateway Security" bullet.

---

## PART A — BEGINNER: Why email security exists

### The core problem
SMTP (1982) has **no built-in sender verification**. Anyone can claim to be anyone. Email has TWO "from" addresses:

| | Envelope From (MAIL FROM / Return-Path) | Header From |
|---|---|---|
| Who sees it | Mail servers only | The human user |
| Used for | Bounce handling, SPF check | Display in inbox |
| Spoofable? | Yes | Yes — and this is what phishing exploits |

**Spoofing** = forging the visible From. **Phishing** = social engineering via email. **BEC (Business Email Compromise)** = impersonating executives/vendors to redirect payments — the most financially damaging email attack class.

### The defense stack at a glance
```
Inbound mail journey:

Internet --> [Connection filtering: IP reputation, RBLs]
         --> [SPF check]        does sending IP match sender domain's DNS?
         --> [DKIM check]       does the crypto signature verify?
         --> [DMARC check]      do SPF/DKIM ALIGN with visible From? policy?
         --> [Anti-malware]     known-bad attachments
         --> [Safe Attachments] detonate unknown files in sandbox
         --> [Anti-spam/phish]  content, impersonation, mailbox intelligence
         --> [Safe Links]       rewrite URLs, verify at click time
         --> INBOX / JUNK / QUARANTINE
```

---

## PART B — INTERMEDIATE: The authentication trio in depth

### SPF — Sender Policy Framework
**What:** DNS TXT record listing servers authorized to send mail for your domain. Receiver checks: *does the connecting IP appear in the MAIL FROM domain's SPF record?*

**Anatomy:**
```
v=spf1 include:_spf.google.com include:spf.protection.outlook.com ip4:203.0.113.5 -all
       \__________________________________________________________/  \__/
                    authorized senders                              qualifier
```
Qualifiers: `-all` hard fail (reject) | `~all` soft fail (accept, mark) | `?all` neutral | `+all` allow everything (never do this).

**SPF limits (interview gold):**
1. **10 DNS lookup limit** — too many `include:` chains → permerror → SPF effectively broken.
2. **Breaks on forwarding** — forwarder's IP isn't in your record.
3. **Checks MAIL FROM, not header From** — SPF alone does NOT stop display-From spoofing.

### DKIM — DomainKeys Identified Mail
**What:** Sending server cryptographically **signs** selected headers + body hash with a private key. Public key published in DNS at `selector._domainkey.yourdomain.com`. Receiver verifies.

**What it proves:** message wasn't altered in transit + the signing domain authorized it.
**Key property:** the signature travels WITH the message → **survives forwarding** (mostly — mailing lists that modify body/subject break it).
Selectors allow key rotation and multiple senders (e.g., `selector1`, `google`, `mailchimp`).

### DMARC — the policy + reporting layer
**What:** DNS record at `_dmarc.yourdomain.com` that (1) requires **alignment**, (2) tells receivers what to do on failure, (3) gives you reports.

```
v=DMARC1; p=quarantine; sp=reject; pct=100; rua=mailto:dmarc@zeta.tech; ruf=mailto:forensics@zeta.tech; adkim=r; aspf=r
```
| Tag | Meaning |
|---|---|
| `p=` | policy: none / quarantine / reject |
| `sp=` | policy for subdomains |
| `pct=` | % of failing mail the policy applies to (staged rollout) |
| `rua=` | aggregate reports (daily XML summaries — WHO is sending as you) |
| `ruf=` | forensic reports (per-failure samples; many receivers don't send) |
| `adkim=`/`aspf=` | alignment mode: r(elaxed) = org domain match; s(trict) = exact match |

**ALIGNMENT is the whole point:** DMARC passes only if SPF *or* DKIM passes **AND** the domain that passed **matches the visible header From domain**. This is what finally stops header spoofing.

```
DMARC evaluation:

        SPF pass? --------- yes --> SPF domain aligns with From? --- yes --+
             |                                                             |
             no                                                            v
             |                                                        DMARC PASS
        DKIM pass? -------- yes --> DKIM domain aligns with From? -- yes --+
             |                                                    
             no --> both fail or unaligned --> DMARC FAIL --> apply p= policy
```

**Rollout path (a guaranteed interview question):**
```
p=none (monitor)  -->  read rua reports weekly  -->  find forgotten legit
                       senders (CRM, marketing, HR tools) --> add them to
                       SPF / set up DKIM for them
       -->  p=quarantine; pct=25 --> 50 --> 100
       -->  p=reject
Timeline: typically 4–12 weeks. Never jump straight to reject.
```

**The memorized one-liner:** *"SPF authorizes the sending server, DKIM cryptographically proves integrity and domain authorization, DMARC enforces alignment with the visible From and tells receivers what to do on failure — plus gives reporting."*

### Related standards (advanced name-drops)
- **ARC** — Authenticated Received Chain; preserves auth results through forwarders/mailing lists.
- **BIMI** — brand logo in inbox; requires DMARC at enforcement.
- **MTA-STS / TLS-RPT** — enforce TLS for mail transport + reporting.
- **DANE** — DNSSEC-based TLS enforcement (more common in EU/gov).

---

## PART C — INTERMEDIATE: Exchange Online Protection & Defender for Office 365

### The layering
| Layer | Included with | Key features |
|---|---|---|
| **EOP** | All M365 | Connection filtering, anti-spam, anti-malware, transport rules, quarantine |
| **MDO Plan 1** | Business Premium / add-on | Safe Attachments, Safe Links, anti-phishing impersonation protection, real-time detections |
| **MDO Plan 2** | E5 / add-on | Threat Explorer, Automated Investigation & Response (AIR), Attack Simulation Training, campaign views |

### Safe Attachments
Unknown attachments are **detonated in a sandbox** before delivery. Policies: Monitor / Block / Dynamic Delivery (deliver body immediately, attachment follows after scan). Also covers SharePoint/OneDrive/Teams files.

### Safe Links
URLs **rewritten** to pass through Microsoft's check **at time of click** — defeats the "weaponize the link after delivery" trick that beats gateway-time scanning. Applies in email, Teams, Office apps.

### Anti-phishing policies (impersonation protection)
- **User impersonation** — protect named VIPs (CEO, CFO) from display-name tricks (`Rahul Sharma <rahul.sharma@gmail-mail.com>`).
- **Domain impersonation** — lookalike domains (zeta-tech.com vs zetatech.com).
- **Mailbox intelligence** — learns each user's normal correspondents; flags anomalies.
- Actions: quarantine, junk, tag with safety tip.

### Preset security policies
**Standard** and **Strict** — Microsoft-managed baselines that auto-update. Mature answer: *"Start from preset policies, then layer targeted custom policies only where the business needs differ — custom sprawl is how orgs drift out of best practice."*

### Operations you'd run day-to-day
- **Quarantine review** + user release request workflow
- **User-reported phishing** — report button → triage in Submissions → block sender/URL → purge campaign (Threat Explorer, Plan 2: soft-delete from all mailboxes)
- **Tuning** — false positive/negative submissions to Microsoft, allow/block lists (tenant allow/block list), transport rule hygiene
- **Evidence for audits** — policy exports, quarantine stats, phishing simulation results

---

## PART D — ADVANCED: scenarios & failure modes

### Scenario: CEO spoof reaches the gateway
```
Attacker sends: From: "CEO Name" <ceo@zeta-tech.co> (lookalike domain)
1. SPF: attacker's domain, their record — may PASS (their own domain!)
2. DKIM: signed by attacker's domain — may PASS
3. DMARC on zeta.tech: NOT triggered (From domain is zeta-tech.co, not yours)
   --> This is why auth alone isn't enough for lookalikes
4. Anti-phish DOMAIN IMPERSONATION catches the lookalike --> quarantine
5. If it were exact-domain spoof (ceo@zeta.tech from foreign IP):
   SPF fails + no DKIM + DMARC p=reject --> rejected at the gate
```
Lesson to articulate: **DMARC stops exact-domain spoofing; impersonation protection stops lookalikes; user training catches what slips through.**

### Why SPF fails on forwarding but DKIM survives
Forwarder re-sends from THEIR IP (not in your SPF) but doesn't touch the DKIM signature → DKIM still validates → DMARC can still pass via DKIM alignment. Mailing lists that add footers/modify subject break DKIM too → ARC exists for this.

### Common real-world findings (audit lens)
- SPF with `+all` or >10 lookups (permerror)
- DMARC stuck at `p=none` for years (monitoring theater)
- No DKIM on third-party senders (marketing tools) → they fail alignment
- Quarantine nobody reviews
- Allow-list entries with no expiry (risk exceptions without governance!)

---

## PART E — Hands-on lab (30 min, do this before the interview)
```bash
# Inspect real records (any OS with nslookup/dig):
nslookup -type=txt zeta.tech                 # find v=spf1 line
nslookup -type=txt _dmarc.zeta.tech          # DMARC policy
nslookup -type=txt selector1._domainkey.zeta.tech   # DKIM (try selector1/selector2 for M365)
```
Also: check any domain on mxtoolbox.com (SPF/DKIM/DMARC/blacklist tabs). In an interview you can say: *"I pulled our own production records this week — we publish X and enforce Y."* Instant credibility.

---

## PART F — Interview questions
1. Explain SPF, DKIM, DMARC and how they work together. *(one-liner + alignment)*
2. What does `p=quarantine` mean and how do you get to `p=reject` safely? *(rollout path + rua reports)*
3. Why does SPF break on forwarding? *(IP-based; DKIM survives)*
4. Difference between Safe Links and normal URL filtering? *(time-of-click vs gateway-time)*
5. A user reports a phish that 40 people received — walk me through response. *(triage → Threat Explorer scope → purge → block IoCs → check for clicks/credential entry → reset+revoke sessions for clickers → user comms → tune policy → document)*
6. What's the difference between EOP and Defender for Office 365? *(layering table)*
7. How would you protect the CEO from impersonation? *(user impersonation policy + DMARC enforcement + lookalike domain monitoring + payment-change process controls — note the last one is a PROCESS control: BEC is beaten by process, not just tech)*

## Self-test checklist
- [ ] I can recite the one-liner and draw the DMARC decision flow
- [ ] I can write a valid SPF and DMARC record from memory
- [ ] I can explain alignment and why it stops header spoofing
- [ ] I know the p=none → reject rollout path with pct staging
- [ ] I can layer EOP vs MDO P1 vs P2 features correctly
- [ ] I've looked up a real domain's records myself
