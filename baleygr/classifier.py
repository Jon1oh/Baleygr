import os
import glob
import json
import time
import random
from urllib.parse import unquote
from threading import Thread

from logger import classifier_logger as logging

SRC_PATH = os.path.join(os.path.dirname(__file__), "resources")
RES_PATH = os.path.join(SRC_PATH, "results.json")
SS_PATH = os.path.join(SRC_PATH, "screenshots")

CATEGORIES = [
    "Safe",
    "Offensive Content",
    "Cyber Malicious",
    "Scam / Phishing",
    "Potentially Illegal Activity",
    "Hate Speech",
    "Violence",
    "Sexual Content",
    "Other",
]


def update():
    list_of_files = glob.glob(os.path.join(SS_PATH, "*"))
    latest_file = max(list_of_files, key=os.path.getctime)
    file = latest_file[latest_file.find("screenshots") + 12 :]
    classify(file)
    save(RES_PATH)


def monitor():
    latest_time = 0
    while True:
        current_time = os.path.getctime(SS_PATH)
        if latest_time < current_time:
            latest_time = current_time
            update()
        time.sleep(1)


def monitor_thread():
    t = Thread(target=monitor)
    t.start()
    return t


def classify(file=None):
    global db
    global counter
    for category in CATEGORIES:
        if not db.get(category):
            db[category] = []

    file_list = [file] if file else os.listdir(SS_PATH)
    for fn in file_list:
        url = unquote(fn.replace(".png", ""))
        if url not in urls:
            counter += 1
            category = random.choice(CATEGORIES)
            db[category].append(url)
            logging.info(f"{counter}. {url}")


def save(path):
    with open(path, "w") as f:
        json.dump(db, f, indent=4)


if __name__ == "__main__":
    counter = 0
    try:
        with open(RES_PATH) as f:
            db = json.load(f)
        urls = sum([_ for _ in db.values()], [])

    except FileNotFoundError:
        db, urls = {}, []
        save(RES_PATH)

    classify()
    save(RES_PATH)

    monitor()
