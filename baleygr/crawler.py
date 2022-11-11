from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import os
from urllib.parse import quote

from logger import crawler_logger as logging

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

SRC_PATH = os.path.join(os.path.dirname(__file__), "resources")
URL_PATH = os.path.join(SRC_PATH, "urls.txt")
SS_PATH = os.path.join(SRC_PATH, "screenshots")

if __name__ == "__main__":
    fn_collection = []
    while True:
        with open(URL_PATH, "r") as f:
            urls = f.read().splitlines()

        counter = 0

        for url in urls:
            counter += 1
            fn = f"{quote(url, safe='')}.png"
            if fn in fn_collection:
                continue
            try:
                driver.get(url)
                driver.save_screenshot(os.path.join(SS_PATH, fn))
                fn_collection.append(fn)
                logging.info(f"{counter} (PASS). {url}")
            except:
                logging.info(f"{counter} (FAIL). {url}")
