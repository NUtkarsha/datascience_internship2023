import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv("pub_data.csv")

# Set page title
st.markdown("<h1 style='color: Purple; font-family: Century; font-size: 32px;'>Search Pubs by Postal Code or Local Authority</h1>", unsafe_allow_html=True)


# Create a dropdown menu to select the local authority or postal code
search_type = st.selectbox(
    "Select Search Type", 
    ["Local Authority", "Postal Code"])

# Create a dropdown menu to select the local authority or postal code
if search_type == "Local Authority":
    selected_location = st.selectbox(
        "Select Local Authority", 
        df["local_authority"].unique())
    filtered_df = df[df["local_authority"]==selected_location]
    pubs_found = len(filtered_df)
    st.markdown(f"<p><span style='color: DeepPink;'>{pubs_found}</span> pubs found in <span style='color: DeepPink;'>{selected_location}</span></p>", unsafe_allow_html=True)



else:
    selected_location = st.selectbox(
        "Select Postal Code", 
        df["postcode"].unique())
    filtered_df = df[df["postcode"]==selected_location]
    pubs_found = len(filtered_df)
    st.markdown(f"<p><span style='color: DeepPink;'>{pubs_found}</span> pubs found in <span style='color: DeepPink;'>{selected_location}</span></p>", unsafe_allow_html=True)



# Plot the map
fig = px.scatter_mapbox(filtered_df, lat="latitude", lon="longitude", 
                        hover_name="name", hover_data=["address", "local_authority"], 
                        color_discrete_sequence=["blue"], zoom=10, height=500)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig)

