import time
import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Go to the mentioned URL
base_url = "https://www.programiz.com/python-programming"
driver.get(base_url)
# Maximize the window
driver.maximize_window()

# items = []
# last_height = driver.execute_script("return document.body.scrollHeight")
#
# item_target_count = 100
#
# while item_target_count > len(items):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(1)
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height
#
#     elements = driver.find_elements(By.XPATH, "//div[contains(text(),'Infinite Scroll Box 21')]")
#     textElements = []
#     for element in elements:
#         textElements.append(element.text)
#
#     items = textElements
#
# print(items)
# print(len(items))
#
# json.dump(items, open("items.json", "w"))
time.sleep(2)
# driver.execute_script("window.scrollBy(0, 500)")
contact = driver.find_element(By.XPATH, "//a[contains(text(),'Contact')]")
driver.execute_script("arguments[0].scrollIntoView()", contact)
time.sleep(2)
driver.close()
