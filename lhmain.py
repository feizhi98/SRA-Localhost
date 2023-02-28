import pymongo
client = pymongo.MongoClient('mongodb://localhost:27017/pizzaRes')
db = client.pizzaRes
collection = db.pet
result = collection.find_one({'name': 'John'})
