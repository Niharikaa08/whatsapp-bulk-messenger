from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time


def load_contacts(path: str = "contacts.csv") -> pd.DataFrame:
    """
    Load contacts from a CSV file.

    Expected columns:
      - name  : contact name as saved in WhatsApp
      - phone : phone number with country code, kept as string
    """
    df = pd.read_csv(path, dtype={"phone": str})
    # Drop rows where name or phone is missing
    df = df.dropna(subset=["name", "phone"])
    return df


def load_message_template(path: str = "messages.txt") -> str:
    """
    Load the message template from a text file.

    The template can contain a {name} placeholder
    which will be replaced for each contact.
    """
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def create_driver() -> webdriver.Chrome:
    """
    Create and return a Chrome WebDriver instance
    using webdriver-manager so no manual driver
    download is needed.
    """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver


def open_whatsapp_and_login(driver: webdriver.Chrome) -> None:
    """
    Open WhatsApp Web and wait for the user to scan the QR code.
    """
    driver.get("https://web.whatsapp.com")
    print("📲 Open WhatsApp Web & scan the QR code.")
    input("Press Enter after scanning QR code and chats are visible...")


def send_message_to_contact(
    driver: webdriver.Chrome,
    name: str,
    phone: str,
    template: str,
    delay: float = 3.0,
) -> bool:
    """
    Search for a contact by name and send a personalized message.

    Returns True if message was sent successfully, False otherwise.
    """
    personal_msg = template.format(name=name)
    print(f"Sending to {name} ({phone})...")

    try:
        # Locate the search box at the top of the chat list
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
            )
        )

        # Clear previous search and type the contact name
        search_box.clear()
        search_box.send_keys(name)
        time.sleep(delay)

        # Open the first matching chat
        search_box.send_keys(Keys.ENTER)
        time.sleep(delay)

        # Locate the message input box at the bottom of the screen
        msg_box = driver.find_element(
            By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
        )

        # Type the personalized message and send it
        msg_box.send_keys(personal_msg + Keys.ENTER)
        time.sleep(2)

        print(f"✅ Message sent to {name}")
        return True

    except Exception as e:
        # Any failure (element not found, timeout, etc.) is logged here
        print(f"❌ Failed to send to {name}: {e}")
        return False


def main() -> None:
    """
    Main entry point for the WhatsApp bulk messenger.

    - Loads contacts and message template
    - Starts Chrome and logs into WhatsApp Web
    - Sends messages to each contact
    """
    contacts = load_contacts("contacts.csv")
    message_template = load_message_template("messages.txt")

    print("🚀 WhatsApp Bulk Messenger Starting...")
    print(f"📱 Contacts loaded: {len(contacts)}")

    driver = create_driver()
    open_whatsapp_and_login(driver)

    sent_count = 0

    for _, row in contacts.iterrows():
        name = row["name"]
        phone = row["phone"]

        success = send_message_to_contact(
            driver=driver,
            name=name,
            phone=phone,
            template=message_template,
            delay=3.0,
        )
        if success:
            sent_count += 1

        # Small delay between contacts to be more human-like
        time.sleep(3)

    print(f"🎉 Completed! {sent_count}/{len(contacts)} messages sent successfully")
    driver.quit()


if __name__ == "__main__":
    main()
