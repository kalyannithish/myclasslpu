from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 
import os
import schedule
driver_path= '/usr/local/bin'
username = "11911809"
password = "Kalyan@0033"
browser = webdriver.Firefox()
browser.get('https://myclass.lpu.in/')
time.sleep(5)
inputElement = browser.find_element_by_name("i")
inputElement.send_keys(username)
print("Entered Username:",username)
time.sleep(1)
inputElement = browser.find_element_by_name("p")
inputElement.send_keys(password)
print("Enter password:",password)
loginButton= browser.find_element_by_xpath("/html/body/div[2]/div/form/div[7]/button").click()
browser.implicitly_wait(3)
time.sleep(2)
#link.send_keys(Keys.ENTER)
View_meeting = browser.find_element_by_xpath("/html/body/div[9]/div/div[1]/div/div/div[1]/div/div[2]/a").click()
#Enterclass = browser.find_element_by_id("calendar").click()
Enterclass = browser.find_element_by_css_selector("#calendar > div.fc-view-container > div > table > tbody > tr > td > div > div > div.fc-content-skeleton > table > tbody > tr > td:nth-child(2) > div > div:nth-child(2) > a:nth-child(1)").click()
JOIN = '/html/body/div[1]/div[2]/div/div/a'
CLASS_JOIN = browser.find_element_by_css_selector('.btn-primary')
CLASS_JOIN.click()
time.sleep(4)
LISTEN.ONLY = '/html/body/div[2]/div/div/div[1]/div/div/span/button[2]/span[1]/i'
LISTEN = browser.find_element_by_xpath(LISTEN_ONLY)
LISTEN
