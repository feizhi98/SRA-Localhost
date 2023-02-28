import streamlit as st
import pymongo

client = pymongo.MongoClient("mongodb://localhost:123456@localhost:27017/pizzaRes")
db = client["pizzaRes"]
pissa = db["pissa"]

# Accept user input
user_input = st.text_input("Enter data to be stored in MongoDB:")

if st.button("Submit"):
    try:
        # Insert the data into MongoDB
        pizza.insert_one({"data": user_input})
        st.success("Data has been stored in MongoDB!")
    except pymongo.errors.PyMongoError as e:
        st.error("An error occurred while storing the data in MongoDB:", e)
    finally:
        # Close the MongoDB client connection
        client.close()
