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
# Pause for 2 minutes
time.sleep(2)
# Get current url
current_url = driver.current_url
print("Current URL: " + current_url)

elements = driver.find_elements(By.XPATH, "//input[@type='checkbox' and @name='cars']")
print(len(elements))
# Get the checkbox list
for element in elements:
    print(element.text)
# Click on the checkboxes
for element in elements:
    if element.is_selected() == True:
        print(element.text)
        continue
    else:
        element.click()
        print(element.text)



time.sleep(3)
# Close the drivers
driver.close()
