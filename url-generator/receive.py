from azure.storage.blob import BlobClient
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Install Driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
blob = BlobClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=urls;AccountKey=pQakwxv1mG9495upsjqgk+wRHWWp6u9+kO9Yw+wIEHxK10jRZvYX0ZXuSYZM+SEpDIE6rvcR1PVy+ASt+rfDCQ==;EndpointSuffix=core.windows.net", container_name="urls", blob_name="urls")
data = blob.download_blob()
dataread = data.readall().decode()
finale = dataread.split("\n")

count = 0
for url in finale:
    driver.get(url)
    driver.save_screenshot(f"./testing/image-{count}.png")
    count += 1




 
