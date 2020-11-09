from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os


driver = Chrome()

driver.get("https://mail.protonmail.com/login")

time.sleep(7)

driver.find_element(By.ID, "username").send_keys("dobry1@protonmail.com")

password1 = os.getenv('protonMailPass1')
driver.find_element(By.ID, "password").send_keys(password1)

driver.find_element(By.ID, ("login_btn")).click()

time.sleep(3)
password2 = os.getenv('protonMailPass2')
driver.find_element(By.ID, "mailboxPassword").send_keys(password2)

driver.find_element(By.ID, ("unlock_btn")).click()

print("chceck new mails")

time.sleep(3)

newMail = driver.find_element(By.XPATH, ('//*[@id="pm_sidebar"]/ul[1]/li[1]/a/div/em')).text

#get_attribute("value")

newMailVal = newMail.strip("()")
	
newMailInt = int(newMailVal)

if(newMailInt>0):
	print(str(newMailInt))
else:
	driver.close()
