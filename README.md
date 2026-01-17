# 🚍 Bus Seat Availability Alert System

A Python-based automation tool that continuously monitors bus seat availability on an online booking website and sends instant alerts through **WhatsApp**, **Email**, and **Mobile Push Notifications**.

This project solves the real-world problem of missing bus bookings due to fast seat sell-outs.

---

## 📌 Table of Contents
- Overview
- Features
- Tech Stack
- Project Structure
- Installation
- Configuration
  - Email (Gmail)
  - WhatsApp (Twilio)
  - Push Notifications (ntfy)
- Running the Project
- Cloud Deployment
- Use Case
- Resume Description
- Author

---

## 🔍 Overview

The Bus Seat Availability Alert System is an automation script that periodically checks seat availability for a specific bus route and date. Once seats become available, the system notifies the user immediately through multiple channels.

---

## ✨ Features

- Automated real-time seat monitoring
- WhatsApp alerts using Twilio API
- Email notifications via Gmail SMTP
- Mobile push notifications using ntfy
- Duplicate alert prevention
- Continuous background execution

---

## 🛠 Tech Stack

- **Programming Language:** Python  
- **Automation:** Selenium  
- **Notifications:** Twilio, Gmail SMTP, ntfy  
- **Tools:** WebDriver Manager, Requests  

---

## 📁 Project Structure

🔐 Configuration
📧 Email Notification (Gmail)

Enable 2-Step Verification in your Google account

Generate a 16-character App Password

Update the following variables in bus_alert.py:

GMAIL_USER = "your_email@gmail.com"
GMAIL_APP_PASSWORD = "your_16_character_app_password"
TO_EMAIL = "your_email@gmail.com"


⚠️ Do not use your regular Gmail password.

💬 WhatsApp Notification (Twilio)

Create a Twilio account at https://www.twilio.com

Activate the WhatsApp Sandbox

Get your Account SID and Auth Token

Update in bus_alert.py:

TWILIO_SID = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
TWILIO_TOKEN = "your_twilio_auth_token"
FROM_WHATSAPP = "whatsapp:+14155238886"
TO_WHATSAPP = "whatsapp:+91XXXXXXXXXX"

🔔 Push Notifications (ntfy)

Install the ntfy mobile app (Android / iOS)

Subscribe to a topic name (example):

bus-seat-alert-2026


Update in bus_alert.py:

NTFY_TOPIC = "bus-seat-alert-2026"

▶️ Running the Project
python bus_alert.py


The script checks seat availability every 2 minutes and sends alerts when seats are found.

☁️ Cloud Deployment (Optional)

This project can be deployed on cloud platforms like:

Railway

Render

PythonAnywhere

Cloud deployment enables 24/7 execution without keeping the local system active.
