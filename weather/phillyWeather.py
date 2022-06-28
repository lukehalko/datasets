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
    # "time": [],
    "temp": [],
    "weather": [],
    "wind": [],
    "humidity": [],
    "barometer": [],
    "visibility": []
}
try:
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    for year in range(2016, 2017):
        for month in range(1, 2):
            print("entering new month")
            browser.get(f"https://www.timeanddate.com/weather/usa/philadelphia/historic?month={month}&year={year}")

            links = browser.find_elements(By.XPATH, "//div[@class='weatherLinks']")[1]
            for day in range(1,32):
                try:
                    print(f"clicking {months[month-1]} {day}")
                    try:
                        links.find_element(By.PARTIAL_LINK_TEXT, f"{months[month-1]} {day}").click()
                        print("got links")
                    except Exception as e:
                        print(e)
                        print("ERROR GETTING LINKS, TRYING AGAIN...")
                        links.find_element(By.PARTIAL_LINK_TEXT, f"{months[month-1]} {day}").click()
                    try:
                        rows = browser.find_element(By.XPATH, "//table[@id='wt-his']").find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr")
                        print("got rows")
                    except Exception as e:
                        print(e)
                        print("ERROR GETTING ROWS, TRYING AGAIN...")
                        time.sleep(1)
                        rows = browser.find_element(By.XPATH, "//table[@id='wt-his']").find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr")
                    for row in rows:
                        data["date"].append(f"{month}-{day}-{year}")
                        for i in range(1,5):
                            try:
                                #timestamp = row.find_element(By.TAG_NAME, "th").text
                                x = 1
                                break
                            except Exception as e:
                                print(e)
                                print("ERROR GETTING TIME (th) ELEMENT, TRYING AGAIN...")
                                time.sleep(1)
                                # data["time"].append(row.find_element(By.TAG_NAME, "th").text)
                        for i in range(1,5):
                            try:
                                values = row.find_elements(By.TAG_NAME, "td")
                            except Exception as e:
                                print(e)
                                print("ERROR GETTING ROW VALUES, TRYING AGAIN...")
                                time.sleep(1)
                        # data["time"] = timestamp
                        data["temp"].append(values[1].text)
                        data["weather"].append(values[2].text)
                        data["wind"].append(values[3].text)
                        data["humidity"].append(values[5].text)
                        data["barometer"].append(values[6].text)
                        data["visibility"].append(values[7].text)   
                
                    print(f"Successfully collected for {months[month-1]} {day}")
                except Exception as e:
                    print(e)

    # df = pd.DataFrame.from_dict(data)
    # print(df)

    # df.to_csv("philadelphia_weather_2016_2022")
    print(data)
    for x in data:
        print(x + " " + str(len(data[x])))
finally:
    try:
        df = pd.DataFrame.from_dict(data)
        df.to_csv("philadelphia_weather_2016_2022")
    except Exception as e:
        print(e)
    browser.quit()
