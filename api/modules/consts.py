import pymongo
import os

CLIENT = pymongo.MongoClient(os.environ.get("mongodb_url"))
CLUSTER = CLIENT["shortened_urls"]
URL_COLLECTION = CLUSTER["urls"]