from selenium import webdriver
from selenium.webdriver.support.select import Select

qspiders=webdriver.Chrome(executable_path=("C:/Users/Rakshith Yenadka/Downloads/chromedriver_win32/chromedriver.exe"))
qspiders.get("http://www.facebook.com")
test=Select(qspiders.find_element_by_name("birthday_day"))
test.select_by_value("20")
test=Select(qspiders.find_element_by_name("birthday_month"))
test.select_by_value("11")
test=Select(qspiders.find_element_by_name("birthday_year"))
test.select_by_value("2016")