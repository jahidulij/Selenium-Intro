import time
import pandas as pd
from selenium import webdriver
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

matches = driver.find_elements(By.TAG_NAME, "tr")

date = []
home_team = []
score = []
away_team = []

for match in matches:
    d = match.find_element(By.XPATH, './td[1]').text
    date.append(d)
    home = match.find_element(By.XPATH, './td[2]').text
    home_team.append(home)
    s = match.find_element(By.XPATH, './td[3]').text
    score.append(s)
    a = match.find_element(By.XPATH, './td[4]').text
    away_team.append(a)
    # print(d + " | " + home + " | " + s + " | " + a)

time.sleep(2)
driver.quit()

df = pd.DataFrame({"Date": date, "Home Team": home_team, "Score": score, "Away Team": away_team})
df.to_csv("football_data.csv", index=False)
print(df)



