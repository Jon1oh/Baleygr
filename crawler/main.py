from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import os
from urllib.parse import quote


# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

from webdriver_manager.core.utils import ChromeType

options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()),
    options=options,
)

URL_PATH = os.path.join(os.path.dirname(__file__), "..", "resources", "urls.txt")
SS_PATH = os.path.join(os.path.dirname(__file__), "..", "resources", "screenshots")
with open(URL_PATH, "r") as f:
    urls = f.read().splitlines()

counter = 0

for url in urls:
    counter += 1
    try:
        driver.get(url)
        driver.save_screenshot(os.path.join(SS_PATH, f"{quote(url, safe='')}.png"))
        print(f"{counter} (PASS). {url}")
    except:
        print(f"{counter} (FAIL). {url}")
