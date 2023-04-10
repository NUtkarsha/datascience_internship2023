import streamlit as st
from PIL import Image

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://img.freepik.com/free-vector/dark-minimal-hexagons-background_79603-1455.jpg");
    
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

st.markdown("""
<style>
.title {
    font-size: 38px;
    color: Violet;
    text-align: center;
}
.description {
    font-size: 22px;
    color:White;
    text-align: center;
}
.attribution {
    font-size: 20px;
    color: white;
    text-align: center;   
}

</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>Welcome to Laptop Price Prediction App!</h1>", unsafe_allow_html=True)
st.write(" ")
image = Image.open("Laptop-For-Sale-in-Nairobi-1.webp")
st.image(image,width=700)
st.write(" ")
st.markdown("<p class='description'>This app contains three pages:</p><ol class='description'><li>On the first page, you can get information about laptops based on your price range.</li><li>On the second page, you can predict the price of a laptop based on its features.</li><li>On Third page, you can plot the price of laptops with different features.</li></ol>", unsafe_allow_html=True)
st.write(" ")
st.markdown("<p style='font-size: 18px; color: Coral;text-align: center;'>For complete documentation, follow this <a href='https://github.com/NUtkarsha/datascience_internship2023/tree/main/Laptop%20price%20prediction'>link</a></p>", unsafe_allow_html=True)
st.write(" ")
st.markdown("<p style='font-size: 16px; color: LightGreen;'>Are you ready to use this app&#x2753</p>", unsafe_allow_html=True)
ready_button = st.button("Yes")

if ready_button:
    st.balloons()
    st.write("Let's go!") 
set_bg_hack_url()   

st.markdown("<p class='attribution'><a href='https://www.linkedin.com/in/utkarshanarkhede/'>LinkedIn</a> | <a href='https://github.com/NUtkarsha'>GitHub</a></p>", unsafe_allow_html=True)

st.markdown("<p class='attribution'>Made by <span style='color: Cyan; '>Utkarsha Narkhede</span>  &  guided by <span style='color: Cyan;'>Mr. Kanav Bansal</span></p>", unsafe_allow_html=True)

