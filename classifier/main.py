import os
import json
import random
from urllib.parse import unquote

SRC_PATH = os.path.join(os.path.dirname(__file__), "..", "resources")
RES_PATH = os.path.join(SRC_PATH, "results.json")
SS_PATH = os.path.join(SRC_PATH, "screenshots")

try:
    with open(RES_PATH) as f:
        db = json.load(f)
    urls = sum([_ for _ in db.values()], [])

except FileNotFoundError:
    db, urls = {}, []
    with open(RES_PATH, "w") as f:
        json.dump(db, f, indent=4)

categories = [
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

for category in categories:
    if not db.get(category):
        db[category] = []

for fn in os.listdir(SS_PATH):
    url = unquote(fn.replace(".png", ""))
    if url not in urls:
        category = random.choice(categories)
        db[category].append(url)

with open(RES_PATH, "w") as f:
    json.dump(db, f, indent=4)
