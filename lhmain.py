import pymongo
import streamlit as st

# Define MongoDB connection string
MONGODB_CONNECTION_STRING = 'mongodb://localhost:27017'

# Connect to MongoDB and get pet collection
client = pymongo.MongoClient(MONGODB_CONNECTION_STRING)
db = client.pizzaRes
collection = db.pet

# Define Streamlit interface for adding a pet document
st.write('Add a new pet:')
name = st.text_input('Name')
pet = st.text_input('Pet')


# Add pet document to collection when submit button is clicked
if st.button('Submit'):
    pet = {
        'name': name,
        'pet': pet,

    }
    collection.insert_one(pet)
    st.write('Pet added successfully!')
