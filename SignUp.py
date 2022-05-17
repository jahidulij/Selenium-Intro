import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
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
# Click onk Sign Up link [Sign Up]
driver.find_element(By.XPATH, "//a[contains(text(),'Sign In')]").click()
driver.find_element(By.XPATH, "//a[contains(text(),'Sign Up')]").click()
driver.find_element(By.ID, "name").send_keys("Jahidul")
driver.find_element(By.ID, "last_name").send_keys("Islam")
driver.find_element(By.ID, "email").send_keys("jahidul.ij@gmail.com")
driver.find_element(By.ID, "password").send_keys("Therap321#")
driver.find_element(By.ID, "password_confirmation").send_keys("Therap321#")
driver.find_element(By.XPATH, "//input[@value='Sign Up']").click()


# Close the drivers
driver.close()
