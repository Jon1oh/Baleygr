import requests
from csv import DictWriter
from bs4 import BeautifulSoup

# grab the url of the page
url = 'https://www.theguardian.com/international'
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

dict = {}
header = ['URL']

for link in soup.find_all('a'):
    data = link.get('href')
    dict.update({'URL': data})
    print(dict)
    with open('./urls.csv', 'w') as file:
        dictwriter = DictWriter(file, fieldnames=header)
        dictwriter.writerow(dict)