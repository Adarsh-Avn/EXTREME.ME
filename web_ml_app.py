import numpy as np
import pickle
import pandas as pd

import streamlit as st

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

def predict_note_Bank(variance,skewness,curtosis,entropy):
    
    
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction


def main():
    st.title("Bank")
    html_temp="""
    <div style="background-color:green;padding:10px">
    <h2 style="color:black;text-align:center;">Streamlit BANK </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("variance","type here")
    skewness = st.text_input("skewness","type here")
    curtosis = st.text_input("curtosis","type here")
    entropy = st.text_input("entropy","type here")
    result=""
    if st.button("predict"):
        result=predict_note_Bank(variance,skewness,curtosis,entropy)
    st.success('the output is {}'.format(result))

if __name__=='__main__':
    main()