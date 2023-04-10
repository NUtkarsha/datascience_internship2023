import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('laptop.csv')

st.markdown('<h1 style="color:Indigo;">Price vs Feature</h1>', unsafe_allow_html=True)
st.markdown('<h4 style="color:Olive;">Choose a feature to plot:</h4>', unsafe_allow_html=True)

features = ['brand', 'RAM_GB', 'ROM_GB', 'SSD', 'OS','processor']
selected_feature = st.selectbox('Select a feature', features)
grouped_data = data.groupby(selected_feature).mean()['price'].sort_values(ascending=False)

colors = ['Crimson', 'green', 'orange', 'DarkTurquoise', 'purple', 'HotPink','Maroon','MediumPurple','Navy','Orchid','LawnGreen']

fig, ax = plt.subplots(figsize=(5, 3))
grouped_data.plot(kind='bar', ax=ax, color=colors)
ax.set_xlabel(selected_feature.capitalize(), fontsize=10, color='Purple',weight='bold')
ax.set_ylabel(' Price', fontsize=10, color='Purple',weight='bold') 
ax.set_title(f' Price vs {selected_feature.capitalize()}', fontsize=12, color='darkgreen',weight='bold') 
ax.tick_params(axis='x', labelsize=6)
ax.tick_params(axis='y', labelsize=6)

st.pyplot(fig)
