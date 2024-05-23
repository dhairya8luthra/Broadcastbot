import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from urllib.parse import quote
# Load the CSV file
csv_file = 'contacts.csv'  # Update with your CSV file path
contacts = []
with open(csv_file, newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        contacts.append({'number': row[1], 'name': row[0]})

# Initialize the WebDriver
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
ser = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=ser,options=chrome_options)

# Open WhatsApp Web
driver.get('https://web.whatsapp.com')
input("Press Enter after scanning QR code")  # Wait for user to scan the QR code
successful_attempts = 0
failed_attempts = 0
for contact in contacts:
    number = contact['number']
    message = """
Hello, I am a bot. I am sending you this message to inform you that I am currently testing a WhatsApp broadcast bot. Please ignore this message. Thank you.
"""
    message = quote(message)

    # Create the WhatsApp URL for the specific number
    url = f"https://web.whatsapp.com/send?phone={number}&text={message}"
    driver.get(url)
    random_interval = random.randint(10, 20)
    time.sleep(10)
    try:
        # Wait for the message input box to be present
        input_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]'))
        )
        input_box.send_keys(Keys.ENTER)
        
        time.sleep(random_interval)
        print(f"Sent {number}:  waiting for {random_interval} seconds")
        successful_attempts+=1
        print("no of successful attempts: ",successful_attempts)
        print("no of failed attempts: ",failed_attempts)
    except Exception as e:
        try:
            driver.get(url)
            input_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]'))
            )
            input_box.send_keys(Keys.ENTER)
            
            time.sleep(random_interval)
            print(f"Sent {number}:  waiting for {random_interval} seconds")
            successful_attempts+=1
            print("no of successful attempts: ",successful_attempts)
            print("no of failed attempts: ",failed_attempts)
        except Exception as e:
            print(f"Failed to send message to {number}: {e}")
            failed_attempts+=1
            print("no of successful attempts: ",successful_attempts)
            print("no of failed attempts: ",failed_attempts)

    time.sleep(5)  # Wait a few seconds before sending the next message


# Close the WebDriver
driver.quit()