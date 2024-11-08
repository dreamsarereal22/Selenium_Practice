from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

# Creating a driver object

driver = webdriver.Firefox()

# Assigning url
url = "https://the-internet.herokuapp.com/dropdown"

# Get req to url
driver.get(url=url)

# Display size
driver.maximize_window()

select_dropdown = driver.find_element(By.ID, "dropdown")

selection = Select(select_dropdown)

# Using visible text value
selection.select_by_visible_text("Option 2")
# Can Use the value
#selection.select_by_value("2")