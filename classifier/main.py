import os
import json
import random

DIRNAME = os.path.dirname(__file__)
DB_PATH = os.path.join(DIRNAME, "db.json")
SS_PATH = os.path.join(DIRNAME, "..", "source", "screenshots")

try:
    with open(DB_PATH) as f:
        db = json.load(f)
except FileNotFoundError:
    db = {}
    with open(DB_PATH, "w") as f:
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
    category = random.choice(categories)
    db[category].append(fn)

with open(DB_PATH, "w") as f:
    json.dump(db, f, indent=4)
