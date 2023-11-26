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
    st.write(starting_point)
    with st.expander('Raw data & Data Dictionary'):
        st.dataframe(pd.read_csv('data/final_dataset.csv'))
        st.write("### Data Dictionary")
        st.markdown(data_dictionary)
    st.header("ETL Phase")
    with st.expander ("Data extraction and streamlining"):
        st.write(etl_process)
    st.header("Explore the Augmented Dataset")
    with st.expander("Augmented dataset"): 
        filters = create_filter_widgets(data)
        filtered_data = apply_filters(data, *filters)
        display_dataframe(filtered_data)

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
