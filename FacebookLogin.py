"""Automated Facebook log in applicaton using ChromeDriver"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os, time

user = "XXX@gmail.com"
password = "XXXXX"
driver = webdriver.Chrome(executable_path = "Path to Chromedriver")

elem = driver.find_element_by_id('email')
elem.send_keys(user)

elem.send_keys(password)

elem.send_keys(Keys.RETURN)

elem = driver.find_element_by_css_selector('.input.textInput')
elem.send_keys('This was posted using Python')
elem = driver.find_element_by_css_selector('.selected')

elem.click()
time.sleep(5)

driver.close()
raw_input('Done')