import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

driver.find_element(By.XPATH, "//a[contains(text(),'Sign In')]").click()
driver.find_element(By.ID, "email").send_keys("jahidul.ij@gmail.com")
driver.find_element(By.ID, "password").send_keys("Therap321")
driver.find_element(By.XPATH, "//input[@value='Login']").click()

# Sign In verification
if driver.title == "My Courses":
    print("Login successful")
else:
    print("Login Unsuccessful")
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='dynamic-text help-block']"))
    )
    print(element.text)


# Close the drivers
driver.close()
