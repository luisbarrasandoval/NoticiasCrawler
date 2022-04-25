from datetime import datetime
import scrapy

from Noticias.items import NoticiasItem

# Donde se encuentra la informacion
ARTICLES = 'article.box-generica'
URL = '.top a'
TITLE = '.bottom a ' # h1 o h2::text
IMG = '.top a img'

PUBLISH_DATE = 'div.contenedor-contenido div.fechaHora::text'


class MeganoticiasSpider(scrapy.Spider):
    name = 'meganoticias'
    allowed_domains = ['meganoticias.cl']
    start_urls = ['https://www.meganoticias.cl/nacional/',
                  'https://www.meganoticias.cl/mundo/']

    def parse(self, response):
        for article in response.css(ARTICLES):
            _img = article.css(IMG)
            item = NoticiasItem()

            title = article.css(TITLE + "h2::text").get()
            if title is None:
                title = article.css(TITLE + "h1::text").get()
            item["title"] = title
            item["url"] = article.css(URL).attrib['href']
            item["img"] = _img.attrib.get('src') or _img.attrib.get('data-src')
            item["description"] = _img.attrib.get('alt') or ''
   
            # load page
            yield scrapy.Request(item["url"], callback=self.parse_page, meta={'item': item})


    def parse_page(self, response):
        item = response.meta['item']
        item['author'] = response.css('.periodista::text').get()
        item["publish_date"] = self.parse_publish_date(response)
        item['category'] = self.parse_categories(response)
        item['content'] = response.css('.contenido-nota').getall()

        # public_date to object datetime
        
        yield item

    def parse_publish_date(self, response):
        publish_date = response.css(PUBLISH_DATE).get()
        try:
            # mal
            publish_date = publish_date[0:10] + ' ' + publish_date[11:19]
            publish_date = datetime.strptime(publish_date, '%Y-%m-%d %H:%M:%S')
        except:
            publish_date = None
        return publish_date
    
    def parse_categories(self, response):
        categories = []
        for category in response.css(".contenedor-temas li"):
            text = category.css('a::text').get().strip()
        return categories