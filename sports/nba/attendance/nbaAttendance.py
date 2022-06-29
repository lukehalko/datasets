import numpy
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_text(e):
    return e.text

url = "https://www.basketball-reference.com/leagues/NBA_"
start_year = 2018
end_year = 2022
data = {
    "date":[],
    "start_time":[],
    "away_team":[],
    "away_pts":[],
    "home_team":[],
    "home_pts":[],
    "attendance":[],
    "stadium":[]
}

try:
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    for year in range(start_year, end_year + 1):
        print(f"Entering {year-1}-{year} season")
        months =[]
        browser.get(url + str(year) + "_games.html")
        time.sleep(1)

        links = browser.find_element(By.XPATH, "//div[@class='filter']").find_elements(By.TAG_NAME, "a")
        
        for link in links:
            months.append(link.get_attribute("href"))
        
        for month in months:
            browser.get(month)
            print("navigated to new page")
            time.sleep(1)

            # pull each column from the page and store it in a variable
            table = browser.find_element(By.XPATH, "//table[@id='schedule']").find_element(By.TAG_NAME, "tbody")
            dates = table.find_elements(By.XPATH, "//th[@data-stat='date_game'][@scope='row']")
            times = table.find_elements(By.XPATH, "//td[@data-stat='game_start_time']")
            away_tms = table.find_elements(By.XPATH, "//td[@data-stat='visitor_team_name']")
            away_pts = table.find_elements(By.XPATH, "//td[@data-stat='visitor_pts']")
            home_tms = table.find_elements(By.XPATH, "//td[@data-stat='home_team_name']")
            home_pts = table.find_elements(By.XPATH, "//td[@data-stat='home_pts']")
            attendance = table.find_elements(By.XPATH, "//td[@data-stat='attendance']")
            stadiums = table.find_elements(By.XPATH, "//td[@data-stat='arena_name']")

            # add each column to a dictionary
            data["date"] = data["date"] + list(map(get_text, dates))
            data["start_time"] = data["start_time"] + list(map(get_text, times))
            data["away_team"] = data["away_team"] + list(map(get_text, away_tms))
            data["away_pts"] = data["away_pts"] + list(map(get_text, away_pts))
            data["home_team"] = data["home_team"] + list(map(get_text, home_tms))
            data["home_pts"] = data["home_pts"] + list(map(get_text, home_pts))
            data["attendance"] = data["attendance"] + list(map(get_text,attendance))
            data["stadium"] = data["stadium"] + list(map(get_text, stadiums))

            print(f"Collected data for {month}")

    df = pd.DataFrame.from_dict(data)
    df.to_csv("nba_attendance_2017_2022.csv")

finally:
    browser.quit()