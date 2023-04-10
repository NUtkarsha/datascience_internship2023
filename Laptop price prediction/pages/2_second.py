import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor

df = pd.read_csv('laptop.csv')

cat_cols = ['brand', 'processor', 'OS']
encoders = {}
for col in cat_cols:
    encoders[col] = LabelEncoder()
    df[col] = encoders[col].fit_transform(df[col].values.reshape(-1,1))

y = np.log(df['price'])
X = df.drop(columns=['price'])

model = XGBRegressor(learning_rate=0.05, max_depth=5, n_estimators=200, random_state=0)
model.fit(X, y)

brands = encoders['brand'].inverse_transform(df['brand'].unique())
rams = df['RAM_GB'].unique()
roms = df['ROM_GB'].unique()
processors = encoders['processor'].inverse_transform(df['processor'].unique())
oss = encoders['OS'].inverse_transform(df['OS'].unique())
ssds = df['SSD'].unique()

title_style = 'font-size: 40px; color: Indigo;'
header_style = 'font-size: 25px;color: Olive;'

st.markdown(f'<h1 style="{title_style}">Laptop Price Predictor</h1>', unsafe_allow_html=True)
st.markdown(f'<p style="{header_style}">Please select the options below to predict the price of a laptop.</p>', unsafe_allow_html=True)

brand = st.selectbox('Brand', brands)
ram = st.selectbox('RAM (GB)', rams)
rom = st.selectbox('ROM (GB)', roms)
processor = st.selectbox('Processor', processors)
os = st.selectbox('Operating System', oss)
ssd = st.selectbox('SSD', ssds)

brand_encoded = encoders['brand'].transform([brand])[0]
processor_encoded = encoders['processor'].transform([processor])[0]
os_encoded = encoders['OS'].transform([os])[0]

if st.button('Show price '):
  
    input = pd.DataFrame({'brand': [brand_encoded], 'RAM_GB': [ram], 'ROM_GB': [rom],
                          'processor': [processor_encoded], 'OS': [os_encoded], 'SSD': [ssd]})
    input = input[X.columns]  
    prediction = np.exp(model.predict(input))[0]

    st.markdown(f'<h3 style="font-size: 20px;">The predicted price of this laptop is <span style="color: Green; font-size: 24px;">₹{prediction:.2f}</span></h3>', unsafe_allow_html=True)


