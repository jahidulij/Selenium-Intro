import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Go to the mentioned URL
base_url = "https://www.worldometers.info/"
driver.get(base_url)
# Maximize the window
driver.maximize_window()
# Pause for 2 seconds
time.sleep(2)
# Get current url
current_url = driver.current_url
print("Current URL: " + current_url)

title1 = driver.find_element(By.XPATH, "//div[contains(text(),'World Population')]")
print(title1.text)

title2 = driver.find_element(By.XPATH, "//a[contains(text(),'Current World Population')]")
item_values = driver.find_elements(By.XPATH, "//span[@class='counter-item']")
item_counts = driver.find_elements(By.XPATH, "//span[@class='counter-number']")

contact = driver.find_element(By.XPATH, "//a[contains(text(),'contact')]")
driver.execute_script("arguments[0].scrollIntoView()", contact)
time.sleep(5)



# Close the drivers
driver.close()
