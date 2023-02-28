import pymongo
client = pymongo.MongoClient('mongodb://localhost:3307/')
db = client.pizzaRes
collection = db.pet
result = collection.find_one({'name': 'John'})
