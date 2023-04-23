import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Load the data
df = pd.read_csv("pub_data.csv")

# Set page title
st.markdown("<h1 style='color: Purple; font-family: Century; font-size: 35px;'>Find Nearest Pubs 🥂</h1>", unsafe_allow_html=True)

# Create a dropdown menu to select the latitude and longitude
selected_lat = st.selectbox("Select Latitude", df["latitude"].unique())
selected_lon = st.selectbox("Select Longitude", df["longitude"].unique())

# Display the selected latitude and longitude
st.markdown("<h2 style='font-family: Bahnschrift; font-size:23px;'>Nearest 5 Pubs: </h2>", unsafe_allow_html=True)

# Calculate the Euclidean distance between each pub and the selected location
df["distance"] = ((df["latitude"] - selected_lat)**2 + (df["longitude"] - selected_lon)**2)**0.5

# Sort the dataframe by distance and select the nearest 5 pubs
nearest_pubs = df.sort_values("distance").head(5)

# Display the nearest pubs in a table format
styled_table = nearest_pubs[["name", "local_authority", "distance"]].reset_index(drop=True).style\
    .set_table_styles([{'selector': 'th', 'props': [('font-weight', 'bold')]}])
st.dataframe(styled_table)


# Plot the map
fig = px.scatter_mapbox(nearest_pubs, lat="latitude", lon="longitude", 
                        hover_name="name", hover_data=["address", "local_authority"], 
                        color_discrete_sequence=["blue"], zoom=10, height=500)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig)
