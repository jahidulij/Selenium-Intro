import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.goibibo.com/")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH, "//div[@class='sc-jJoQJp iPfLQ']//p[@class='sc-dJjYzT cjzxWN fswWidgetTitle']").click()
all_dates = driver.find_elements(By.XPATH, "//div[@class='DayPicker-Day']//p[@class='fsw__date']")

done = driver.find_element(By.XPATH, "//span[@class='fswTrvl__done']")
for date_element in all_dates:
    date = date_element.text
    print(date)
    if date == '25':
        date_element.click()
        done.click()
        break

time.sleep(2)
driver.quit()
