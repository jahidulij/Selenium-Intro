import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.ID, "datepicker").click()
# driver.find_element(By.XPATH, "//a[text()=19]").click()
all_dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//a")

for date_element in all_dates:
    date = date_element.text
    print(date)
    if date == '25':
        date_element.click()
        break

time.sleep(2)
driver.quit()
