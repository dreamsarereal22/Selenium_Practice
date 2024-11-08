'''from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
url = "https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407"
driver.get(url)
driver.maximize_window()
time.sleep(2)

# This a JS Window method
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

checkbox = driver.find_element(By.XPATH, "//label[normalize-space()='Tuesday']")
checkbox.click()'''

# Challenge
# Check how many check boxes are checked
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

# Defining and assigning webdriver object
driver = webdriver.Firefox()
url = "https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407"

# Request for the Url
driver.get(url=url)

# Define browser display size
driver.maximize_window()

# Defining target checkboxes
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE)
    time.sleep(2)

count_checkbox = 0

for checkbox in checkboxes:
    if checkbox.is_selected:
        count_checkbox += 1

checkbox_count = 7
if count_checkbox == checkbox_count:
    print("Completed")
else:
    print("Not complete")