import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import numpy as np
import pandas as pd

browser = webdriver.Chrome("/Users/lukeh/Desktop/tmp/chromedriver")
browser.get("https://www.basketball-reference.com/leagues/")
time.sleep(1)

tbody = browser.find_element_by_xpath(".//table[@id='stats']").find_element_by_tag_name("tbody")

