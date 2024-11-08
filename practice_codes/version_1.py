from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

# Create a webdriver Object
options = Options()
options.set_preference("acceptInsecureCerts", True)
options.add_argument("--start-maximized")

driver = webdriver.Firefox(options=options, service=Service(GeckoDriverManager().install()))
url = "https://10.2.0.253"

username = "automation"
password = "Auto2024"

driver.get(url=url)
driver.maximize_window()

username_field = driver.find_element(By.ID, "username")

password_field = driver.find_element(By.ID, "secretkey")

login_button = driver.find_element(By.ID, "login_button")

username_field.send_keys(username)
time.sleep(1)
password_field.send_keys(password)
time.sleep(1)
login_button.click()
time.sleep(3)

#security_link = driver.find_element(By.XPATH, "//a[@class='menu-label ng-tns-c150-12 ng-star-inserted']")

network_link = driver.find_element(By.XPATH, "//a[@class='menu-label ng-tns-c150-13 ng-star-inserted']")

#wifi_link = driver.find_element(By.XPATH, "//a[@class='menu-label ng-tns-c150-15 ng-star-inserted']")


# security_link.click()
# time.sleep(5)
network_link.click()
time.sleep(5)
# wifi_link.click()
# time.sleep(3)
inbound_val = driver.find_element(By.CSS_SELECTOR, "body > fos-root:nth-child(1) > nu-router-outlet:nth-child(3) > div:nth-child(1) > nu-router-content:nth-child(1) > fos-dashboard:nth-child(2) > nu-dashboard:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > nu-dashboard-widget-wrapper:nth-child(6) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > fos-dashboard-traffic-history-widget:nth-child(1) > fos-common-dashboard-widget:nth-child(1) > nu-dashboard-widget:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > fos-resource-usage-widget-status-entry:nth-child(1) > h3:nth-child(2) > span:nth-child(2)")
inbound = inbound_val.text

print(inbound)





#hover_element = driver.find_element(By.CSS_SELECTOR, "g[transform='translate(732.8499755859375, 0)']")
#actions = ActionChains(driver)
#actions.move_to_element(hover_element).perform()
#time.sleep(5)

driver.close();


#//span[normalize-space()='73.15 Mbps']
##cdk-overlay-17