'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Firefox()

url = 'https://10.2.8.24'

username = 'zebra'
password = 'extrastr0ng'

browser.get(url)
browser.maximize_window()

browser.find_element(by='name', value= 'username').send_keys(username)
time.sleep(2)
browser.find_element(by='name', value= 'password').send_keys(password)
time.sleep(2)
#browser.find_element(by='id', value= 'submit').click()
browser.find_element(By.ID,'submit').click()'''

'''
Best Practice:
1. Initialize webdriver by creating an object of it
2. Define a url variable and assign url
3. Optional use maximize_window()
4. Define username and password
5. Find username and password text boxes and enter the text
6. Find login button and click
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

# This will handle pop alerts
opt = Options()
opt.set_preference("media.navigator.permission.disabled" , True)

driver = webdriver.Firefox(options=opt)
url = 'https://10.2.8.24'

driver.get(url)
driver.maximize_window()

username = 'zebra'
password = 'extrastr0ng'

username_box = driver.find_element(By.NAME, 'username')
password_box = driver.find_element(By.NAME, 'password')
submit_button = driver.find_element(By.ID, 'submit')

# Action
# Sending user information
username_box.send_keys(username)
time.sleep(1)
password_box.send_keys(password)
time.sleep(1)
# CLICK ACTION BUTTON
# CHECK first if disable using assert

assert not submit_button.get_attribute('disabled')
submit_button.click()
time.sleep(1)

# Handling Links
buttons = driver.find_element(By.XPATH, "//a[@title='QR Scan']")
buttons.click()
time.sleep(1)
req_button = driver.find_element(By.ID, 'html5-qrcode-button-camera-permission')
req_button.click()

time.sleep(1)
start_cam = driver.find_element(By.ID, "html5-qrcode-button-camera-start")
start_cam.click()