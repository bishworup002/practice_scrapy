import scrapy
from scrapy_trip_project.items import TripItem
import re
import json

class TripSpider(scrapy.Spider):
    name = 'trip'
    start_urls = ['https://uk.trip.com/hotels/?locale=en-GB&curr=GBP']

    def parse(self, response):
        # Extract the script tag content containing 'window.IBU_HOTEL'
        script_content = response.xpath('//script[contains(text(), "window.IBU_HOTEL")]/text()').get()
        
        if script_content:
            # Use regex to find the JSON-like object within the script content
            json_data_match = re.search(r'window\.IBU_HOTEL\s*=\s*({.*?});', script_content, re.DOTALL)

            if json_data_match:
                # Extract the matched JSON-like string
                json_data_str = json_data_match.group(1)

                try:
                    # Convert the JSON-like string to a Python dictionary
                    json_data = json.loads(json_data_str)

                    # Extract hotel data
                    htlsData = json_data.get('initData', {}).get('htlsData', [])

                    with open("htlsData.json", "w", encoding="utf-8") as json_file:
                        json.dump(htlsData, json_file, indent=4, ensure_ascii=False)
                    self.logger.info("htlsData saved successfully to htlsData.json")
                    
                    # Extract hotel data
                    hotels = htlsData.get('inboundCities', [])[0].get('recommendHotels', [])

                    # print(hotels)
                    
                    for hotel in hotels:
                        item = TripItem()
                        item['title'] = hotel.get('hotelName')
                        item['rating'] = hotel.get('rating')
                        item['location'] = hotel.get('fullAddress')
                        item['latitude'] = hotel.get('lat')
                        item['longitude'] = hotel.get('lon')
                        item['room_type'] = "Standard"  # Modify as per available data or further scraping logic
                        item['price'] = hotel.get('prices', {}).get('priceInfos', [{}])[0].get('price')
                        
                        # Handling single image URL from 'imgUrl'
                        base_url = 'https://ak-d.tripcdn.com/images'
                        image_urls = [base_url + hotel.get('imgUrl', '')]
                        
                        # # Handling additional images from 'pictureList'
                        # for picture in hotel.get('pictureList', []):
                        #     image_urls.append(base_url + picture.get('pictureUrl'))
                        
                        print( image_urls )
                        
                        item['image_urls'] = image_urls
                        
                        yield item

                except json.JSONDecodeError as e:
                    self.logger.error(f"Failed to decode JSON: {e}")
