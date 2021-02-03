from pymongo import MongoClient
import os

class DBModel(object):
    # client = MongoClient()
    client = MongoClient("mongodb+srv://wijatama:tEyYdWRXuDSDGF1N@crawlmend-project.twn5s.mongodb.net/journal_details?retryWrites=true&w=majority")

    def insert_url(self, database, collection, url):
        db = self.client[database]
        result = db[collection].insert_one({'url':url})
        print('url inserted.')

        return result.inserted_id

    def get_urls(self, database):
        db = self.client[database]
        collection = db['urls']
        result = collection.find()

        print('all urls is collected.')
        return result

    def insert_detail(self, database, collection, data):
        "Insert the detail of crawled mendeley journal page"
        db = self.client[database]
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