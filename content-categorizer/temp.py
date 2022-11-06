from db import db, push_db, pull_db

url_pairs = [
    [
        "https://creative-termination-dude-implementing.trycloudflare.com/login.html",
        "https://github.com/login",
    ]
]

for url_pair in url_pairs:
    push_db("url_pairs", str(url_pair))
