import requests
import uuid
import json
from threading import Thread

urls = []
with open("content-categorizer/urls.json", "r") as f:
    urls = json.loads(f.read())["domains"]
    counter = len(urls)


def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m) : (i + 1) * k + min(i + 1, m)] for i in range(n))


def check_urls(urls):
    global counter
    for url in urls:
        try:
            url_r = requests.get(f"http://{url}")
            if url_r.status_code == 200:
                url_c = url_r.content.decode("utf-8")
                with open(f"content-categorizer/webpages/{uuid.uuid4()}.txt", "w") as f:
                    f.write(url_c)
                print(f"{counter} Passed: {url}")
            else:
                print(f"{counter} Failed: {url}")
        except:
            print(f"{counter} Error: {url}")
        counter -= 1


def check_urls_t(urls):
    check_urls(urls)


if __name__ == "__main__":
    t_ls = []
    for urls_ in list(split(urls, 1000)):
        t = Thread(target=check_urls_t, args=(urls_,))
        t_ls.append(t)

    for t in t_ls:
        t.start()

    for t in t_ls:
        t.join()
