#Using Streamlit

import numpy as np
import pickle
import pandas as pd
from flasgger import Swagger
import streamlit as st

from PIL import Image


pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)


def predict_note_authentication(variance, skewness, curtosis, entropy):
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    print(prediction)
    return prediction

def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Bank Note Authenticator ML App using Streamlit </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    variance = st.text_input("Variance")
    skewness = st.text_input("skewness")
    curtosis = st.text_input("curtosis")
    entropy = st.text_input("entropy")
    result = ""
    if st.button("Predict"):
        result = predict_note_authentication(variance, skewness, curtosis, entropy)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
    
