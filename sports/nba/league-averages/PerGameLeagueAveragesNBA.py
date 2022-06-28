import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import numpy as np
import pandas as pd

browser = webdriver.Chrome("/Users/lukeh/Desktop/tmp/chromedriver")
browser.get("https://www.basketball-reference.com/leagues/NBA_stats_per_game.html")
time.sleep(1)

data = []

for i in range(82):

    # NOTE: Sometimes the attribute 'data-row' does not render, causing the script to fail. If this happens, just try again. :)

    row = browser.find_element_by_xpath(f".//tr[@data-row={i}]")
    if "thead" not in row.get_attribute('class'):
            cells = row.find_elements_by_tag_name("td")
            year = {}
            for cell in cells:
                if cell.text != "":
                    year[cell.get_attribute("data-stat")] = cell.text
                else:
                    year[cell.get_attribute("data-stat")] = "~ NO DATA ~"
            data.append(year)
            print("Data Collected: " + year['season'])


df = pd.DataFrame.from_dict(data)
df.to_csv("nba-per-game-league-averages.csv")


            

