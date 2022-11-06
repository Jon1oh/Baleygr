import requests
from threading import Thread


def generate_urls(url):
    urls = []
    if url.endswith("gov.sg/"):
        for ext in exts:
            url_ = url.replace("gov.sg", ext)
            try:
                response = requests.get(url_)
                if response.status_code == 200:
                    with open(__file__.replace("main.py", "urls.txt"), "a") as f:
                        f.write(url_ + "\n")
                    urls.append(url_)
            except:
                print("Error: " + url_)


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
