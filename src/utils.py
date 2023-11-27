import streamlit as st
from streamlit_option_menu import option_menu
from src.config import *
import pandas as pd
import numpy as np

logo = 'static/images/logo-AirBnB-Data_Dive.png'
airbnb_logo = 'static/images/airbnb-logo.png'

@st.cache_data()
def load_css(file_name):
    with open(file_name, "r") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def setup_sidebar():
    with st.sidebar:
        col1, col2, col3 = st.columns([0.2,0.7,0.2])
        with col2: 
            st.image(logo)
        choose = option_menu("", ["Introduction", "Data Overview", "Data Visualization", "Data to Map", "Modeling", "Try it yourself", "Conclusion"],
                             icons=['house', 'clipboard-data', 'graph-up', 'map', 'cpu-fill', 'braces-asterisk', 'check-circle'],
                             default_index=0,
                             styles={
            "container": {"padding": "5!important", "background-color": "#fafafa"},
            "icon": {"color": babu, "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": '#F0F2F6'},
            "nav-link-selected": {"background-color": foggy},
        }
        )
        

        footer = '''
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

        # About me
        '''
        st.sidebar.markdown(footer, unsafe_allow_html=True)
        st.sidebar.markdown("""
        #### Gilles de Peretti <a href="https://github.com/gillesdeperetti" target="_blank"><i class='fab fa-github'></i></a> <a href="https://www.linkedin.com/in/gilles-de-peretti-8219425a/" target="_blank"><i class='fab fa-linkedin'></i></a>
        """, unsafe_allow_html=True)
        return choose
    
@st.cache_data
def calculate_global_metrics(data):
    """
    Calculate global metrics for market dynamics analysis, including average availability and ratings.
    
    Args:
    data (DataFrame): The Airbnb dataset.

    Returns:
    DataFrame: A DataFrame with aggregated metrics.
    """
    grouped_data = data.groupby('Location').agg(
        Total_Listings=pd.NamedAgg(column='id', aggfunc='count'),
        Average_Availability=pd.NamedAgg(column='availability_365', aggfunc='mean'),
        Average_Reviews=pd.NamedAgg(column='number_of_reviews', aggfunc='mean'),
        Average_Rating=pd.NamedAgg(column='Rating', aggfunc='mean')  
    ).reset_index()

    return grouped_data