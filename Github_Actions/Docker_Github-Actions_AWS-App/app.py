from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image


load_dotenv() #loading all the environment variables

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# function to load Gemini model and get responses
model = genai.GenerativeModel('gemini-pro-vision')

def get_response(input,image):
    if input != "":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

#Initialize a Streamlit App

st.set_page_config(page_title="Book Vision", page_icon="📚")
st.title("Book Vision 📚")
st.markdown("BookVision is a cutting-edge application designed to generate detailed summaries  of books from images  using advanced AI technology. Leveraging the power of the Google Gemini Vision Pro model, BookVision transforms images of book pages into concise and informative summaries, making it easier for users to grasp the essence of a book quickly.")
"[![Open in GitHub](https://github.com/codespaces/badge.svg)](https://github.com/Raghul-M/Bookvision/)"

def github():
        badge(type="github", name="streamlit/streamlit")

input='''Give a detailed summary about the book . If the image is not book Answer Sorry Its not the image of book . Dont generate anything random about the image .Ask the user to
 upload book image with the visibility of Book Title'''
uploaded_file = st.file_uploader("Choose an image..", type=["jpg", "jpeg", "png"])
image=""
submit=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', width=300)

if image != "":
    submit = st.button("Submit")

if submit:
    try:
        response = get_response(input, image)
        if response:
            st.subheader("Book Summary....")
            st.write(response)
        else:
            st.subheader("Sorry! We are unable to generate a summary for this book. Please try later or with a better quality image.")
    except InternalServerError:
        st.subheader("Sorry! We are experiencing technical difficulties. Please try again later.")
    except Exception as e:
        st.subheader("An unexpected error occurred: {}".format(e))
