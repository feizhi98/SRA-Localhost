import pymongo
client = pymongo.MongoClient('mongodb://localhost:3306/')
db = client.pizzaRes
collection = db.pet
result = collection.find_one({'name': 'John'})
