import requests
from threading import Thread
from db import db, push_db, pull_db


def generate_urls(url):
    global counter
    for ext in exts:
        url_ = url.replace(url[url.rfind(".", 1) : -1], ext)
        pull_db()
        if db.get("urls"):
            if url_ in db.get("urls"):
                continue
        counter += 1
        try:
            response = requests.get(url_)
            if response.status_code == 200:
                push_db("urls", url_)
                print("Success: " + str(counter) + url_)
        except:
            print("Error: " + str(counter) + " URL: " + url_)


def generate_urls_t(url, output):
    output.append(generate_urls(url))


if __name__ == "__main__":
    with open(__file__.replace("main.py", "DN_extensions.txt"), "r") as f:
        exts = f.read().splitlines()

    with open(__file__.replace("main.py", "whitelist.txt"), "r") as f:
        urls = f.read().splitlines()

    t_ls = []
    valid_urls = []
    counter = 0

    for url in urls:
        t = Thread(target=generate_urls_t, args=(url, valid_urls))
        t_ls.append(t)

    for t in t_ls:
        t.start()

    for t in t_ls:
        t.join()

    print("Done")
