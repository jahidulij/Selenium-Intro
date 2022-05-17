import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Go to the mentioned URL
base_url = "https://courses.letskodeit.com/practice"
driver.get(base_url)
# Maximize the window
driver.maximize_window()
# Pause for 2 minutes
time.sleep(2)

actions = ActionChains(driver)

mouse = driver.find_element(By.ID, "mousehover")
top = driver.find_element(By.XPATH, "//a[contains(text(),'Top')]")
reload = driver.find_element(By.XPATH, "//a[contains(text(),'Reload')]")

actions.move_to_element(mouse).move_to_element(top).move_to_element(reload).click().perform()

time.sleep(5)
# Close the drivers
driver.close()
