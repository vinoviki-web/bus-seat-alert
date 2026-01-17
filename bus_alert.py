import requests
from twilio.rest import Client
import smtplib
from email.mime.text import MIMEText
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# --------- CONFIG ----------
URL = "https://www.rathimeena.in/search/harur-to-chennai?fromStationCode=ST5B8C201F&toStationCode=STF17D51&onwardDate=2026-01-19"
CHECK_INTERVAL = 120  # 2 minutes (120 seconds)

# ntfy.sh - Pick a unique topic name (subscribe to this in ntfy app)
NTFY_TOPIC = "ashokk-bus-harur-chennai-2026"

# Gmail Config
GMAIL_USER = "vinoviki2004@gmail.com"        # Your Gmail address
GMAIL_APP_PASSWORD = " "  # 16char App Password (not regular password)
TO_EMAIL = "vinoviki2004@gmail.com"           # Where to send alert (can be same)

# Twilio WhatsApp Config
TWILIO_SID = " "
TWILIO_TOKEN = " "
FROM_WHATSAPP = "whatsapp:+14155238886"   # Twilio sandbox number
TO_WHATSAPP = "whatsapp:+917418454875"    # Your number with country code

# ----------------------------

twilio_client = Client(TWILIO_SID, TWILIO_TOKEN)

# Setup Chrome in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check_bus():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    try:
        driver.get(URL)
        
        # Wait for bus cards to load (up to 15 seconds)
        try:
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, "trip-card"))
            )
        except:
            pass  # Continue even if timeout
        
        time.sleep(3)  # Extra wait for full render
        
        text = driver.page_source.lower()
        
        # Log for debugging
        print(f"Page loaded, length: {len(text)} chars")
        
        # Check for seat numbers (e.g., "27 seats", "33 seats") 
        seats_match = re.findall(r'>(\d+)\s*seats?<', text)
        if seats_match:
            total_seats = sum(int(s) for s in seats_match)
            return True, f"{total_seats} seats available across {len(seats_match)} bus(es)!"
        
        # Alternative: Check for "starts from" which indicates available bus
        if "starts from" in text and "sold out" not in text:
            return True, "Buses available with seats!"
        
        # Check if all buses are sold out
        sold_out_count = text.count("sold out")
        
        if sold_out_count > 0 and "starts from" not in text:
            return False, f"All {sold_out_count} bus(es) are sold out"
        
        if sold_out_count > 0 and "starts from" in text:
            return True, "Some seats may be available!"
        
        return False, "No trips found or still loading"
    finally:
        driver.quit()

def send_notification(msg):
    """Send push notification via ntfy.sh"""
    requests.post(f"https://ntfy.sh/{NTFY_TOPIC}", data=msg)

def send_email(msg):
    """Send email via Gmail"""
    email = MIMEText(msg)
    email["Subject"] = "🚍 Bus Alert - Harur to Chennai!"
    email["From"] = GMAIL_USER
    email["To"] = TO_EMAIL
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        server.sendmail(GMAIL_USER, TO_EMAIL, email.as_string())

def send_whatsapp(msg):
    """Send WhatsApp message via Twilio"""
    twilio_client.messages.create(
        body=msg,
        from_=FROM_WHATSAPP,
        to=TO_WHATSAPP
    )

def send_all_alerts(msg):
    """Send alert via all channels"""
    try:
        send_notification(msg)
        print("  ✓ ntfy notification sent")
    except Exception as e:
        print(f"  ✗ ntfy failed: {e}")
    
    try:
        send_email(msg)
        print("  ✓ Email sent")
    except Exception as e:
        print(f"  ✗ Email failed: {e}")
    
    try:
        send_whatsapp(msg)
        print("  ✓ WhatsApp sent")
    except Exception as e:
        print(f"  ✗ WhatsApp failed: {e}")

print("Bus watcher started...")
send_whatsapp("⏱️ Still checking for bus seats Harur → Chennai...")
while True:
    try:
        available, message = check_bus()
        
        if available:
            alert_msg = f"🚍 {message} Harur → Chennai on 21 Jan 2026. Check immediately!"
            send_all_alerts(alert_msg)
            print("Alert sent!", message)
            break
        else:
            print(f"No seats yet... ({message})")
    except Exception as e:
        print("Error:", e)

    time.sleep(CHECK_INTERVAL)

