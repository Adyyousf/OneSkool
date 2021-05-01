import scrapy  # importing scrapy. Python web scraping Framework.

# MySpider is a scrapy.spider sub-class that i define and Scrapy uses to scrape information from the website. 
class MySpider(scrapy.Spider):
    name = "myspider"  # unique name to identify the spider

    # Generator function that returns a Request (iterable) which the Spider will begin to crawl from.
    def start_requests(self):
        # url/s of website/s to be downloaded
        urls = [
            'https://in.finance.yahoo.com/news/govt-permits-oxygen-concentrator-imports-101255981.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
    # Method to handle the response downloaded from the Request
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'mySpider-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved File {filename}')