import time
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

col_names = []
try:
    browser = webdriver.Chrome("/Users/lukeh/DATA/lib/tmp/chromedriver")
    browser.get("https://www.basketball-reference.com/leagues/NBA_2022_per_game.html")
    time.sleep(1)

    fullTable = browser.find_elements_by_xpath(".//tr[@class='full_table']")
    firstRow = fullTable[0].find_elements_by_tag_name("td")

    for col in range(len(firstRow)):
        col_names.append(firstRow[col].get_attribute("data-stat"))

    cols = {}

    for name in col_names:
        cols[name] = []
        stat = browser.find_elements_by_xpath(f".//td[@data-stat='{name}']")
        for j in range(len(stat)):
            cols[name].append(stat[j].text)
            
        print(cols[name])

    data = pd.DataFrame.from_dict(cols)
    print(data)
    data.to_csv("player_per_game_2022.csv")
finally:
    browser.quit()



