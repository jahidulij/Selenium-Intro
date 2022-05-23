import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Go to the mentioned URL
base_url = "https://testautomationpractice.blogspot.com/"
driver.get(base_url)
# Maximize the window
driver.maximize_window()
# Pause for 2 seconds
time.sleep(2)

copy_text = driver.find_element(By.XPATH, "//button[contains(text(),'Copy Text')]")

actions = ActionChains(driver)
actions.double_click(copy_text).perform()

time.sleep(5)
# Close the drivers
driver.close()
