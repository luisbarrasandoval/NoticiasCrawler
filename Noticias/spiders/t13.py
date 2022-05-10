import scrapy
from Noticias.items import NoticiasItem


NOTICIAS = '.card-normal'

class T13(scrapy.Spider):
    name = 't13'
    allowed_domains = ['www.t13.cl']
    start_urls = [
        'https://www.t13.cl/nacional',
        'https://www.t13.cl/mundo'
    ]


    def parse(self, response):
        item = NoticiasItem()
        for noticia in response.css(NOTICIAS):
            item["url"] =  response.urljoin(noticia.css("a")[0].attrib['href'])
            item["title"] = noticia.css("h2::text").get()
            item["img"] = noticia.css("img")[0].attrib['src']
            yield item