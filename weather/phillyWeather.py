import numpy
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

start_year = 2016
end_year = 2021
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

data = {
    "date": [],
    "time": [],
    "temp": [],
    "weather": [],
    "wind": [],
    "humidity": [],
    "barometer": [],
    "visibility": []
}
try:
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    for year in range(2016, 2022):
        for month in range(1, 13):
            print("entering new month")
            browser.get(f"https://www.timeanddate.com/weather/usa/philadelphia/historic?month={month}&year={year}")

            links = browser.find_elements(By.XPATH, "//div[@class='weatherLinks']")[1]
            for day in range(1,32):
                try:
                    print(f"clicking {months[month-1]} {day}")
                    links.find_element(By.PARTIAL_LINK_TEXT, f"{months[month-1]} {day}").click()
                    time.sleep(1)
                    print("got links")
                    rows = browser.find_element(By.XPATH, "//table[@id='wt-his']").find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr")
                    print("got rows")
                    for row in rows:
                        data["date"].append(f"{month}-{day}-{year}")
                        data["time"].append(row.find_element(By.TAG_NAME, "th").text)
                        values = row.find_elements(By.TAG_NAME, "td")
                        data["temp"].append(values[1].text)
                        data["weather"].append(values[2].text)
                        data["wind"].append(values[3].text)
                        data["humidity"].append(values[5].text)
                        data["barometer"].append(values[6].text)
                        data["visibility"].append(values[7].text)   
                
                    print(f"Successfully collected for {months[month-1]} {day}")
                except Exception as e:
                    print(e)
    print(data)
    for x in data:
        print(x + " " + str(len(data[x])))
finally:
    try:
        df = pd.DataFrame.from_dict(data)
        df.to_csv("philadelphia_weather_2016_2021.csv")
    except Exception as e:
        print(e)
        print("*** FAILED TO GENERATE CSV FILE ***")
    browser.quit()