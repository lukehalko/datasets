import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import numpy as np
import pandas as pd

browser = webdriver.Chrome("/Users/lukeh/Desktop/tmp/chromedriver")
browser.get("https://www.basketball-reference.com/leagues/")
time.sleep(1)

urls = []

for i in range(86):
    row = browser.find_element_by_xpath(f".//tr[@data-row={i}]")
    if "thead" not in row.get_attribute("class"):
        link = row.find_element_by_xpath(".//th[@data-stat='season']").find_element_by_tag_name("a").get_attribute("href")
        urls.append(link)




