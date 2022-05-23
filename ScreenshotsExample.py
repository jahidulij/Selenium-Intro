import time
from selenium import webdriver
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
alert_button = driver.find_element(By.ID, "alertbtn")

alert_button.screenshot(".\\element_screenshot.png")
# driver.save_screenshot(".\\visible_page_screenshot.png")
driver.get_screenshot_as_file("C:/Users/Asus/workspace_python/seleniumIntro/Screenshots/full_page_screenshot.jpg")

driver.close()
