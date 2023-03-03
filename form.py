import streamlit as st
import datetime

st.title("Form for the Users")
st.write("Fill the form carefully.")

Name = st.text_area("Name", value="Your Name")
info = st.text_area("Share some information about you", "Info here",
                    help='You can write about your hobbies or family')
age = st.number_input("Age", min_value=18, max_value=100, step=1)
birth_date = st.date_input("Date of Birth", min_value=datetime.date(1980, 1, 1),
                           max_value=datetime.date(2023, 12, 31))
smoke = st.selectbox("Do you smoke?",
                     options=['Yes','No','frequent'])
genre = st.radio("Which movie genre do you like?",
                 options=['horror', 'adventure', 'romantic','suspense'])
weight = st.slider("Choose your weight in kg", min_value=40, max_value=150, step=1)
height = st.slider("Choose your height in cm", min_value=120, max_value=200, step=1)
colors = st.multiselect('What are your favorite colors',
                        options=['Green', 'Yellow', 'Red', 'Blue', 'Pink'])
image = st.file_uploader("Upload your photo", type=['jpg', 'png'])


submit = st.button("Submit")

if submit:
    st.write("You submit the form successfully")
    st.write("please click the button shown at sidebar to see your form ")

click = st.sidebar.button('Click me!')
if click:
    st.sidebar.write("Your form ")
    st.sidebar.write("Name:",Name)
    st.sidebar.write("info:",info)
    st.sidebar.write("age :" ,age)
    st.sidebar.write("Birth Date: ",birth_date)
    st.sidebar.write("Smoker: ",smoke)
    st.sidebar.write("weight :" ,weight)
    st.sidebar.write("height :" ,height)
    st.sidebar.write("Colours : ",colors)
    st.sidebar.write("Thank You!")
    st.balloons()