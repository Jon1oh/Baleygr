# Main Imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests, os

# Install Driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the files
dir = os.listdir('./whitelist_screenshots')

if len(dir) == 0:
    with open('whitelist.txt') as file:
        content = file.readlines()
        count = 0
        for url in content:
            driver.get(url)
            driver.save_screenshot(f"./whitelist_screenshots/image-{count}.png")
            count += 1
else:
    pass
