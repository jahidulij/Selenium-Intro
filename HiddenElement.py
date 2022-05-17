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

hide = driver.find_element(By.ID, "hide-textbox")
show = driver.find_element(By.ID, "show-textbox")

element = driver.find_element(By.ID, "displayed-text")
hide.click()
present = element.is_displayed()


if present == True:
    element.send_keys("Hello!")
    hide.click()
else:
    show.click()
    element.send_keys("Hi!!!")


time.sleep(3)
# Close the drivers
driver.close()
