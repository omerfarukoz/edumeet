from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from selenium.webdriver.chrome.options import Options
import random
import time
import json

# Load configuration from JSON file
with open("config.json") as config_file:
    config = json.load(config_file)

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--use-fake-ui-for-media-stream")
chrome_options.add_argument("--use-fake-device-for-media-stream")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--allow-file-access-from-files")
chrome_options.add_argument("--allow-running-insecure-content")
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--mute-audio=false")
chrome_options.add_argument("--autoplay-policy=no-user-gesture-required")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--use-file-for-fake-audio-capture=/root/edumeet/media/siren.wav")
chrome_options.add_experimental_option(
    "prefs",
    {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 1,
        "profile.default_content_setting_values.notifications": 1,
    },
)
service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=chrome_options)
# Start user session



# Open a new page for each bot
browser.get(config["url"])
time.sleep(2)  # Adjust the sleep time as needed for loading

# Find the username text field
textfield = browser.find_element(By.CSS_SELECTOR, 'div.premeeting-screen > div > div> div > div > div > div > input')

# Clear the text field
textfield.clear()

# Type bot name
if config["userandomnames"]:
    textfield.send_keys(random_name)
else:
    textfield.send_keys(config["customname"])

# Join Meeting
join_button = browser.find_element(By.CSS_SELECTOR, 'div[data-testid="prejoin.joinMeeting"]')
join_button.click()
# /usr/share/jitsi-meet
if config["haspassword"]:
    time.sleep(1)
    password_input = browser.find_element(By.CSS_SELECTOR, 'input')
    password_input.send_keys(config["password"])
    password_input.send_keys("\n")  # Press Enter
time.sleep(5)
browser.save_screenshot('screenshot.png')
while True:
    video_element = browser.find_element(By.XPATH, "//*[contains(@id, 'largeVideo')]")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"video_element_screenshot_{timestamp}.png"
    video_element.screenshot("resim/" + filename)
    print(f"Screenshot saved as '{filename}'.")

# Close the browser (if you want it to stay open, comment this out)
# browser.quit()
