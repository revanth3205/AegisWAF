# 🔥 Aegis Web Application Firewall (AWAF)

## 📌 Project Overview
The **Aegis Web Application Firewall (AWAF)** is a custom-built security system designed to monitor, filter, and protect web applications from malicious HTTP traffic. It operates as a **reverse proxy**, inspecting each incoming request, applying security rules, and deciding whether to allow or block the request before forwarding it to the backend application.

---

## 🎯 Objectives
- Design a custom firewall capable of detecting common web attacks  
- Implement real-time traffic inspection and filtering  
- Provide configurable security rules  
- Simulate enterprise-level WAF architecture  
- Log and analyze malicious traffic for forensic purposes  

---

## 🏗 System Architecture
Client → WAF Engine → Backend Server → Database


---

## ⚙️ Core Modules

### 🔹 Firewall Engine
Handles incoming requests and forwards safe traffic to backend.

### 🔹 Rule Engine
Detects malicious patterns using regex-based detection.

### 🔹 Rate Limiter
Prevents excessive requests from a single IP.

### 🔹 Logger
Stores attack logs for monitoring and analysis.

### 🔹 Configuration System
Controls firewall behavior dynamically.

---

## 🚀 Key Features

- SQL Injection detection  
- Cross-Site Scripting (XSS) detection  
- Command Injection detection  
- IP blacklisting  
- Anomaly-based detection system  
- Multi-threaded request handling  
- Reverse proxy functionality  
- Sliding window rate limiting  
- Detailed logging system  

---

## 🔄 Working Mechanism

1. Client sends an HTTP request  
2. Firewall intercepts and parses the request  
3. Rate limiter checks request frequency  
4. Rule engine scans request payload  
5. Anomaly score is calculated  
6. If score exceeds threshold → request is blocked  
7. Otherwise → request is forwarded to backend server  

---

## 🧪 Attack Simulation

### 🔹 SQL Injection
http://localhost:8080/?id=1' OR 1=1 --


### 🔹 XSS
http://localhost:8080/?q=<script>alert(1)</script>


### 🔹 Command Injection
http://localhost:8080/?cmd=ls;ct/etc/passwd


---

## ✅ Advantages

- Real-time protection against common web attacks  
- Modular and extensible design  
- Easy configuration using JSON  
- Lightweight and efficient  
- Suitable for academic and research purposes  

---

## ⚠️ Limitations

- Regex-based detection may produce false positives  
- Limited protection against advanced evasion techniques  
- No built-in HTTPS support (can be added)  
- Not optimized for high-scale production environments  

---

## 🚀 Future Enhancements

- Machine learning-based anomaly detection  
- Real-time monitoring dashboard  
- TLS/HTTPS support  
- Docker containerization  
- Integration with SIEM systems  
- Persistent IP banning and threat intelligence feeds  

---

## 🎓 Conclusion

The Advanced Web Application Firewall demonstrates how modern security systems can be built using modular components. It provides a strong foundation for understanding real-world WAF technologies and can be extended further for enterprise use cases.

---

## 👨‍💻 Author

**Revanth Kengana**  
Cybersecurity Enthusiast
