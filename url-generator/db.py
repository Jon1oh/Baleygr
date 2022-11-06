import requests
import urllib


def pull_db():
    global db
    r = requests.get("https://baleygr.lgf2111.repl.co/pull")
    db = r.json()


def push_db(key, value):
    key_, value_ = urllib.parse.quote(key), urllib.parse.quote(value)
    r = requests.get(f"https://baleygr.lgf2111.repl.co/push?key={key_}&value={value_}")
    print("Success" if r.status_code == 200 else "Failed")
