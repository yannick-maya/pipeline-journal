import pymongo

class MongoDBConnector:
    def __init__(self, uri, db_name):
        self.client = pymongo.MongoClient(uri)
        self.db = self.client[db_name]

    def insert_document(self, collection_name, document):
        collection = self.db[collection_name]
        result = collection.insert_one(document)
        return result.inserted_id

    def find_documents(self, collection_name, query={}):
        collection = self.db[collection_name]
        return list(collection.find(query))

    def close(self):
        self.client.close()