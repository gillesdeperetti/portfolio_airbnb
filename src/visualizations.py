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