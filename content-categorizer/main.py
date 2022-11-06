from db import db, pull_db, push_db

if not db.get["url_pairs"]:
    db["url_pairs"] = []
url_pairs = db["url_pairs"]
url_pairs = [
    [
        "https://creative-termination-dude-implementing.trycloudflare.com/login.html",
        "https://github.com/login",
    ],
]
