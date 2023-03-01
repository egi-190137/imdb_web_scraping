import scrapy


class ImageSpider(scrapy.Spider):
    name = 'image'
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    def parse(self, response):
        raw_image_urls = response.css('td.posterColumn img::attr(src)').getall()
        
        image_urls = []
        for url in raw_image_urls:
            image_urls.append(response.urljoin(url))

        yield {
            'image_urls': image_urls,
        }
