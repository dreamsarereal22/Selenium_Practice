from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# Automatically allow camera access
chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_camera": 1
})

driver = webdriver.Chrome(options=chrome_options)
driver.get("your_website_url")
