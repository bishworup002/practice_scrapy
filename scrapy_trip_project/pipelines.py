import os
from sqlalchemy import create_engine, Column, String, Float, Integer, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings

Base = declarative_base()

class Trip(Base):
    __tablename__ = 'trips'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    rating = Column(String)
    reviews = Column(String)
    location = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    room_type = Column(String)
    price = Column(String)
    image_paths = Column(String)

class TripPipeline:
    def __init__(self):
        settings = get_project_settings()
        db_url = settings.get('DATABASE')
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def process_item(self, item, spider):
        session = self.Session()
        trip = Trip(**item)
        try:
            session.add(trip)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return item

class TripImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item.get('image_urls', []):
            yield Request(image_url)

    def item_completed(self, results, item, info):
        if results:
            item['image_paths'] = [x['path'] for ok, x in results if ok]
        else:
            item['image_paths'] = None
        return item
