import streamlit as st
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["SRA_Project"]

# Accept user input
user_input = st.text_input("Enter data to be stored in MongoDB:")

if st.button("Submit"):
    # Insert the data into MongoDB
    prediction = db["prediction"]
    prediction.insert_one({"data": user_input})
    st.success("Data has been stored in MongoDB!")
