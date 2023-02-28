import pymongo

# Connect to the local MongoDB instance
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Select the database and collection you want to use
db = client["pizzaRes"]
collection = db["pissa"]

# Perform some database operations
result = collection.find_one({"pizza": "durian"})
