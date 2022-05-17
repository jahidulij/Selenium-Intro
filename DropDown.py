import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
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
# Get current url
current_url = driver.current_url
print("Current URL: " + current_url)

element = driver.find_element(By.ID, "carselect")
sel = Select(element)
# Select dropdown by value
benz = sel.select_by_value("benz")
# time.sleep(3)
# Select dropdown by visible text
honda = sel.select_by_visible_text("Honda")
# Select dropdown by index
bmw = sel.select_by_index(0)

# Get all the options
print(len(sel.options))
all_options = sel.options
for option in all_options:
    print(option.text)

time.sleep(3)
# Close the drivers
driver.close()
