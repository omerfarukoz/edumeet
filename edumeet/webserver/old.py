from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options for headless mode
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
options.add_argument("--ignore-certificate-errors")  # Ignore certificate errors
options.add_argument("--allow-insecure-localhost")
# Create a service for ChromeDriver
service = Service(ChromeDriverManager().install())

# Start the Chrome browser in headless mode
driver = webdriver.Chrome(service=service, options=options)

# Example: Navigate to a website
driver.get("https://meet.edumeet.tech/selamknk")

# Print the title of the page
print(driver.title)
driver.save_screenshot('screenshot.png')
# Close the browser
driver.quit()
