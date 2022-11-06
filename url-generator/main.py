import requests
from threading import Thread

def check_urls(url_):
    try:
        response = requests.get(url_)
        if response.status_code == 200:
            with open(__file__.replace("main.py", "urls3.txt"), "a") as f:
                f.write(url_ + "\n")
            urls.append(url_)
            print("Success: " + str(counter) + url_)
    except:
        print("Error: " + str(counter) + " URL: " + url_)

def generate_urls(url):
    urls = []
    global counter
    counter = 0
    if url.endswith("gov.sg/") or url.endswith("edu.sg/") or url.endswith("com.sg/"):
        for ext in exts:
            counter += 1
            url_ = url.replace(url[-7:-1], ext)
            check_urls(url_)


def generate_urls_t(url, output):
    output.append(generate_urls(url))


if __name__ == "__main__":
    with open(__file__.replace("main.py", "DN_extensions.txt"), "r") as f:
        exts = f.read().splitlines()

    with open(__file__.replace("main.py", "whitelist.txt"), "r") as f:
        urls = f.read().splitlines()

    t_ls = []
    valid_urls = []
    for url in urls:
        t = Thread(target=generate_urls_t, args=(url, valid_urls))
        t_ls.append(t)

    for t in t_ls:
        t.start()

    for t in t_ls:
        t.join()


    # valid_urls = [generate_urls(url) for url in urls]
    # print(valid_urls)
