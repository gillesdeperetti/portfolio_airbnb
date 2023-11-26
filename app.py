# LIBRARIES
from src.utils import *
from src.data_loader import *
from src.visualizations import *
from src.texts import *
from src.config import page_config
from static.styles import *
import streamlit as st
import pandas as pd

st.set_page_config(**page_config)
load_css('static/styles/custom.css')
choose = setup_sidebar()
data = load_data()

# PAGES
if choose == "Introduction":
    st.title('Deep Dive in Airbnb Data')
    st.write(introduction)
    wordcloud_fig = plot_wordcloud(data)
    st.pyplot(wordcloud_fig)

if choose == "Data Overview": 
    st.title('Extraction Transformation Load')

if choose == "Data Visualization":
    st.title('Exploratory Data Analysis')

if choose == "Data to Map":
    st.title('Filter, Find, and Visualize')

if choose == "Modeling":
    st.title('Predictive modeling steps')

if choose == "Try it yourself":
    st.title('Model user interface')

if choose == "Conclusion":
    st.title('Conclusion')
