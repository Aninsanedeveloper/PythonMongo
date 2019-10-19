from pymongo import MongoClient #import modules

MONGO_URI = 'mongodb://localhost:27017' #the uri for mongo client where mongodb means protocol, localgost server ip, and 20717 th default port

client = MongoClient(MONGO_URI) 

db = client['smartcontracts'] # createa database you can use whatever you want after you put some data on this
collection = db['customers'] # createa a collection in the db



collection.insert_one({"name": "Marino Salazar"}) #this way is to insert a single item on the collection and can ceate a db
