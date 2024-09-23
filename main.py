import streamlit as st
from scrape import scrape_website

st.title("AI Web Scrapper")
url = st.text_input("Enter a website URL...")

if st.button("Scrape Site"):
    st.write("Scrape the website")
    result = scrape_website(url)
    print(result)
    
    