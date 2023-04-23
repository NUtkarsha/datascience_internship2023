import streamlit as st
import pandas as pd

st.markdown("<h1 style='color: Purple; font-family: Century; font-size: 35px;'>Welcome to Pub Finder App 🍺</h1>", unsafe_allow_html=True)
st.markdown("<ul><li><h2 style='font-family: Bahnschrift; font-size:18px;'>This app helps you find pubs in a specific area and shows you the nearest pubs based on your location </h2></li></ul>", unsafe_allow_html=True)

# Add image
image = "https://wp.inews.co.uk/wp-content/uploads/2022/04/PRI_217454067.jpg"
st.image(image, use_column_width=True)    
st.write("This is multipage application consist of three pages 📑")
st.write("📋 First page is of introduction page")
st.write("📋 Second page is search page where user can search pubs by Postal Code or Local Authority")
st.write("📋 Third page is also search page where user can search by longitude and latitude and user get 5 nearest pubs from the location")
st.write(" ")
st.markdown("<p style='font-family: Bahnschrift SemiBold; font-size: 16px; color:Green;'>👉 For complete Code, go through this <a href='https://github.com/yourusername/yourrepository'>LINK</a></p>", unsafe_allow_html=True)
st.write(" ")
st.write(" ")
st.write(" ")
st.markdown("<p style='text-align: center;font-size:18px;font-family: Sitka Small Semibold;'><a href='https://www.linkedin.com/in/utkarshanarkhede/'>LinkedIn</a> | <a href='https://github.com/NUtkarsha'>GitHub</a></p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;font-size:18px;font-family: Sitka Small Semibold;'>Made by <span style='color: FireBrick;'>Utkarsha Narkhede 👩‍💻 </span> & guided by <span style='color: FireBrick;'>Mr. Kanav Bansal 🧑‍🏫 </span></p>", unsafe_allow_html=True)

