# bus-seat-alert
# 🚍 Bus Seat Availability Alert System

A Python-based automation system that continuously monitors bus seat availability on a booking website and sends instant alerts via **WhatsApp (Twilio)**, **Email (Gmail SMTP)**, and **Mobile Push Notifications (ntfy)**.

This project is designed to help users avoid missing bus tickets when seats sell out quickly.

---

## ✨ Features

- 🔄 Automated seat availability monitoring
- 📲 WhatsApp notifications using Twilio
- 📧 Email alerts using Gmail SMTP
- 🔔 Mobile push notifications using ntfy
- 🚫 Duplicate alert prevention
- 🕒 Runs continuously until seats are available

---

## 🛠 Tech Stack

- Python
- Selenium
- WebDriver Manager
- Twilio API
- Gmail SMTP
- ntfy.sh

---

## 📁 Project Structure


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/vinoviki-web/bus-seat-alert.git
cd bus-seat-alert

pip install -r requirements.txt
Configuration Guide
📧 Email Notification Setup (Gmail)

Enable 2-Step Verification in your Google Account

Generate a 16-character App Password

Update these variables in bus_alert.py:
GMAIL_USER = "your_email@gmail.com"
GMAIL_APP_PASSWORD = "your_16_character_app_password"
TO_EMAIL = "your_email@gmail.com"
TWILIO_SID = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
TWILIO_TOKEN = "your_twilio_auth_token"
FROM_WHATSAPP = "whatsapp:+14155238886"
TO_WHATSAPP = "whatsapp:+91XXXXXXXXXX"
🔔 Push Notification Setup (ntfy)

Install ntfy app (Android / iOS)

Subscribe to a topic name (example):

bus-seat-alert-2026


Update in bus_alert.py:

NTFY_TOPIC = "bus-seat-alert-2026"


You will now receive instant mobile notifications.

▶️ Running the Project
python bus_alert.py


The script will:

Check seat availability every 2 minutes

Send alerts when seats are found

Stop automatically after sending alerts

☁️ Cloud Deployment (Optional)

This project can be deployed on cloud platforms such as:

Railway

Render

PythonAnywhere

Cloud deployment allows 24/7 monitoring without keeping your laptop ON.

🧠 Use Case

This system is useful for users who frequently miss bus bookings due to high demand and need real-time automated alerts.



