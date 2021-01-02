from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import datetime

chromeOptions = webdriver.ChromeOptions()
preferences = {"download.default_directory" : "E:\\2nd Year\\DataScience_2019501107\\DADV\\finalexam\\day"}
chromeOptions.add_experimental_option("prefs", preferences)
chromedriver = "E:\\2nd Year\\DataScience_2019501107\\DADV\\finalexam\\chromedriver.exe"
browser = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)
browser.maximize_window()

url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
browser.get(url)
time.sleep(2)

Companies_list = []
for i in range(1, 60):
	p = browser.find_element_by_xpath('//*[@id="constituents"]/tbody/tr['+str(i)+']/td[1]/a')
	Companies_list.append(p.text)
# print(len(Companies_list))
# print(Companies_list)

time.sleep(4)

#Time Conversion
Start_date = datetime.datetime(2018, 4, 8)
End_date = datetime.datetime(2021, 1, 2)
from_date = int(time.mktime(Start_date.timetuple()))
to_date = int(time.mktime(End_date.timetuple()))
print(from_date)
print(to_date)

for each in Companies_list:
    browser.get("https://finance.yahoo.com/quote/"+each+"/history?period1="+str(from_date)+"&period2="+str(to_date)+"&interval=1d&filter=history&frequency=1d")
    browser.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a/span').click()
    time.sleep(3)

chromeOptions = webdriver.ChromeOptions()
preferences2 = {"download.default_directory" : "E:\\2nd Year\\DataScience_2019501107\\DADV\\finalexam\\week"}
chromeOptions.add_experimental_option("prefs", preferences2)
chromedriver2 = "E:\\2nd Year\\DataScience_2019501107\\DADV\\finalexam\\chromedriver.exe"
browser = webdriver.Chrome(executable_path=chromedriver2, options = chromeOptions)

for each in Companies_list:
    browser.get("https://finance.yahoo.com/quote/"+each+"/history?period1="+str(from_date)+"&period2="+str(to_date)+"&interval=1d&filter=history&frequency=1wk")
    browser.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a/span').click()
    time.sleep(3)

chromeOptions = webdriver.ChromeOptions()
preferences3 = {"download.default_directory" : "E:\\2nd Year\\DataScience_2019501107\\DADV\\finalexam\\month"}
chromeOptions.add_experimental_option("prefs", preferences3)
chromedriver3 = "E:\\2nd Year\\DataScience_2019501107\\DADV\\finalexam\\chromedriver.exe"
browser = webdriver.Chrome(executable_path=chromedriver3, options = chromeOptions)

for each in Companies_list:
    browser.get("https://finance.yahoo.com/quote/"+each+"/history?period1="+str(from_date)+"&period2="+str(to_date)+"&interval=1d&filter=history&frequency=1mo")
    browser.find_element_by_xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a/span').click()
    time.sleep(3)