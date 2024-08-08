from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy_trip_project.spiders.trip_spider import TripSpider

process = CrawlerProcess(get_project_settings())
process.crawl(TripSpider)
process.start()
