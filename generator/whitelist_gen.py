# Main Imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as BraveService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

# Wait Imports
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Interraction Imports
from selenium.webdriver.common.by import By


# Install Driver
options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
driver = webdriver.Chrome(
    service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()),
    options=options,
)


URL = "https://www.sgdi.gov.sg/{route}"
ROUTES = [
    "ministries",
    "statutory-boards",
    "organs-of-state",
    "other-organisations",
    "public-services",
    "spokespersons",
]

with open(__file__.replace("whitelist_gen.py", "whitelist.txt"), "w") as f:
    for route in ROUTES:
        driver.get(URL.replace("{route}", route))
        anchors = driver.find_elements(
            By.CSS_SELECTOR, ".directory-list .ministries li a"
        )
        for anchor in anchors:
            href = anchor.get_attribute("href")
            if not href.startswith("https://www.sgdi.gov.sg/") and href:
                f.write(href + "\n")
                print(href)

driver.quit()
