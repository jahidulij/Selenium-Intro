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

cur_window = driver.current_window_handle

# Pause for 2 minutes
time.sleep(2)
# Get current url
current_url = driver.current_url
print("Current URL: " + current_url)

# New tab
new_tab = driver.find_element(By.ID, "opentab").click()
handles = []
handles = driver.window_handles
for handle in handles:
    print(handle)
newHandle = handles[1]
driver.switch_to.window(newHandle)
print(driver.current_url)

# New window
# new_window = driver.find_element(By.ID, "openwindow").click()
# handles = []
# handles = driver.window_handles
# for handle in handles:
#     print(handle)
# newHandle = handles[1]
# driver.switch_to.window(newHandle)
# print(driver.current_url)

# Close the drivers
driver.close()
