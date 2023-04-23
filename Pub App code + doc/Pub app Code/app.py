import streamlit as st
st.markdown("<h1 style='color: Brown; font-family: Century; font-size: 35px;text-align: center;'>~ About ~</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='font-family: Bahnschrift;color: Green; font-size:20px;'>Scenario:</h2>", unsafe_allow_html=True)
st.write('''Let’s assume you are on a vacation in the United Kingdom with your friends. For fun, you
decided to go to the Pubs nearby for some drinks. Google Map is down because of some
issues.
While searching the internet, you came across https://www.getthedata.com/open-pubs. On
this website, you found all the pub locations (Specifically Latitude and Longitude info). In order
to impress your friends, you decided to create a web application with the data available in your
hand''')
st.markdown(" 👉For complete project documentation, click on [this link](https://docs.google.com/document/d/1UpZY1vOPkyAwJMsb6dOGWMc8pRTdhGE1_MHOFH-VgNg/edit?usp=sharing)")
st.markdown("<h2 style='font-family: Bahnschrift;color: Green; font-size:20px;'>Dataset Info:</h2>", unsafe_allow_html=True)
st.write("➡️ The dataset consist of 50564 rows and 9 columns.")
st.write("➡️ Columns are as follow:")
st.write("<ul><li>Food Standard Agency's ID for this pub (fsa_id)</li><li>Name of pub</li><li>Address fields</li><li>Postcode of pub</li><li>Easting</li><li>northing</li><li>Latitude</li><li>Longitude</li><li>Local authority this pub falls under</li></ul>", unsafe_allow_html=True)