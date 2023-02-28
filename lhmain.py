import streamlit as st
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["pizzaRes"]

# Check if the connection was successful
if db is not None:
    st.write("Connected to MongoDB!")
else:
    st.write("Failed to connect to MongoDB!")
