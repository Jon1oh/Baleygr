import requests, json
from bs4 import BeautifulSoup

# grab the url of the page
url = 'https://www.theguardian.com/international'
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

for link in soup.find_all('a'):
    data = {
        'URL': link.get('href')
    }

    print(data)
    with open('./urls.json', 'a') as file:
        json.dump(data, file, indent=4)
        file.write("\n")
