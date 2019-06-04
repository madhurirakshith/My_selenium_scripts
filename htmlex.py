from selenium import webdriver
from selenium.webdriver.common.keys import Keys
qspiders=webdriver.Chrome(executable_path=("C:/Users/Rakshith Yenadka/Downloads/chromedriver_win32/chromedriver.exe"))
qspiders.get("file:///D:/login.html")
qspiders.find_element_by_id('12334').send_keys("abc@gmail.com")
qspiders.find_element_by_id('334').send_keys("pass@123")
qspiders.find_element_by_id('123').click()
