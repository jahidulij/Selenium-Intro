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
# Pause for 2 seconds
time.sleep(2)
# Get current url
current_url = driver.current_url
print("Current URL: " + current_url)

# Get multi select list
multi_list = driver.find_element(By.ID, "multiple-select-example")
sel = Select(multi_list)
elements = sel.options

for element in elements:
    print(element.text)

# select all the elements
sel.select_by_index(1)
sel.select_by_visible_text("Apple")
sel.select_by_value("peach")


time.sleep(3)
# Close the drivers
driver.close()
