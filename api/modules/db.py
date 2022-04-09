from datetime import datetime
from modules.consts import URL_COLLECTION

class DBRequests:
    @classmethod
    def add_url(cls, short_url: str, full_url: str):
        # If the short_url already exists, it returns None
        if cls.get_url(short_url=short_url):
            return None

        url = {
            "short_url": short_url,
            "full_url": full_url,
            "added_date": datetime.now()
        }

        return URL_COLLECTION.insert_one(url)

    @classmethod
    def get_url(cls, short_url: str):
        url = URL_COLLECTION.find_one({"short_url": short_url})

        # If the db doesn't contain the short_url, the response is None
        if url:
            return url["full_url"]
        return None