from pymongo import MongoClient
import os

class DBModel(object):
    # client = MongoClient()
    client = MongoClient("mongodb+srv://wijatama:tEyYdWRXuDSDGF1N@crawlmend-project.twn5s.mongodb.net/journal_details?retryWrites=true&w=majority")
    database = "journal_details"

    def insert_url(self, collection, url):
        db = self.client[self.database]
        result = db[collection].insert_one({'url':url})
        print('url inserted.')

        return result.inserted_id

    def get_urls(self):
        db = self.client[self.database]
        collection = db['urls']
        result = collection.find()

        print('all urls is collected.')
        return result

    def insert_detail(self, collection, data):
        "Insert the detail of crawled mendeley journal page"
        db = self.client[self.database]
        result = db[collection].insert_one(  #data)
                    {
                        "url": data[0],
                        "title": data[1],
                        "publihser": data[2],
                        "doc_id": data[3],
                        "authors": data[4],
                        "keywords": data[5],
                        "abstract": data[6]
                    }
                )
        return result.inserted_id

    def check_docs(self, collection, url):
        db = self.client[self.database]
        result = db[collection].find_one({'url': url})
        if result is None:
            value = False
        else:
            value = True
        return value
