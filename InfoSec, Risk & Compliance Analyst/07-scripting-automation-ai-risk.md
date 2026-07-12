# 07 — Scripting for Security, Compliance Automation & AI Risk

> Covers roadmap Block 11. JD mapping: "Automation & Scripting", "Compliance Automation", "Emerging Tech & AI". You're already strong here — this file AIMS your skill at security use cases.

---

## PART A — The three script archetypes interviewers ask about

### 1. Log analysis (detect something bad in a log)
**Bash one-liner thinking (say the pipeline aloud):**
```bash
# Top source IPs for failed SSH logins
grep "Failed password" /var/log/auth.log \
  | awk '{print $(NF-3)}' \
  | sort | uniq -c | sort -rn | head -20
```
**Python version (the structured answer):**
```python
import re, csv
from collections import Counter

pattern = re.compile(r"Failed password .* from (\d+\.\d+\.\d+\.\d+)")
hits = Counter()
with open("auth.log") as f:
    for line in f:
        m = pattern.search(line)
        if m:
            hits[m.group(1)] += 1

with open("bruteforce_report.csv", "w", newline="") as out:
    w = csv.writer(out)
    w.writerow(["source_ip", "failed_attempts"])
    for ip, n in hits.most_common():
        if n >= 10:                    # threshold
            w.writerow([ip, n])
```
**How to narrate brute-force detection logic:** parse timestamp + source + outcome → count failures per source per time window (e.g., >10 in 5 min) → output report / raise alert → (advanced) auto-block via firewall API with allow-list safety.

### 2. Compliance check (verify a control across the fleet)
You've literally built this pattern (Intune Proactive Remediation):
```bash
# Detection: is FileVault on? (macOS)
if fdesetup status | grep -q "FileVault is On"; then
  exit 0      # compliant
else
  exit 1      # triggers remediation / flags non-compliance
fi
```
PowerShell equivalent for BitLocker: `(Get-BitLockerVolume -MountPoint C:).ProtectionStatus`.
**The framing:** *"detection script + remediation script + scheduled execution + centralized reporting = continuous control monitoring."* That phrase is GRC gold.

### 3. Evidence automation via API (compliance automation — the JD bullet)
```python
# Sketch: pull Intune device compliance for monthly audit evidence
import requests
url = "https://graph.microsoft.com/v1.0/deviceManagement/managedDevices"
r = requests.get(url, headers={"Authorization": f"Bearer {token}"},
                 params={"$select": "deviceName,complianceState,lastSyncDateTime"})
# -> write to timestamped xlsx -> drop in evidence folder
```
**Your story, upgraded:** "My openpyxl/Python Excel automation + Graph API work is compliance automation — I turn manual screenshot-collection into scheduled, timestamped, repeatable evidence generation. Same report every month, zero drift, audit-ready."

Other automation targets to mention: monthly access-review exports, stale-account reports (last sign-in > 90 days), MFA registration gaps, patch compliance trend charts, certificate expiry monitors.

### Script GOVERNANCE (the L2 R&C twist most candidates miss)
Reviewing scripts is in the JD ("developing AND reviewing"). Your review checklist:
```
1. Hardcoded secrets?            never; use Key Vault / env vars / managed identity
2. Least privilege?              scoped API permissions, read-only where possible
3. Error handling?               fail safe, not fail open  (your set -e story!)
4. Logging?                      what it did, when, as whom
5. Input validation?             injection into shell commands
6. Change control?               version control, peer review, tested in staging
```
Your eksctl debugging story (set -e + grep exit codes, CRLF line endings) = a *real* example of why script review matters. Use it.

---

## PART B — AI risk (small JD bullet, big differentiation opportunity)

### The enterprise AI risk list
| Risk | What happens | Control |
|---|---|---|
| **Data leakage** | Employees paste confidential/customer data into public chatbots | AUP for AI, DLP rules on AI domains, sanctioned enterprise tools with no-training guarantees |
| **Shadow AI** | Unsanctioned tools adopted team-by-team | Discovery via CASB/Zscaler logs, approved-tool catalog |
| **Prompt injection** | Malicious input hijacks an AI integration | Input/output filtering, least-privilege tool access, human approval for actions |
| **Hallucination** | Confident wrong output used in decisions | Human review requirements, no unreviewed AI output in security/compliance decisions |
| **Model/vendor risk** | Where does data go? training reuse? retention? | Vendor assessment (your questionnaire skill!), DPAs, data residency |

### Governance frameworks to name
- **NIST AI RMF** — govern/map/measure/manage AI risks.
- **ISO/IEC 42001** — AI management system standard (the "ISO 27001 of AI").
- **EU AI Act** — risk-tiered regulation (awareness level).

### Your one-paragraph interview answer
*"The biggest immediate risk is data leakage — staff pasting sensitive data into public AI tools. Controls: an AI acceptable-use policy, DLP coverage of AI web categories, offering a sanctioned enterprise alternative so the secure path is the easy path, and folding AI vendors into normal third-party risk assessment. For AI we integrate ourselves, prompt injection and output review become the concerns. NIST's AI RMF gives the governance structure."*

---

## Interview questions
1. "Write/describe a script to detect brute-force attempts in a log." *(pipeline narration above)*
2. "How would you automate compliance evidence collection?" *(Graph API → timestamped artifacts; continuous control monitoring)*
3. "What do you look for when reviewing someone else's script?" *(6-point checklist + your CRLF/set -e war story)*
4. "What risks do AI tools bring to an enterprise and what controls apply?" *(the paragraph above)*
5. "Bash or Python — when?" *(bash: quick pipelines on a box; Python: structured parsing, APIs, reports, testability)*

## Self-test checklist
- [ ] I can narrate brute-force detection logic without notes
- [ ] I can state the detection/remediation/reporting = continuous control monitoring framing
- [ ] 6-point script review checklist
- [ ] AI risk paragraph rehearsed aloud
- [ ] My eksctl debugging story shaped as a script-governance lesson
