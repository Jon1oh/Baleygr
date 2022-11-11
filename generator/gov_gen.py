from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import os


# from webdriver_manager.core.utils import ChromeType

# options = webdriver.ChromeOptions()
# options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
# driver = webdriver.Chrome(
#     service=Service(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()),
#     options=options,
# )

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

GOV_URL = os.path.join(os.path.dirname(__file__), "..", "resources", "gov-urls.txt")
URL = "https://www.sgdi.gov.sg/{route}"
ROUTES = [
    "ministries",
    "statutory-boards",
    "organs-of-state",
    "other-organisations",
    "public-services",
    "spokespersons",
]

with open(GOV_URL, "w") as f:
    counter = 0
    for route in ROUTES:
        driver.get(URL.replace("{route}", route))
        anchors = driver.find_elements(
            By.CSS_SELECTOR, ".directory-list .ministries li a"
        )
        for anchor in anchors:
            href = anchor.get_attribute("href")
            if not href.startswith("https://www.sgdi.gov.sg/") and href:
                f.write(href + "\n")
                counter += 1
                print(f"{counter}. {href}")

driver.quit()
