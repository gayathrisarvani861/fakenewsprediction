import numpy as np
import pickle
import pandas as pd
import streamlit as st 
import os



pickle_in=open("fakenews.pkl","rb")
model=pickle.load(pickle_in)



def welcome():
    return "Welcome All"


def predict_stock(ORIGINAL):
    prediction=model.predict([[ORIGINAL]])
    print(prediction)
    return prediction


def main():
    """st.title( ")"""
    html_temp = """
    <div style="background-color:black;padding:10px">
    <h2 style="color:white;text-align:center;">MPG Prediction Using Streamlit </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    ORIGINAL = st.text_input("Please enter news")
    
    result=""
    if st.button("Predict"):
        result=predict_stock(ORIGINAL)
    st.success('The news is {}'.format(result))
    

     
    
if __name__=='__main__':
    main()