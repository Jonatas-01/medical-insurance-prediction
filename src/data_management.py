import streamlit as st
import pandas as pd
import joblib

# load data
@st.cache_data
def load_data():
    df = pd.read_csv('outputs/datasets/collection/insurance.csv')
    return df

# load model
def load_pkl_file(file_path):
    return joblib.load(file_path)