import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Go to the mentioned URL
base_url = "https://www.adamchoi.co.uk/overs/detailed"
driver.get(base_url)
# Maximize the window
driver.maximize_window()
# Pause for 2 seconds
time.sleep(2)
# Get current url
current_url = driver.current_url
print("Current URL: " + current_url)
all_match_button = driver.find_element(By.XPATH, "//label[contains(text(),'All matches')]")
all_match_button.click()

country = Select(driver.find_element(By.ID, "country"))
country.select_by_visible_text("Spain")

time.sleep(3)

matches = driver.find_elements(By.TAG_NAME, "tr")

date = []
home_team = []
score = []
away_team = []

for match in matches:
    date.append(match.find_element(By.XPATH, './td[1]').text)
    home_team.append(match.find_element(By.XPATH, './td[2]').text)
    score.append(match.find_element(By.XPATH, './td[3]').text)
    away_team.append(match.find_element(By.XPATH, './td[4]').text)

time.sleep(2)
driver.quit()

df = pd.DataFrame({"date": date, "home_team": home_team, "score": score, "away_team": away_team})
df.to_csv("customiz ed_data.csv", index=False)
print(df)



