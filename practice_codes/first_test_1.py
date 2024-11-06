from selenium import webdriver

'''
Steps:
1. Initialize webdriver
2. Navigate to URL
3. Maximize the window
4. Get title of the page
5. Print title
'''

browser = webdriver.Firefox()
#https://10.2.0.253/login?redir=%2F
browser.get("https://10.2.8.24")
browser.maximize_window()

title = browser.title

print(title)