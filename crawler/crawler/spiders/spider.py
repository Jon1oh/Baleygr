import scrapy
from db import pull_db, push_db, db

class PostsSpider(scrapy.Spider):
    name = 'posts'
    pull_db()
    urls = db['urls']

    def parse(self, response):
        page = response.url.split('/')[-1]
        filename = '%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)

