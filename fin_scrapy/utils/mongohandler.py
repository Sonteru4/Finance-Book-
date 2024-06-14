import pymongo
from pymongo import *


class Mongo_Client_Wrapper():
    def __init__(self, address):
        try:
            self.client = MongoClient(address, False)
            self.client = self.client.data
            print("connected \r\n")
        except Exception as e:
            print(e)
            self.client = None

    def get_server_info(self):
        # Send a query to the server to see if the connection is working.
        try:
            print("server info")
            self.client.server_info()
        except Exception as e:
            print(("Unable to get server info %s.", e))
            self.client = None

    def mongo_insert(self, document, data):
        print("in handler")
        print(data)
        if self.client is None:
            raise Exception("Cant insert into mongo. Client is not connected")
        try:
            result = self.client[document].insert_one(data)
            print("Result %s, objectId : %s" % (result.acknowledged, result.inserted_id))
        except pymongo.results.InsertOneResult as e:
            return
        print("data inserted")
