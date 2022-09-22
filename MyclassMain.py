from selenium import webdriver
import time
from time import sleep
import datetime
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

username = 'XXXXXXXX' #registration id
password = 'XXXXXXXX' #password
options = webdriver.ChromeOptions() 
#download chrome drive and add it's address here
driver = webdriver.Chrome(options=options, executable_path=r'C:\\Users\\kalya\\Documents\\chromedriver')
#driver = webdriver.Chrome(r"C:\Users\asing\Desktop\programs\python\chromedriver.exe")

driver.get("https://myclass.lpu.in/")
driver.maximize_window()


username_textbox = driver.find_element_by_name('i')
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_name('p')
password_textbox.send_keys(password)

login_button = driver.find_element_by_tag_name('button')
login_button.submit()

driver.get("https://lovelyprofessionaluniversity.codetantra.com/secure/tla/m.jsp")

def goToClass():
	try:
		element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div[1]/div[2]/a[1]')))
	except Exception as e:
		print("Its Holiday, enjoy your day")
		sleep(5)
		driver.quit()
		return

	maxClasses = 7 #maximum classes in a week
	grayColor = '128, 128, 128'
	for i in range(1, maxClasses+2):
		try:
			sub = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div[1]/div[2]/a['+str(i)+']')
			bgColor = sub.value_of_css_property('background')
		except Exception as e:
			print('All classes are completed, Come Next Day')
			sleep(5)
			driver.quit()
			quit()
		if(grayColor not in bgColor):
			sub.click()
			break
	joinClass()

def joinClass():
	try:
		joinButton = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="meetingSummary"]/div/div/a')))
		# joinButton = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a')
		joinButton.click()
	except Exception as e:
		print("Class is Not Started Yet")
		sleep(5)
		return
	print("Pass: Joined Class")
	chooseMode()

def chooseMode():
	# sleep(10)
	try:
		frame = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="frame"]')))
		driver.switch_to.frame(frame)
		listenMode = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/span/button[2]')))
		listenMode.click()
	except Exception as e:
		print("Fail: Audio Mode is Not Visible")
		return
	print("Pass: Listen Mode Selected")


goToClass()
