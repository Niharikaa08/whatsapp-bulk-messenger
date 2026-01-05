# WhatsApp Bulk Messenger (Python + Selenium)

Automates sending personalized WhatsApp messages to multiple contacts using WhatsApp Web.  

## Features

- Reads contacts (name, phone) from `contacts.csv`
- Uses `messages.txt` with `{name}` placeholder for personalization
- Automates WhatsApp Web in Google Chrome using Selenium
- Modular functions for cleaner, testable code
- Basic logging of success/failure for each contact

## How It Works

- `load_contacts()`  
  Reads `contacts.csv` into a pandas DataFrame, keeping `phone` as a string and dropping empty rows.

- `load_message_template()`  
  Loads the message template from `messages.txt` and returns it as a string. The template can contain `{name}`.

- `create_driver()`  
  Uses `webdriver-manager` to download and start the correct ChromeDriver automatically.

- `open_whatsapp_and_login()`  
  Opens `https://web.whatsapp.com` and waits for the user to scan the QR code before continuing.

- `send_message_to_contact()`  
  Searches for a contact by name, opens the chat, and sends a personalized message built from the template.

- `main()`  
  Orchestrates the full flow: load data, start driver, login, loop through contacts, send messages, and close the browser.

## Project Structure

```text
whatsapp-bulk-messenger/
├── bulk_sender.py      # Main automation script with modular functions
├── contacts.csv        # List of contacts (name, phone)
├── messages.txt        # Message template with {name} placeholder
└── README.md           # Project documentation
```

## Setup

1. Clone or download this repository.
2. Install Python 3 if not already installed.
3. Install required packages:

   ```bash
   python -m pip install selenium pandas webdriver-manager
   ```

4. Make sure Google Chrome is installed on your system and you can open WhatsApp Web manually.

## Preparing Contacts and Message

1. Edit `contacts.csv` and add your contacts in this format:

   ```csv
   name,phone
   TestUser,+91XXXXXXXXXX
   ExampleContact,+91YYYYYYYYYY
   ```

   - `phone` must include the country code and no spaces.
   - `name` should match how the contact is saved in WhatsApp.

2. Edit `messages.txt` and write your message template, for example:

   ```text
   Hi {name}! This is a test message sent automatically using my Python WhatsApp Bulk Messenger project.
   ```

## How to Run

1. Open a terminal in the project folder.
2. Run the script:

   ```bash
   python bulk_sender.py
   ```

3. Chrome will open WhatsApp Web.
4. Scan the QR code with your phone and wait for your chats to load.
5. Go back to the terminal and press **Enter** when asked.
6. The script will:
   - Search for each contact by name
   - Open the chat
   - Send the personalized message
   - Print status for each contact (success or failure)

## Changelog

- **2026-01-05**  
  - Refactored script into modular functions (`load_contacts`, `load_message_template`, `create_driver`, `open_whatsapp_and_login`, `send_message_to_contact`, `main`).  
  - Improved code readability and added inline comments.

## Author
Niharikaa Khandelwal

