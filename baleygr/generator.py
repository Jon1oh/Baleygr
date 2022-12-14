import requests
import os
from threading import Thread
from logger import generator_logger as logging


def check_urls(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(URL_PATH, "a") as f:
                f.write(url + "\n")
            urls.append(url)
            logging.info(f"{counter} (PASS). {url}")
    except:
        logging.info(f"{counter} (FAIL). {url}")

#This set of code is designed to test if the website that is being used can be reached and if so, it will be marked as a pass.


def generate_urls(url):
    global counter
    for ext in exts:
        counter += 1
        url_ = url.replace(url[-7:-1], ext)
        check_urls(url_)

#This set of code is designed to replace the gov.sg extension in the official urls of sites.

def generate_urls_thread(url, output):
    output.append(generate_urls(url))

#This set of code is designed to add urls that have been created by the general_urls function to output.

def check_single():
    with open(URL_PATH, "r") as f:
        urls = set(f.read().splitlines())
    with open(URL_PATH, "w") as f:
        for url in urls:
            f.write(url + "\n")
#This set of code is designed to read the urls line by line.

if __name__ == "__main__":
    ROOT_PATH = os.path.dirname(__file__)
    LOG_PATH = os.path.join(ROOT_PATH, "logger", "generator.log")
    SRC_PATH = os.path.join(ROOT_PATH, "resources")
    SDM_PATH = os.path.join(SRC_PATH, "subdomains-10000.txt")
    GOV_PATH = os.path.join(SRC_PATH, "gov-urls.txt")
    URL_PATH = os.path.join(SRC_PATH, "urls.txt")

    with open(SDM_PATH, "r") as f:
        exts = f.read().splitlines()

    with open(GOV_PATH, "r") as f:
        urls = f.read().splitlines()

    thread_list, valid_urls, counter = [Thread(target=check_single)], [], 0

    for url in urls:
        t = Thread(target=generate_urls_thread, args=(url, valid_urls))
        thread_list.append(t)

    for t in thread_list:
        t.start()

    for t in thread_list:
        t.join()
