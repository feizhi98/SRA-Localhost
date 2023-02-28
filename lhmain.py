import pymongo
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client.pizzaRes
collection = db.pet
result = collection.find_one({'name': 'John'})
