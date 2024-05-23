# WhatsApp Broadcast Bot

The WhatsApp Broadcast Bot is a Python script that allows you to send messages to multiple WhatsApp contacts simultaneously using the WhatsApp Web interface. It reads contact details from a CSV file and automates the process of sending messages to each contact number.

## Features

- Reads contacts from a CSV file
- Sends messages to multiple WhatsApp contacts
- Sends messages at random intervals between 10 and 20 seconds
- Parses the message from the URL for better readability
- Uses Selenium WebDriver to automate the process

## Prerequisites

Before running the script, you need to ensure that you have the following prerequisites installed:

- Python 3.x
- Chrome browser
- ChromeDriver (compatible with your Chrome browser version)

## Installation

1. Clone the repository or download the script files.
2. Install the required Python packages by running the following command:
   pip install selenium
3. Download the compatible ChromeDriver for your Chrome browser version from the official website: https://sites.google.com/a/chromium.org/chromedriver/downloads
4. Extract the ChromeDriver and place it in the same directory as the script.

## Usage

1. Create a CSV file (e.g., `contacts.csv`) with the following format:
Name,PhoneNumber
John Doe,+1234567890
Jane Smith,+9876543210
2. Open the script and update the `csv_file` variable with the path to your CSV file.
3. Run the script using the following command:
python broadcast_bot.py
4. When prompted, scan the QR code in the WhatsApp Web interface to authenticate the session.
5. The script will start sending messages to the contacts in the CSV file at random intervals between 10 and 20 seconds.

## Configuration

You can customize the script by modifying the following variables:

- `message`: The message you want to send to the contacts.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The script uses the Selenium WebDriver for browser automation.
- The CSV file parsing is done using the built-in `csv` module.

