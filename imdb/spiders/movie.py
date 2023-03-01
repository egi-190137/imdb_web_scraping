import scrapy


class MovieSpider(scrapy.Spider):
    name = 'movie'
    start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']

    def parse(self, response):

        for row in response.css('table > tbody > tr'):
            raw_image_urls = row.css('td.posterColumn img::attr(src)').get()

            yield {
                'Judul': row.css('td.titleColumn > a::text').get(),
                'Rating': row.css('td.ratingColumn.imdbRating > strong::text').get(),
                'image-src': response.urljoin(raw_image_urls),
            }