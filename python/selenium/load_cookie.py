import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import json

browser = webdriver.Chrome(executable_path='./chromedriver')
wait = WebDriverWait(browser, 160)
with open('cook.json', 'r') as fli:
    data = json.load(fli)
browser.get("https://shopee.co.id/buyer/login")
for i in data:
    browser.add_cookie(i)
browser.quit()