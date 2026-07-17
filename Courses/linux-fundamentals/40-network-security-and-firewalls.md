---
type: lesson
course: linux-fundamentals
module: "Module 7: Linux Security and Access Control"
order: 40
title: Network Security and Firewalls
---

# Network Security and Firewalls

> 🎥 [Search YouTube for "Network Security and Firewalls"](https://www.youtube.com/results?search_query=Network%20Security%20and%20Firewalls%20Linux%20Fundamentals%20tutorial)

Network security and firewalls are crucial components of a Linux system's defense mechanism. They help protect the system from unauthorized access, malicious activities, and data breaches. In this lesson, we will explore the basics of network security and firewalls, and how to configure them on a Linux system.

## Network Security Basics

Network security refers to the practices and measures taken to protect a network from unauthorized access, use, disclosure, disruption, modification, or destruction. This includes protecting against malware, viruses, and other types of cyber threats.

### Types of Network Security Threats

* **Malware**: Software designed to harm or exploit a system.
* **Viruses**: Malicious code that replicates itself and spreads to other systems.
* **Trojans**: Malicious software disguised as legitimate programs.
* **Denial of Service (DoS)**: Overwhelming a system with traffic to make it unavailable.
* **Man-in-the-Middle (MitM) Attack**: Intercepting communication between two parties.

## Firewalls

A firewall is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules. Firewalls can be hardware-based or software-based.

### Types of Firewalls

* **Network-based Firewalls**: Sit between the internet and a network, controlling incoming and outgoing traffic.
* **Host-based Firewalls**: Run on individual hosts, controlling incoming and outgoing traffic.
* **Application-based Firewalls**: Control traffic at the application level, rather than network or host level.

### Configuring Firewalls

To configure a firewall on a Linux system, you can use the `ufw` (Uncomplicated Firewall) command-line tool.

```bash
sudo ufw status
sudo ufw enable
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https
sudo ufw deny from 192.168.1.0/24
```

### Firewall Rules

Firewall rules are used to define what traffic is allowed or blocked. Here are some common rules:

* **Allow**: Permit incoming or outgoing traffic on a specific port or protocol.
* **Deny**: Block incoming or outgoing traffic on a specific port or protocol.
* **Reject**: Block incoming traffic with a rejection message.
* **Drop**: Block incoming traffic without sending a rejection message.

## Mermaid Diagram: Firewall Architecture

```mermaid
graph LR
    A[Internet] -->|HTTP|> B[Firewall]
    B -->|HTTP|> C[Web Server]
    A[Internet] -->|SSH|> B[Firewall]
    B -->|SSH|> D[SSH Server]
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#ff0,stroke:#333,stroke-width:2px
    style C fill:#0f0,stroke:#333,stroke-width:2px
    style D fill:#0f0,stroke:#333,stroke-width:2px
```

[Image: A diagram showing the flow of traffic through a firewall, with the internet, firewall, web server, and SSH server.](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Firewall_architecture.svg/800px-Firewall_architecture.svg.png)

In this lesson, we have covered the basics of network security and firewalls, including types of network security threats, types of firewalls, and configuring firewalls on a Linux system. We have also discussed firewall rules and a Mermaid diagram illustrating the architecture of a firewall.
