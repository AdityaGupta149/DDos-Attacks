# 🚀 DDoS Attack Simulation using Python

## 📌 Overview
This project demonstrates the simulation of two common Denial of Service (DoS) attacks in a controlled environment:

- 🔴 **HTTP Flood Attack (Layer 7 - Application Layer)**
- 🔵 **UDP Flood Attack (Layer 4 - Transport Layer)**

The attacks are implemented using Python scripts and analyzed using **Wireshark** to study abnormal network traffic patterns.

---

## 🎯 Objective
The objective of this project is to gain practical understanding of:

- How DDoS attacks work  
- How network traffic behaves during an attack  
- How to detect abnormal patterns using packet analysis  

---
## 🧠 About the Attacks

### 🔴 HTTP Flood Attack (Layer 7)

An HTTP Flood attack is a type of application-layer DDoS attack where a large number of HTTP requests (GET/POST) are sent to a web server to overwhelm it.

#### 📌 How it works:
- The attacker sends continuous HTTP requests to the server  
- Each request consumes server resources (CPU, memory, threads)  
- The server becomes slow or unresponsive  

#### 📌 Characteristics:
- Looks like legitimate traffic  
- Difficult to detect  
- High number of repeated requests  
- Targets web servers  

---

### 🔵 UDP Flood Attack (Layer 4)

A UDP Flood attack is a transport-layer attack where a large number of UDP packets are sent to a target system.

#### 📌 How it works:
- The attacker sends random UDP packets to a target port  
- The system tries to process or respond to each packet  
- Resources get exhausted due to high traffic  

#### 📌 Characteristics:
- No connection required (connectionless protocol)  
- Very fast packet transmission  
- High bandwidth consumption  
- No acknowledgment mechanism
---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|--------|
| Python | Attack simulation |
| Requests Library | HTTP request generation |
| Socket Programming | UDP packet transmission |
| Wireshark | Packet capture & analysis |

---

## 📂 Project Structure
DDoS-Simulation
│
├── http_flood.py # HTTP Flood Simulation
├── udp_flood.py # UDP Flood Simulation
├── HTTP_Report.pdf # HTTP Attack Report
├── UDP_Report.pdf # UDP Attack Report
└── README.md

---
## ⚙️ How to Run

1️⃣ Start Local Server (for HTTP Flood)

python -m http.server 8080

2️⃣ Run HTTP Flood Attack

python http_flood.py

3️⃣ Run UDP Flood Attack

python udp_flood.py

---

📊 Wireshark Analysis

🔴 HTTP Flood Attack
Continuous HTTP GET requests
High packet transmission rate
Repeated request patterns

📌 Example:
GET / HTTP/1.1
Host: 127.0.0.1

🔵 UDP Flood Attack
Large number of UDP packets
No connection establishment
High-speed packet transmission

📌 Example:

Protocol: UDP

Length: 1024 bytes

---
⚠️ Disclaimer
This project is developed strictly for educational purposes only.

All simulations are performed on localhost (127.0.0.1)

No real systems or networks are targeted

Do not use this code for malicious activities

---

📚 Learning Outcomes
Understanding of DoS/DDoS attack mechanisms

Hands-on experience with Wireshark

Knowledge of network traffic analysis

Practical implementation of Python networking

---
🚀 Future Scope

Implement SYN Flood attack

Add detection mechanisms (IDS/IPS)

Apply rate-limiting techniques

Visualize traffic patterns
