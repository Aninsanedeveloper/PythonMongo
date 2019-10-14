from pymongo import MongoClient #import modules

MONGO_URI = 'mongodb://localhost' #the uri for mongo client

client = MongoClient(MONGO_URI) 

db = client['mycustomers'] # createa database
collection = db['products'] # createa a collection

collection.insert_one({"name": "Api", "price": 300})