import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import numpy as np
import pandas as pd


browser = webdriver.Chrome('/Users/lukeh/Desktop/tmp/chromedriver')
browser.get("https://www.basketball-reference.com/leagues/NBA_2021_per_game.html")
time.sleep(1)

elem=browser.find_element_by_tag_name('body')

pagedowns=60

print('initialize while loop')

while pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    pagedowns-=1

print('***************while loop ended******************')

table = browser.find_elements_by_xpath(".//table[@id='per_game_stats']")
fullTable = table[0].find_elements_by_xpath(".//tr[@class='full_table']")
data=[]
print(fullTable[1].text.split(' '))

#for i in range(len(fullTable)-1): #TODO: This loop is for more thorough scrapinh
    #rank=fullTable[i].find_elements_by_xpath(".//td[@data-stat='ranker']")
    #name=fullTable[i].find_elements_by_xpath(".//td[@data-stat='player']")
    #data.append({name[0].text:{"rank":i}})

print(data)
for i in range(len(fullTable)): 
    arr=fullTable[i].text.split(' ')
    print(i)
    print(arr)
    if(len(arr)>=31):
        data.append({"Name":arr[1]+' '+arr[2], "Position":arr[3],
        "Age":arr[4],"Team":arr[5],"G":arr[6],"GS":arr[7],"MP":arr[8],"FG":arr[9],"FGA":arr[10],"FGPercent":arr[11],
        "ThreePt":arr[12],"ThreePtAttempts":arr[13],"ThreePtPercent":arr[14],"TwoPt":arr[15],"TwoPtAttempts":arr[16],"TwoPtPercent":arr[17],
        "eFGPercent":arr[18],"FT":arr[19],"FTA":arr[20],"FTPercent":arr[21],"ORB":arr[22],"DRB":arr[23],"TRB":arr[24],"AST":arr[25],"STL":arr[26],"BLK":arr[27],"TOV":arr[28],"PFouls":arr[29],"PTS":arr[30], "Rk":arr[0]})

#data.append({"Player":arr[1]+' '+arr[2], "POS":arr[3],"AGE":arr[4],"Team":arr[5],"G":arr[6],"GS":arr[7],"MP":arr[8],"FG":arr[9],"FGA":arr[10],"FG%":arr[11], "3P":arr[12],"3PA":arr[13],"3P%":arr[14],"2P":arr[15],"2PA":arr[16],"2PT%":arr[17], "eFG%":arr[18],"FT":arr[19],"FTA":arr[20],"FT%":arr[21],"ORB":arr[22],"DRB":arr[23],"TRB":arr[24],"AST":arr[25],"STL":arr[26],"BLK":arr[27],"TOV":arr[28],"PFouls":arr[29],"PTS":arr[30], "Rk":arr[0]})

df = pd.DataFrame.from_dict(data)
print(df)
df.to_csv('2020-2021-per-game-player.csv')
#"POS":0,"AGE":0,"G":0,"GS":0,"FG":0,"FGA":0,"FG%":0,"3P":0,"3PA":0,"3P%":0,"2P":0,"2PA":0,"2P%":0,"eFG%":0,"FT":0,"FTA":0,"FT%":0,"ORB":0,"DRB":0,"TRB":0