import scrapy
import json
import math
import time

def get_time():
    return str(math.floor(time.time() * 1000))


class BiobioSpider(scrapy.Spider):
    name = 'biobio'
    allowed_domains = ['www.biobiochile.cl']
    # start_urls = ['http://www.biobiochile.cl/']
    start_urls = [
        'https://www.biobiochile.cl/static/news.json?t=' + get_time()
    ]


    def parse(self, response):
        if "json" in response.url:
            yield from self.parse_with_json(response)

    
    def parse_with_json(self, response):
        data = json.loads(response.text)
        for noticia in data:
            yield {
                'title': noticia['post_title'],
                'url': noticia['post_URL'],
                'img': noticia['post_image']['URL'],
                'description': noticia['post_excerpt'],
                'author': noticia['author']['display_name'],
                'publish_date': noticia['post_date'],
                'category': [category['name'] for category in noticia['post_categories']],
                'content': noticia['post_content']
            }