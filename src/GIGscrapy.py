import time
import scrapy
from scrapy.crawler import CrawlerProcess

class BrickSetSpider(scrapy.Spider):
    name = "spiderman"  # just a name for the spider.

    url = "https://gig.ee/et/kasutatud-tehnika.html"
    # Set the headers here
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'
    }

    def start_requests(self):
        yield scrapy.http.Request(self.url, headers=self.headers)


    def parse(self, response):
        SET_SELECTOR = 'li.item'
        for product in response.css(SET_SELECTOR):
            NAME_SELECTOR = 'div.product-block h2 ::text'
            PRICE_SELECTOR = 'div.price-box span.price ::text'
            PICTURE_SELECTOR = 'div.product-image-block img ::attr(src)'
            yield {
                    'name': product.css(NAME_SELECTOR).extract_first(),
                    'price': product.css(PRICE_SELECTOR).extract_first().replace(u'\xa0', '').replace('\n', '').strip(),
                    'picture': product.css(PICTURE_SELECTOR).extract_first()
                }

        NEXT_PAGE_SELECTOR ='li a.next.i-next ::attr(href)'

        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()

        if next_page:
            time.sleep(5)  # to avoid http response 429
            url = response.urljoin(next_page)
            yield scrapy.Request(url, self.parse, headers=self.headers)


output_file = 'scrapy-products.json'
process = CrawlerProcess(settings={
    'FEEDS': {
        output_file: {
            'format': 'json',
            'indent': 4
        }
    }
})
process.crawl(BrickSetSpider)
process.start()