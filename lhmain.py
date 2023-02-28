import streamlit as st
import pymongo

client = pymongo.MongoClient("mongodb://localhost:123456@localhost:27017/pizzaRes")
db = client["pizzaRes"]
pissa = db["pissa"]

# Accept user input
user_input = st.text_input("Enter data to be stored in MongoDB:")

if st.button("Submit"):
    # Insert the data into MongoDB
    pissa.insert_one({"data": user_input})
    st.success("Data has been stored in MongoDB!")
