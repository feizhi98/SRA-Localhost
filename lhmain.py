import streamlit as st
import pymongo

# Get the credentials from the user
username = st.text_input("Enter MongoDB username")
password = st.text_input("Enter MongoDB password", type="password")
database_name = st.text_input("Enter MongoDB database name")

# Connect to MongoDB
client = pymongo.MongoClient(f"mongodb+srv://{localhost}:{123456}@cluster0.mongodb.net/{pizzaRes}?retryWrites=true&w=majority")
db = client[database_name]

# Use the database
collection = db["pissa"]
results = collection.find()
for result in results:
    st.write(result)
