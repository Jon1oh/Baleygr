import scrapy

class PostsSpider(scrapy.Spider):
    name = 'posts'

    start_urls = [
        'https://equinox-windflower-582.notion.site/singapore-sucks-706401cda27248b483c318f6f46b37a0',
        'https://equinox-windflower-582.notion.site/PAP-is-a-dictatorship-bc394f2585e047a89f89f465d241d5a0',        
        
    ]

    def parse(self, response):
        page = response.url.split('/')[-1]
        filename = '%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)

