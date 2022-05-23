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
driver.implicitly_wait(10)
# Pause for 2 seconds
time.sleep(2)
# Get current url
current_url = driver.current_url
print("Current URL: " + current_url)

element = driver.find_element(By.ID, "bmwradio")
# Check if radio button is selected
check_selected = element.is_selected()
# Print the value of the radio button
print("Before: " + str(check_selected))
if check_selected == True:
    print(element.text)
    pass
else:
    element.click()
    print(element.text)

check_selected = element.is_selected()
print("After: " + str(check_selected))

# List of radio buttons
radio_list = driver.find_elements(By.XPATH, "//input[contains(@type,'radio')]")

for i in radio_list:
    print(i.text)
    print(i)

time.sleep(3)
# Close the drivers
driver.close()
