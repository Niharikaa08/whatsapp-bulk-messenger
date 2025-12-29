from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

# Read contacts
df = pd.read_csv('contacts.csv', dtype={'phone': str})
message = open('messages.txt', 'r').read()

print("🚀 WhatsApp Bulk Messenger Starting...")
print(f"📱 Contacts loaded: {len(df)}")
print("📲 Open WhatsApp Web & Scan QR first!")

# Setup Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://web.whatsapp.com")
input("Press Enter after scanning QR code...")

sent_count = 0
for index, row in df.iterrows():
    name = row['name']
    phone = row['phone']
    personal_msg = message.format(name=name)

    print(f"Sending to {name} ({phone})...")

    try:
        search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')))
        search_box.clear()
        search_box.send_keys(name)
        time.sleep(3)
        search_box.send_keys(Keys.ENTER)
        time.sleep(3)

        msg_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        msg_box.send_keys(personal_msg + Keys.ENTER)
        time.sleep(2)

        print(f"✅ Message sent to {name}")
    except Exception as e:
        print(f"❌ Failed to send to {name}: {e}")

    time.sleep(3)

print(f"🎉 Completed! {sent_count}/{len(df)} messages sent successfully")

driver.quit()
