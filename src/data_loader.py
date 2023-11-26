import pandas as pd
import numpy as np
import streamlit as st

def load_data():
    data = pd.read_csv("data/data_augmented.csv")  
    return data


def create_filter_widgets(data):
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
    # Numeric filters 
    filtered_data = data[
        (data['number_of_reviews'] >= number_of_reviews) &
        (data['price_in_euro'] >= price_in_euro)
    ]
    
    # Categorical filters if 'Any' or 'All' is not selected
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

def display_dataframe(data):
    column_config = configure_columns()
    column_order = configure_order()
    st.dataframe(data=data[column_order], column_config=column_config, hide_index=True)
