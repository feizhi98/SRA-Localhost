import streamlit as st
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["pizzaRes"]
collection = db["pissa"] # Replace with the name of your collection

# Check if the connection was successful
if db is not None:
    st.write("Connected to MongoDB!")
else:
    st.write("Failed to connect to MongoDB!")

# Retrieve data from the collection
data = collection.find()

# Display the data in the Streamlit app
for pizza in data:
    st.write(pizza)
