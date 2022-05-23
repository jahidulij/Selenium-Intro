import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager

browser = "firefox"
# Setup browser
if browser == "chrome":
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
if browser == "firefox":
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
if browser == "edge":
    driver = webdriver.Ie(service=Service(IEDriverManager().install()))
else:
    print("Please provide the supported browser.")

# Go to the mentioned URL
base_url = "https://courses.letskodeit.com/practice"
driver.get(base_url)
# Maximize the window
driver.maximize_window()
# Pause for 2 seconds
time.sleep(2)

# Close the drivers
driver.close()
