import pandas as pd
import numpy as np
import streamlit as st

def load_data():
    """
    Loads data from a CSV file.

    Returns:
        pandas.DataFrame: The loaded data.
    """
    return pd.read_csv("data/data_augmented.csv")


def create_filter_widgets(data):
    """
    Creates filter widgets for data exploration.

    Args:
        data (pandas.DataFrame): The data to create filter widgets for.

    Returns:
        tuple: A tuple containing the selected filter values.
    """

    location = st.selectbox('Location', ['All'] + sorted(data['Location'].unique().tolist()))
    col1, col2 = st.columns([1, 1])
    with col1:
        number_of_reviews = st.slider('Number of Reviews >=', 0, int(data['number_of_reviews'].max()), 0)
        price_in_euro = st.slider('Price in Euro >=', 0, int(data['price_in_euro'].max()), 0)
    with col2:
        bedrooms = st.selectbox('Bedrooms', ['Any'] + sorted(data['Bedrooms'].unique().tolist()))
        baths = st.selectbox('Baths', ['Any'] + sorted(data['Baths'].unique().tolist()))

    return number_of_reviews, price_in_euro, bedrooms, baths, location

def apply_filters(data, number_of_reviews, price_in_euro, bedrooms, baths, location):
    """
    Applies filters to the data.

    Args:
        data (pandas.DataFrame): The data to apply filters to.
        number_of_reviews (int): The minimum number of reviews.
        price_in_euro (int): The minimum price in Euros.
        bedrooms (str): The selected number of bedrooms.
        baths (str): The selected number of baths.
        location (str): The selected location.

    Returns:
        pandas.DataFrame: The filtered data.
    """

    filtered_data = data[
        (data['number_of_reviews'] >= number_of_reviews) &
        (data['price_in_euro'] >= price_in_euro)
    ]
    
    if bedrooms != 'Any':
        filtered_data = filtered_data[filtered_data['Bedrooms'] == bedrooms]
    if baths != 'Any':
        filtered_data = filtered_data[filtered_data['Baths'] == baths]
    if location != 'All':
        filtered_data = filtered_data[filtered_data['Location'] == location]
    
    return filtered_data

def configure_columns():
    return {
        'id': st.column_config.TextColumn("ID"),
        'host_id': st.column_config.TextColumn("Host ID"),
        'latitude': st.column_config.NumberColumn("Latitude"),
        'longitude': st.column_config.NumberColumn("Longitude"),
        'minimum_nights': st.column_config.NumberColumn("Minimum Nights"),
        'availability_365': st.column_config.NumberColumn("Availability (days)"),
        'number_of_reviews': st.column_config.NumberColumn("Total Reviews"),
        'number_of_reviews_ltm': st.column_config.NumberColumn("Reviews (Last 12M)"),
        'last_review': st.column_config.DateColumn("Last Review"),
        'reviews_per_month': st.column_config.NumberColumn("Reviews per Month"),
        'price_in_euro': st.column_config.NumberColumn("Price (€)", format="€%d"),
        'room_type': st.column_config.SelectboxColumn(label='Room Type', options=['Private room', 'Entire home/apt', 'Shared room']),
        'Rating': st.column_config.ProgressColumn(label='Rating', format='%d⭐',width='medium', min_value=0, max_value=5),
        'calculated_host_listings_count': st.column_config.NumberColumn("Number of host listings"),
        'name': st.column_config.TextColumn("Listing name"),
        'host_name': st.column_config.TextColumn("Host name"),
        'neighbourhood': st.column_config.TextColumn("Neighborhood"),
        'Housing types': st.column_config.TextColumn("Housing Types"),
        'Property Type Cluster': st.column_config.TextColumn("Property Type Cluster")
    }

def configure_order():
    return [
    'id', 'name', 'host_id', 'host_name', 'calculated_host_listings_count',
    'neighbourhood', 'Location', 'latitude', 'longitude',
    'room_type', 'Housing types', 'Property Type Cluster', 'Bedrooms', 'Beds', 'Baths',
    'minimum_nights', 'availability_365',
    'number_of_reviews', 'number_of_reviews_ltm', 'last_review', 'reviews_per_month', 'Rating',
    'price_in_euro'
]

@st.cache_data
def display_dataframe(data):
    column_config = configure_columns()
    column_order = configure_order()
    st.dataframe(data=data[column_order], column_config=column_config, hide_index=True)

@st.cache_data
def calculate_global_metrics(data):
    """
    Calculate global metrics for market dynamics analysis, including average availability and ratings.

    Args:
    data (DataFrame): The Airbnb dataset.

    Returns:
    DataFrame: A DataFrame with aggregated metrics.
    """
    return (
        data.groupby('Location')
        .agg(
            Total_Listings=('id', 'count'),
            Average_Availability=('availability_365', 'mean'),
            Average_Reviews=('number_of_reviews', 'mean'),
            Average_Rating=('Rating', 'mean'),
        )
        .reset_index()
    )

@st.cache_data
def prepare_data_for_sunburst(data):
    """
    Prepare data for sunburst chart, calculating percentages within each property type cluster.

    Args:
    data (DataFrame): The Airbnb dataset.

    Returns:
    DataFrame: A DataFrame suitable for sunburst chart visualization.
    """
    sunburst_data = data.groupby(['Location', 'Property Type Cluster', 'room_type']).size().reset_index(name='Count')

    cluster_total = sunburst_data.groupby(['Location', 'Property Type Cluster'])['Count'].transform('sum')
    sunburst_data['Percentage'] = (sunburst_data['Count'] / cluster_total) * 100

    return sunburst_data