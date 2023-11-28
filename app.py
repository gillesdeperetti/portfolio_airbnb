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
    st.write(eda_intro)
    with st.expander("Data Dictionary") : 
        st.write(augmented_data_dictionary)
    st.header('Snapshot: Comparing Local and Global Trends')
    st.write(snapshot_local_vs_global)
    location = st.selectbox('Select Location:', data['Location'].unique())
    comparison_results = display_location_comparison(data, location)

    with st.expander(f"Local Statistics for {location} with Comparisons"):
        for result in comparison_results:
            col1, col2 = st.columns(2)

            var_name = result[0].split()[1]  

            delta_color_mean = "normal" if var_name not in ["minimum_nights", "price_in_euro"] else "inverse"
            delta_color_median = "normal" if var_name not in ["minimum_nights", "price_in_euro"] else "inverse"

            col1.metric(result[0], result[1], f"{result[2]:+.2f}", delta_color=delta_color_mean)
            col2.metric(result[5], result[6], f"{result[7]:+.2f}", delta_color=delta_color_median)

    with st.expander("Global Statistics"):
        for result in comparison_results:
            col1, col2 = st.columns(2)

            col1.metric(result[3], result[4])
            col2.metric(result[8], result[9])
    st.header("Market Dynamics : Supply and Demand across Cities")
    col1, col2 = st.columns([0.6,0.4])
    with col1 : 
        grouped_metrics = calculate_global_metrics(data)
        fig = plot_market_dynamics_scatter(grouped_metrics)
        st.plotly_chart(fig, use_container_width=True)
    with col2 : 
        st.write(market_dynamics_S)
    with st.expander("Detailed analysis"):
        st.write(market_dynamics_A)

    st.header("Global Distribution of Room Types and Property Clusters Across Cities")
    col1, col2 = st.columns([0.6,0.4])
    with col1 : 
        sunburst_data = prepare_data_for_sunburst(data)
        global_fig = plot_global_sunburst(sunburst_data)
        st.plotly_chart(global_fig)
    with col2 : 
        st.write(global_distribution_S)
    with st.expander("Key Observations per City"):
        st.write(global_distribution_A)
    
        
            
if choose == "Data to Map":
    st.title('Filter, Find, and Visualize')

if choose == "Modeling":
    st.title('Predictive modeling steps')

if choose == "Try it yourself":
    st.title('Model user interface')

if choose == "Conclusion":
    st.title('Conclusion')
