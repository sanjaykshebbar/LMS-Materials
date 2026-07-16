---
title: "04 — Network & Perimeter Security: Firewalls, Wireless, Zero Trust"
category: "InfoSec, Risk & Compliance Analyst"
tags: [Obsidian-Sync]
---
# 04 — Network & Perimeter Security: Firewalls, Wireless, Zero Trust

> Covers roadmap Block 8. JD mapping: "Network Security" bullet (assess, monitor, regulate, AUDIT — note the verbs: governance of firewalls, not CLI mastery).

---

## PART A — BEGINNER: Networking security foundations

### The layers where security lives
```
L7  Application   <- NGFW app control, WAF, proxies (Zscaler!)
L4  Transport     <- ports, stateful inspection (TCP/UDP)
L3  Network       <- IPs, routing, ACLs, VPN tunnels
L2  Data link     <- VLANs, 802.1X port security, MAC
```

### Core concepts, one line each
- **Stateful inspection** — firewall tracks connection state; return traffic for an allowed outbound session is permitted automatically.
- **NAT** — private IPs translated to public; hides internal topology.
- **DMZ** — semi-trusted zone for internet-facing services, isolated from the internal LAN.
- **VLAN** — logical network segmentation at L2.
- **Proxy** — intermediary that terminates and inspects traffic (forward proxy = users out; reverse proxy = internet in).
- **IDS vs IPS** — detect & alert vs sit inline and block.
- **VPN** — IPsec site-to-site (office↔office/cloud) vs SSL/TLS client VPN (user↔network). Being replaced by ZTNA (see Part D).

---

## PART B — INTERMEDIATE: Next-Gen Firewalls

### Traditional vs NGFW
| Capability | Traditional | NGFW |
|---|---|---|
| Port/IP/stateful rules | Yes | Yes |
| Application awareness | No ("port 443") | Yes ("this is Dropbox, block uploads") |
| User identity in rules | No | Yes (AD/LDAP integration — rule per group) |
| IPS built in | No | Yes |
| TLS/SSL inspection | No | Yes (decrypt, inspect, re-encrypt) |
| Threat intel / sandboxing | No | Yes (cloud lookups, file detonation) |

### Firewall rule anatomy & processing
```
[Source zone/IP] -> [Dest zone/IP] -> [Service/App] -> [User] -> ACTION (allow/deny) + LOG

Processing: TOP-DOWN, FIRST MATCH WINS, implicit DENY at the bottom.
Rule order errors: a broad allow above a specific deny = the deny never fires
("rule shadowing").
```

### How to AUDIT a firewall rule base (YOUR interview answer — memorize the checklist)
```
1. Overly permissive rules        any-any, huge port ranges, 0.0.0.0/0 sources
2. Stale rules                    zero hit count over 90+ days
3. No documentation               rules without ticket ref / owner / description
                                  = change management failure
4. Missing logging                especially on deny rules & CDE boundaries
5. Expired "temporary" rules      opened for a project, never removed
6. Shadowed/redundant rules       unreachable rules below broader ones
7. Exposed management planes      firewall admin UI reachable from internet
8. Weak review cadence            PCI Req 1 mandates ruleset review every 6 months
```
Deliverable of an audit: findings register with severity + owner + remediation date (your tracking skill again).

### Vendor name-map (recognition, not CLI)
| Vendor | Product/OS | Terms you might hear |
|---|---|---|
| Fortinet | FortiGate / FortiOS | Security Fabric, FortiAnalyzer (logs), FortiManager, NSE certs |
| Check Point | Quantum / Gaia | SmartConsole, policy packages, blades |
| Cisco | ASA (legacy), Firepower FTD | FMC (management), Snort IPS |
| SonicWall | TZ/NSa series | mid-market focus |
| Palo Alto | PA-series / PAN-OS | App-ID, Panorama (worth knowing; industry reference) |

If pushed on hands-on: *"My perimeter depth is on the Zscaler side; on traditional firewalls I'm strong on rule-base auditing and governance, and I cross-train fast — I've started Fortinet's NSE self-paced track."*

---

## PART C — INTERMEDIATE: Enterprise wireless (Aruba)

