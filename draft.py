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
# Pause for 2 seconds
time.sleep(2)
# Get current url
current_url = driver.current_url
print("Current URL: " + current_url)
# Click onk Sign Up link [Sign Up]
# driver.find_element(By.XPATH, "//a[contains(text(),'Sign In')]").click()
# driver.find_element(By.XPATH, "//a[contains(text(),'Sign Up')]").click()
# Provide value on the text field
# driver.find_element(By.ID, "name").send_keys("Jahidul")
# driver.find_element(By.ID, "last_name").send_keys("Islam")
# driver.find_element(By.ID, "email").send_keys("jahidul.ij@gmail.com")
# driver.find_element(By.ID, "password").send_keys("Therap321#")
# driver.find_element(By.ID, "password_confirmation").send_keys("Therap321#")
# driver.find_element(By.XPATH, "//input[@value='Sign Up']").click()
# Sign In

# driver.find_element(By.XPATH, "//a[contains(text(),'Sign In')]").click()
# driver.find_element(By.ID, "email").send_keys("jahidul.ij@gmail.com")
# driver.find_element(By.ID, "password").send_keys("Therap321")
# driver.find_element(By.XPATH, "//input[@value='Login']").click()
#
# # Sign In verification
# if driver.title == "My Courses":
#     print("Login successful")
# else:
#     print("Login Unsuccessful")
#
# driver.implicitly_wait(5)
# msg = driver.find_element(By.XPATH, "//span[@class='dynamic-text help-block']")
# print(msg.text)

# Find radio buttons of the pages
rdo_fields = driver.find_elements(By.XPATH, "//input[@type='radio']")
print(len(rdo_fields))
for i in rdo_fields:
    print(rdo_fields[i])

# Close the drivers
driver.close()
