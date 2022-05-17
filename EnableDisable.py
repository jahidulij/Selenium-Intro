import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Go to the mentioned URL
base_url = "https://courses.letskodeit.com/practice"
driver.get(base_url)
# Maximize the window
driver.maximize_window()
# Pause for 2 minutes
time.sleep(2)

enable_element = driver.find_element(By.ID, "enabled-button")
disable_element = driver.find_element(By.ID, "disabled-button")

element = driver.find_element(By.ID, "enabled-example-input")

disable_element.click()
print(element.is_enabled())

if element.is_enabled() == True:
    element.send_keys("I'm going to disable it right now.")
    time.sleep(2)
    disable_element.click()
    print(element.is_enabled())
else:
    enable_element.click()
    print(element.is_enabled())
    element.send_keys("I'm enable now.")



time.sleep(3)
# Close the drivers
driver.close()
