import scrapy


class MeganoticiasSpider(scrapy.Spider):
    name = 'meganoticias'
    allowed_domains = ['meganoticias.cl']
    start_urls = ['https://www.meganoticias.cl/lo-ultimo/']

    def parse(self, response):
        pass
