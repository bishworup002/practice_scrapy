# Settings for Scrapy
BOT_NAME = 'scrapy_trip_project'
SPIDER_MODULES = ['scrapy_trip_project.spiders']
NEWSPIDER_MODULE = 'scrapy_trip_project.spiders'

# Enable the Images Pipeline
ITEM_PIPELINES = {
    'scrapy_trip_project.pipelines.TripPipeline': 300,
    'scrapy.pipelines.images.ImagesPipeline': 1,
}

IMAGES_STORE = 'images'

# PostgreSQL Database Configuration
DATABASE = {
    'drivername': 'postgresql',
    'host': 'localhost',
    'port': '5433',
    'username': 'postgres',
    'password': 'p@stgress',
    'database': 'trip'
}
