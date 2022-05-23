import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Go to the mentioned URL
base_url = "https://courses.letskodeit.com/practice"
driver.get(base_url)
# Maximize the window
driver.maximize_window()
# Pause for 2 seconds
time.sleep(2)

# Close the drivers
driver.close()
