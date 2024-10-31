from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait for the raise hands button to be clickable
wait = WebDriverWait(browser, 10)  # 10 seconds timeout
raise_hands_button = wait.until(EC.element_to_be_clickable((By.XPATH, 'your_xpath_here')))
raise_hands_button.click()



'--use-fake-ui-for-media-stream',
    '--use-fake-device-for-media-stream',