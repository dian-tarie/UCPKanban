from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome(executable_path="C:\Windows\System32\chromedriver.exe")
driver.get("https://dev.amalan.xyz/customers")

driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='email']").send_keys("dian@amalan.org")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='password']").send_keys("bzdLDc2x9O05")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='auth-login']/div/div/div/div[1]/div/div[2]/div/form/button").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='app']/section[3]/div/div/div/div/div[1]/table/tbody/tr[1]/td[2]/a").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='app']/section[1]/div/div[2]/div/a[1]").click()
time.sleep(3)
driver.find_element_by_xpath("//*[@id='app']/section[1]/div/div[2]/div/a[2]").click()

driver.close()
