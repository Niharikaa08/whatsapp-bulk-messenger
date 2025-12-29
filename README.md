# WhatsApp Bulk Messenger (Python + Selenium)

Automates sending personalized WhatsApp messages to multiple contacts using WhatsApp Web. This project is built for learning browser automation and showcasing Python skills on a resume.

## Features
- Reads contacts (name, phone) from `contacts.csv`
- Uses `message.txt` with `{name}` placeholder for personalized messages
- Opens WhatsApp Web in Chrome and sends messages automatically
- Adds small delays between messages to reduce risk of temporary blocking
- Logs success/failure for each contact in the terminal

## Tech Stack
- Python 3
- Selenium
- pandas
- webdriver-manager
- Google Chrome + ChromeDriver

## Project Structure
whatsapp-bulk-messenger/
├── bulk_sender.py # Main automation script
├── contacts.csv # List of contacts (name, phone)
├── message.txt # Message template with {name} placeholder
└── README.md # Project documentation


## Setup

1. Clone or download this repository.
2. Install the required Python packages: python -m pip install selenium pandas webdriver-manager
3. Make sure Google Chrome is installed on your system.

## Preparing Contacts and Message
1. Edit `contacts.csv` and add your contacts in this format: 
name,phone
TestUser,+91XXXXXXXXXX
ExampleContact,+91YYYYYYYYYY
- `phone` must include the country code and no spaces.
2. Edit `message.txt` and write your message template, for example:
Hi everyone ! This is a test message sent automatically using my Python WhatsApp Bulk Messenger project.

## How to Run

1. Open a terminal in the project folder.
2. Run the script: python bulk_sender.py
3. Chrome will open WhatsApp Web.
4. Scan the QR code with your phone to log in.
5. Go back to the terminal and press **Enter** when asked.
6. The script will:
- Search each phone number
- Open the chat
- Send the personalized message
- Print status for each contact

## Notes

- Use this tool only with contacts who have agreed to receive messages.
- Do not use it for spam or violating WhatsApp Terms of Service.
- This project is created for educational purposes and portfolio building.

## Author
Niharikaa Khandelwal


