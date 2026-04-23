# Deception-Based-Security-Mechanism-using-a-Web-Honeypot-Flask-
A Flask-based deception honeypot that simulates a bank login page to capture and log suspicious activity including credentials, IP address, and user-agent.

📌 Overview
This project implements a web-based honeypot that mimics a real banking login page to detect and log malicious activity.
Any interaction with the system is treated as suspicious and recorded, including:
Login attempts
User credentials
IP address
Browser information

🎯 Objectives
Simulate a realistic banking login interface
Capture attacker interaction data
Log and monitor suspicious activity
Demonstrate deception-based security

🛠️ Technologies Used
Python (Flask)
HTML, CSS
JSON (for logging)

⚙️ Features
Fake bank login page
Captures username & password attempts
Logs IP address and user-agent
Displays alert page for attacker
Admin dashboard to view logs
Stores logs in structured JSON format

🚀 How It Works
User visits fake login page → event logged
User enters credentials → captured & stored
System redirects to alert page
Admin can view logs at /logs

▶️ Run the Project
python honeypot.py
Then open:
http://127.0.0.1:5000/login

🧪 Demonstration
🔹 Fake Bank Login Page
🔹 Suspicious Activity Alert
🔹 Honeypot Logs Dashboard
🔹 Captured Log Data (JSON)

📊 Sample Log Output
Example from your system:
👉
Captured data includes:
IP Address
Username & Password
Timestamp
User-Agent

🔐 Key Security Concept
This project demonstrates deception-based security, where attackers are tricked into interacting with a fake system while their actions are monitored.

⚠️ Disclaimer
This project is for educational purposes only.
Do not deploy on public networks without authorization.
