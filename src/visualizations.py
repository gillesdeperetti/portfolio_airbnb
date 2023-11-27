import plotly.express as px
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data()
def plot_wordcloud(data, colormap='viridis'):
    """
    Generate and plot a word cloud based on the textual data in the provided DataFrame.

    :param data: The DataFrame containing text data.
    :param colormap: (Optional) The colormap to use for the word cloud. Default is 'viridis'.

    :return: A matplotlib.figure.Figure object representing the word cloud plot.
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
    """Calculates global mean and median for numerical columns."""
    stats = data.describe().loc[['mean', '50%']]
    return stats

@st.cache_data
def compare_location_statistics(data, global_stats, location):
    """Compares statistics of a given location with global statistics."""
    location_data = data[data['Location'] == location]
    
    if location_data.empty:
        return pd.DataFrame(columns=global_stats.columns)
    
    location_stats = location_data.describe().loc[['mean', '50%']]
    return location_stats

@st.cache_data
def display_location_comparison(data, location):
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

import plotly.express as px

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

    return fig