import streamlit as st
import pandas as pd


st.markdown("<h1 style='text-align: center; color: black;'>MY DATA APP</h1>", unsafe_allow_html=True)

st.markdown("""
This app allows you to download scraped data on articles from coinafrique
* **Python libraries:** base64, pandas, streamlit
* **Data source:** [CoinAfrique](https://sn.coinafrique.com/).
""")


# Fonction de loading des données
def load_(dataframe, title, key) :
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    </style>""", unsafe_allow_html=True)

    if st.button(title,key):
      
        st.subheader('Display data dimension')
        st.write('Data dimension: ' + str(dataframe.shape[0]) + ' rows and ' + str(dataframe.shape[1]) + ' columns.')
        st.dataframe(dataframe)

# définir quelques styles liés aux box
st.markdown('''<style> .stButton>button {
    font-size: 12px;
    height: 3em;
    width: 25em;
}</style>''', unsafe_allow_html=True)

          
# Charger les données 
load_(pd.read_csv('data/Chauss_enfant.csv', encoding='ISO-8859-1'), 'Chaussures data 1', '1')
load_(pd.read_csv('data/Chauss_homme.csv', encoding='ISO-8859-1'), 'Chaussures data 2', '2')
load_(pd.read_csv('data/Vet_enfant.csv', encoding='ISO-8859-1'), 'Vetements data 3', '3')
load_(pd.read_csv('data/Vet_homme.csv', encoding='ISO-8859-1'), 'Vetements data 4', '4')




 


