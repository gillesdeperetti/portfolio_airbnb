# Deep Dive into Airbnb Data

In this project, I undertake the analysis of Airbnb listings across several major European cities. The data, obtained from [Inside Airbnb](http://insideairbnb.com/get-the-data/), circumvents the challenges of accessing the Airbnb API directly and provides rich datasets for comprehensive analysis.

The goal is to design and execute a complete data processing workflow. This includes the ETL (Extract, Transform, Load) operations for data curation, the development of dynamic visualizations and the construction of machine learning models aimed at predicting listing prices based on various attributes.

## Project Features:

## Implemented Technologies:

- Streamlit for crafting the web application's user interface.
- Pandas for robust data wrangling and manipulation.
- Plotly for dynamic, interactive data visualizations.

## Composition of the Project

The following outlines the structure of the project's directories:

    ├── README.md
    ├── app.py
    ├── data
    │ ├── data_augmented.csv
    │ └── final_dataset.csv
    ├── datasets
    │ ├── amsterdam.csv
    │ ├── barcelona.csv
    │ ├── berlin.csv
    │ ├── brussels.csv
    │ ├── florence.csv
    │ ├── lisbon.csv
    │ ├── london.csv
    │ └── paris.csv
    ├── notebooks
    │ └── ETL.ipynb
    ├── requirements.txt
    ├── src
    │ ├── init.py
    │ ├── config.py
    │ ├── data_loader.py
    │ ├── utils.py
    │ └── visualizations.py
    └── static
    ├── images
    │ ├── airbnb-logo.png
    │ └── logo-AirBnB-Data_Dive.png
    └── styles
    └── custom.css
