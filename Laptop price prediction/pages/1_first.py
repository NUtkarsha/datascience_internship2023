import streamlit as st
import pandas as pd

st.markdown(
    """
    <style>
    h1 {
        color: Indigo;
    }
    .element-container h2 {
        font-size: 25px;
        color:Olive;
    }
       .min-price {
        font-weight: bold;
        color: Green;
    }
    .max-price {
        
        font-weight: bold;
        color: Green;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title('Price & Features')


df = pd.read_csv('laptop.csv')

st.header('Select Price Range and You will Get Various Options for Laptops')
min_price = st.number_input('Minimum price', value=df.price.min())
max_price = st.number_input('Maximum price', value=df.price.max())
apply_button = st.button('Apply')


if apply_button:
    filtered_df = df[(df['price'] >= min_price) & (df['price'] <= max_price)]
    st.write('Showing laptops with price between <span class="min-price">' + str(min_price) + '</span> and <span class="max-price">' + str(max_price) + '</span>', unsafe_allow_html=True)
    st.write(filtered_df)
