import datetime
import json
import os

from bson.objectid import ObjectId
from flask import Flask
from flask_cors import CORS
from pymongo import *


class JSONEncoder(json.JSONEncoder):
    ''' extend json-encoder class'''

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return o.__dict__

    # create the flask object
app = Flask(__name__)
CORS(app)

# add mongo url to flask config, so that flask_pymongo can use it to make connection
app.config['MONGO_URI'] = os.environ.get('DB')
print(os.environ.get('DB'))
mongo = MongoClient(os.environ.get('DB'), False)
mongo = mongo.data

# use the modified encoder class to handle ObjectId & datetime object while jsonifying the response.
app.json_encoder = JSONEncoder

from app.controllers import *
