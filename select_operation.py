from selenium import webdriver
from selenium.webdriver.support import select

qspiders=webdriver.Chrome(executable_path=("C:/Users/Rakshith Yenadka/Downloads/chromedriver_win32/chromedriver.exe"))
qspiders.get("http://www.facebook.com")
qspiders.implicitly_wait(30)
qspiders.find_element_by_name("firstname").send_keys("Madhuri")
qspiders.find_element_by_name("lastname").send_keys("Rakshith")
qspiders.find_element_by_xpath("//input[(@aria-label='Mobile number or email address')]").send_keys("1234567892")
qspiders.find_element_by_xpath("//input[(@aria-label='New password')]").send_keys("rakma035@")
qspiders.find_element_by_xpath("//input[@value='1']").click()
qspiders.find_element_by_name("websubmit").click()
qspiders.find_element_by_xpath("//select[id='day')]").click()