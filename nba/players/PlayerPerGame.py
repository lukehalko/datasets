import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import numpy as np
import pandas as pd

browser = webdriver.Chrome("/Users/lukeh/Desktop/tmp/chromedriver")
browser.get("https://www.basketball-reference.com/leagues/")
time.sleep(1)

urls = []
seasons = []

for i in range(86):
    row = browser.find_element_by_xpath(f".//tr[@data-row={i}]")
    if "thead" not in row.get_attribute("class"):
        link = row.find_element_by_xpath(".//th[@data-stat='season']").find_element_by_tag_name("a").get_attribute("href")
        season = row.find_element_by_xpath(".//th[@data-stat='season']").text
        #Cut .html off the end for now
        newLink = link.replace(".html", "")

        urls.append(newLink + "_per_game.html")
        seasons.append(season)


for i in range(len(urls)):
    data = []
    browser.get(urls[i])
    time.sleep(0.5)
    rows = browser.find_elements_by_xpath(".//tr[@class='full_table']")
    for row in rows:
        player = {}
        cells = row.find_elements_by_tag_name("td")
        for cell in cells:
            player[cell.get_attribute("data-stat")] = cell.text
        data.append(player)
        print("player collected: " + player['player'])
    df = pd.DataFrame.from_dict(data)
    df.to_csv(f"{seasons[i]}-per-game-player.csv")
    print(f"{seasons[i]} season collected")