### Authentication models
| Model | How | Verdict |
|---|---|---|
| **WPA2/3-Personal (PSK)** | One shared password | Fine at home; **audit finding** for corporate SSIDs (no per-user identity, leavers keep the key) |
| **WPA2/3-Enterprise (802.1X)** | Per-user auth via **RADIUS** — certificates (EAP-TLS, best) or AD creds (PEAP) | Corporate standard |

- **Aruba ClearPass** = the NAC/RADIUS policy engine (device profiling, posture checks, guest portals).
- **WPA3** improvements: SAE handshake (kills offline dictionary attacks on PSK), forward secrecy.
- **Design hygiene:** guest SSID isolated from corporate (separate VLAN, internet-only), IoT/AV devices on their own segment *(connect to your meeting-room AV work: "we put AV endpoints on segregated VLANs")*, rogue AP detection, disable WPS.

```
Corporate Wi-Fi (802.1X) flow:

Laptop --> AP --> Aruba controller --> RADIUS/ClearPass --> Entra/AD
                                            |
                              policy: user group + device posture
                                            |
                            VLAN assignment / allow / quarantine
```

---

## PART D — INTERMEDIATE/ADVANCED: Zero Trust & SASE (lead with your Zscaler strength)

### Perimeter model vs Zero Trust
```
OLD: castle & moat                      NEW: zero trust
+---------------------+                 Every request, every time:
| trusted inside      |                   - verify IDENTITY (MFA)
|  <- firewall ->     |                   - verify DEVICE (compliance)
| untrusted outside   |                   - verify CONTEXT (location, risk)
+---------------------+                   - least-privilege, app-level access
"inside = trusted"                      "never trust, always verify"
```

### SASE/SSE vocabulary (you have real experience — own it)
- **SWG** (Secure Web Gateway) = Zscaler ZIA: cloud proxy inspecting user web traffic anywhere.
- **ZTNA** = Zscaler ZPA: app-level access brokered by identity/posture — **replaces VPN**; users never land "on the network."
- **CASB** — visibility/control over SaaS usage (shadow IT discovery, DLP into sanctioned apps).
- **SASE** = SWG + ZTNA + CASB + FWaaS + SD-WAN converged in cloud. **SSE** = the security half (Gartner term).
- Your line: *"I've operated a zero-trust stack in production — Zscaler ZIA/ZPA integrated with Entra ID and device posture from Intune. Traditional perimeter concepts map cleanly onto it."*

### Advanced talking points
- **Microsegmentation** — east-west traffic control inside the network/DC.
- **TLS inspection trade-offs** — privacy (banking/health bypass lists), certificate pinning breakage, compliance requirements.
- **NDR** (network detection & response) — one-line awareness.
- **Firewall change management** — request → risk review → approval → implement in window → verify → document. (Change tickets = audit evidence for PCI Req 1/6.)

---

## PART E — Interview questions
1. **"Audit a rule base you've never seen — how?"** → the 8-point checklist + deliverable as findings register.
2. **"What makes a firewall next-gen?"** → app awareness, user identity, IPS, TLS inspection, threat intel.
3. **"PSK vs 802.1X for corporate Wi-Fi?"** → per-user identity, revocation on offboarding, posture via ClearPass; PSK = finding.
4. **"Explain zero trust."** → never trust/always verify + your Zscaler production story.
5. **"How does ZTNA differ from VPN?"** → network-level access vs app-level; no lateral movement surface; posture-aware.
6. **"A business unit wants port 3389 (RDP) open inbound for a vendor."** → never raw to internet; alternatives (ZPA/jump host/VPN + MFA + source restriction), risk exception process if unavoidable, time-bound + logging.
7. **"Where do firewalls sit in PCI?"** → Req 1; CDE boundary control; 6-month ruleset reviews; segmentation testing.

## Self-test checklist
- [ ] 8-point firewall audit checklist from memory
- [ ] NGFW vs traditional in 4 bullet points
- [ ] 802.1X flow + why PSK fails corporate audit
- [ ] Zero trust explained through my own Zscaler experience
- [ ] One safe answer for the "I haven't run FortiGate CLI" question
