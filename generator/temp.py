from db import db, push_db, pull_db

with open("url-generator/urls.txt", "r") as f:
    urls = f.read().splitlines()
for url in urls:
    push_db("urls", url)
    print("Pushed: " + url)
