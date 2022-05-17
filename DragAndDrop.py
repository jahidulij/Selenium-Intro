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
# Pause for 2 minutes
time.sleep(2)

actions = ActionChains(driver)
drag_me = driver.find_element(By.ID, "draggable")
drag_me_to = driver.find_element(By.ID, "droppable")

actions.drag_and_drop(drag_me, drag_me_to).perform()

time.sleep(5)
# Close the drivers
driver.close()
