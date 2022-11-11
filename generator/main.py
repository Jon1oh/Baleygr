import requests
from threading import Thread
import os


def check_urls(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(URL_PATH, "a") as f:
                f.write(url + "\n")
            urls.append(url)
            print(f"{counter} (PASS). {url}")
    except:
        print(f"{counter} (FAIL). {url}")


def generate_urls(url):
    global counter
    for ext in exts:
        counter += 1
        url_ = url.replace(url[-7:-1], ext)
        check_urls(url_)


def generate_urls_thread(url, output):
    output.append(generate_urls(url))


if __name__ == "__main__":
    SRC_PATH = os.path.join(os.path.dirname(__file__), "..", "resources")
    SDM_PATH = os.path.join(SRC_PATH, "subdomains-10000.txt")
    GOV_PATH = os.path.join(SRC_PATH, "gov-urls.txt")
    URL_PATH = os.path.join(SRC_PATH, "urls.txt")

    with open(SDM_PATH, "r") as f:
        exts = f.read().splitlines()

    with open(GOV_PATH, "r") as f:
        urls = f.read().splitlines()

    thread_list, valid_urls, counter = [], [], 0

    for url in urls:
        t = Thread(target=generate_urls_thread, args=(url, valid_urls))
        thread_list.append(t)

    for t in thread_list:
        t.start()

    for t in thread_list:
        t.join()
