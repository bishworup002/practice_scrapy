import scrapy
from scrapy_trip_project.items import TripItem

class TripSpider(scrapy.Spider):
    name = 'trip'
    start_urls = ['https://uk.trip.com/hotels/list?city=338&checkin=2024/8/2&checkout=2024/08/03']

    def parse(self, response):
        for hotel in response.css('div.hotel-card'):  # Replace with actual selector for each hotel card
            item = TripItem()
            item['title'] = hotel.css('h3.hotel-title::text').get()  # Replace with actual selector for hotel title
            item['rating'] = hotel.css('span.hotel-rating::text').get()  # Replace with actual selector for rating
            item['location'] = hotel.css('span.hotel-location::text').get()  # Replace with actual selector for location
            item['latitude'] = hotel.css('meta[itemprop=latitude]::attr(content)').get()  # Replace with correct selector
            item['longitude'] = hotel.css('meta[itemprop=longitude]::attr(content)').get()  # Replace with correct selector
            item['room_type'] = hotel.css('span.room-type::text').get()  # Replace with actual selector for room type
            item['price'] = hotel.css('span.hotel-price::text').get()  # Replace with actual selector for price
            item['image_urls'] = hotel.css('img::attr(src)').getall()  # Selector for image URLs
            yield item
