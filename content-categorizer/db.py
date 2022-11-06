import requests
import urllib

db = {}


def pull_db():
    global db
    r = requests.get("https://baleygr.lgf2111.repl.co/pull")
    db.update(r.json())


def push_db(key, value):
    key_, value_ = urllib.parse.quote(key), urllib.parse.quote(value)
    r = requests.get(f"https://baleygr.lgf2111.repl.co/push?key={key_}&value={value_}")
    return r.status_code == 200


def init_db(key):
    key_ = urllib.parse.quote(key)
    r = requests.get(f"https://baleygr.lgf2111.repl.co/init?key={key_}")
    return r.status_code == 200
