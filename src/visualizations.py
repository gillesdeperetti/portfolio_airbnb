import plotly.express as px
import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import seaborn as sns
from src.utils import *

@st.cache_data()
def plot_wordcloud(data, colormap='viridis'):
    """
    Generates and plots a word cloud based on the textual data in the provided DataFrame.

    Args:
        data (pandas.DataFrame): The DataFrame containing text data.
        colormap (str, optional): The colormap to use for the word cloud. Default is 'viridis'.

    Returns:
        matplotlib.figure.Figure: A matplotlib figure object representing the word cloud plot.
    """

    custom_stopwords = set(STOPWORDS)
    locations = set(data['Location'].unique())
    custom_stopwords.update(locations)
    
    exclusion = ['rental', 'rentals', 'Rent', 'rents', 'Rental', 'rent', 'Rental unit', 'bed', 'beds', 'bath', 'baths', 'bedroom', 'bedrooms', ]
    custom_stopwords.update(exclusion)
    
    wordcloud = WordCloud(width=800, height=450,
                          background_color='white',
                          stopwords=custom_stopwords,
                          colormap=colormap,
                          min_font_size=5).generate(' '.join(data['name']))
    
    fig, ax = plt.subplots(figsize=(8, 4.5), facecolor=None)
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    plt.close(fig)  
    return fig

@st.cache_data
def calculate_global_statistics(data):
    """
    Calculates global mean and median for numerical columns.

    Args:
        data (pandas.DataFrame): The data to calculate statistics for.

    Returns:
        pandas.DataFrame: A DataFrame containing the global mean and median for each numerical column.
    """
    return data.describe().loc[['mean', '50%']]

@st.cache_data
def compare_location_statistics(data, global_stats, location):
    """
    Compares statistics of a given location with global statistics.

    Args:
        data (pandas.DataFrame): The data to compare.
        global_stats (pandas.DataFrame): The global statistics.
        location (str): The location to compare.

    Returns:
        pandas.DataFrame: A DataFrame containing the statistics of the given location compared to the global statistics.
    """

    location_data = data[data['Location'] == location]

    if location_data.empty:
        return pd.DataFrame(columns=global_stats.columns)

    return location_data.describe().loc[['mean', '50%']]

@st.cache_data
def display_location_comparison(data, location):
    """
    Displays a comparison of location statistics with global statistics.

    Args:
        data (pandas.DataFrame): The data to compare.
        location (str): The location to compare.

    Returns:
        list: A list of tuples containing the comparison results.
    """

    global_stats = calculate_global_statistics(data)
    location_stats = compare_location_statistics(data, global_stats, location)

    variables = ['price_in_euro', 'Rating', 'number_of_reviews', 'minimum_nights', 'availability_365', 'Bedrooms', 'Beds', 'Baths']
    comparison_results = []

    for var in variables:
        local_mean = round(location_stats.at['mean', var], 2)
        global_mean = round(global_stats.at['mean', var], 2)
        mean_delta = local_mean - global_mean

        local_median = round(location_stats.at['50%', var], 2)
        global_median = round(global_stats.at['50%', var], 2)
        median_delta = local_median - global_median

        if var == 'price_in_euro':
            local_mean = f"{local_mean}€"
            global_mean = f"{global_mean}€"
            local_median = f"{local_median}€"
            global_median = f"{global_median}€"
        elif var == 'Rating':
            local_mean = f"{local_mean}⭐"
            global_mean = f"{global_mean}⭐"
            local_median = f"{local_median}⭐"
            global_median = f"{global_median}⭐"

        comparison_results.append((f"Mean {var} in {location}", local_mean, mean_delta, "Global Mean", global_mean, f"Median {var} in {location}", local_median, median_delta, "Global Median", global_median))

    return comparison_results

@st.cache_data
def plot_market_dynamics_scatter(grouped_data):
    """
    Plot the market dynamics using a scatter plot with color scale based on availability and size based on ratings.
    
    Args:
    grouped_data (DataFrame): Data with aggregated metrics.

    Returns:
    plotly.graph_objs._figure.Figure: A Plotly figure object.
    """
    fig = px.scatter(
        grouped_data, 
        x='Location', 
        y='Total_Listings',
        size='Average_Reviews',  
        color='Average_Availability',  
        color_continuous_scale=px.colors.diverging.Geyser_r,
    )

    fig.update_layout(
        xaxis_title='City',
        yaxis_title='Total Listings',
        legend_title='Metrics',
        coloraxis_colorbar=dict(title='Average Availability')
    )
    fig.update_layout(height=400)
    return fig

def plot_global_sunburst(data):
    """
    Plots a sunburst chart to visualize global data.

    Args:
        data (pandas.DataFrame): The data to plot.

    Returns:
        plotly.graph_objs._figure.Figure: A Plotly figure object representing the sunburst chart.
    """

    color_sequence = {
        'Private room': '#8338ec',
        'Entire home/apt': '#fb5607',
        'Hotel room': '#ffbe0b',
        'Shared room': '#ff006e',
    }

    fig = px.sunburst(
        data, 
        path=['Location', 'room_type', 'Property Type Cluster'], 
        values='Count',
        color='room_type',  
        color_discrete_map=color_sequence,
        title='Interactive diagram: click on a segment to find out more'
    )

    fig.update_layout(height=600)

    fig.update_traces(textinfo='label+percent parent')
    return fig