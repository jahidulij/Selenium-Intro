import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# Setup Chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Go to the mentioned URL
base_url = "https://www.atlantisitgroup.com/home"
driver.get(base_url)
# Maximize the window
driver.maximize_window()
driver.implicitly_wait(5)
careers = driver.find_element(By.XPATH, "//a[contains(text(),'Careers')]")
driver.execute_script("arguments[0].scrollIntoView()", careers)
time.sleep(2)
careers.click()
# elements = driver.find_elements(By.XPATH, "//h4[contains(text(),'')]")
#
# for element in elements:
#     print(element.text)

time.sleep(2)
