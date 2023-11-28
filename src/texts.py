introduction = """
        In this project, I undertake the analysis of Airbnb listings across several major European cities. The data, obtained from [Inside Airbnb](http://insideairbnb.com/get-the-data/), circumvents the challenges of accessing the Airbnb API directly and provides rich datasets for comprehensive analysis.

        The goal is to design and execute a complete data processing workflow. This includes the ETL (Extract, Transform, Load) operations for data curation, the development of dynamic visualizations using **Plotly**, and the construction of machine learning models aimed at predicting listing prices based on various attributes.

        I started with datasets from eight iconic cities: **Florence, Amsterdam, Brussels, Barcelona, Lisbon, Berlin, Paris, and London**. These datasets are well-suited for thorough data analysis and visualization tasks.

        The consolidation of these datasets resulted in a combined dataset with **17 features encompassing a total of 237,238 Airbnb listings**. Among these, the "name" feature, although seemingly unprocessed, revealed a treasure trove of insights.

        ## Exploring the `Name` Variable: A Glimpse Into Data Diversity
        """

starting_point = """        
        Starting from a collection of independent datasets for each city, my initial step was to amalgamate these distinct files into a unified DataFrame. This consolidation was crucial, as it facilitated a holistic view of the data, allowing for more coherent analysis and manipulation.

        Those datasets are stored In the `datasets` directory. Each file corresponds to a specific city and contains the listings relevant to that locality.

        As the foundation of this project's data analysis segment, the combined DataFrame represents not just a collection of numbers and strings, but the starting point from which actionable insights and predictive models will be derived. 

        ## Explore the raw data 
        """

data_dictionary = """ 
        - `id`: Identifier number of the listing (numeric).
        - `name`: The name or title of the listing (text).
        - `host_id`: Identifier number of the host (numeric).
        - `host_name`: Name of the host (text).
        - `neighbourhood`: Neighborhood of the property (text).
        - `neighbourhood_group` The neighbourhood as geocoded using the latitude and longitude (text).
        - `latitude` and `longitude`: Geographical coordinates of the property (numeric).
        - `room_type`: Type of room offered (text, categorical).
        - `price`: Price per night (numeric). 
        - `minimum_nights`: Minimum number of nights required (numeric).
        - `number_of_reviews`: Total number of reviews (numeric).
        - `last_review`: Date of the last review (date).
        - `reviews_per_month`: Number of reviews per month (numeric).
        - `availability_365`: Number of days available over the next 365 days (numeric).
        - `number_of_reviews_ltm`: Number of reviews in the last 12 months (numeric).
        - `license`: The licence/permit/registration number (text).
        """

etl_process = """
        The Extract, Transform, Load (ETL) phase is a pivotal component in the lifecycle of data analysis. During this initial phase of the project, I delved deep into the dataset and unearthed several key insights that were instrumental in refining the data for further exploration:

        - Upon examination, I discovered that the fields `neighborhood_group` and `license` were predominantly filled with NaN (not a number) values. The substantial presence of these missing values necessitated a decision regarding their utility and relevance.

        - Due to the dataset's international scope and the availability of precise geolocation data, the `license` variable, which is subject to local regulations, and `neighborhood_group` were found to be non-essential and thus omitted.

        - A correlation check between the `Last_review` and `reviews_per_month` fields was carried out to verify that the NaNs in these two related fields had the same number of N.A. values. 

        - The `name` variable emerged as a surprisingly rich source of nuanced data. Through careful parsing, it was possible to extrapolate new variables indicative of the `Housing Types`, `Property Type Clusters`, number of `bedrooms`, `beds`, `baths` and `ratings`.

        - City identification was another critical step in the data cleaning process. When possible, cities were directly extracted from the `name` field. In cases where the city information was not explicit, it was inferred from the `neighborhood` field. A small fraction of listings (2.4%) that could not be reliably associated with a city were excluded from the dataset to maintain integrity.

        - For the sake of consistency and comparative analysis, all listing prices were converted to euros. The `price_in_euro` field was carefully examined for outliers, which were then cleansed using the Interquartile Range (IQR) method. Additionally, listings with a price of zero were considered inaccurate representations and were thus removed.

        - Data type integrity is crucial for accurate analysis. As such, each variable's data type was meticulously reviewed and realigned to ensure consistency and accuracy in the dataset.

        The detailed methodology and the meticulous steps undertaken in the ETL phase are thoroughly documented. For an in-depth review of this process, the [ETL Notebook can be accessed here](https://github.com/gillesdeperetti/portfolio_airbnb/blob/master/notebooks/ETL.ipynb).

        """

eda_intro = """
        We're now going to explore and visualize the data offered by our augmented dataset. We're going to start with general insights, and then move on to more specific ones. The aim is to understand our data and think about which features to select or which particularities to take into account for the next stage, which will be modeling. 

        If required, the data dictionary attached to this data visualization is available below. 
        """
snapshot_local_vs_global = """
        Focusing on key metrics like pricing and ratings across major European cities, this interactive visualization contrasts local nuances with global dataset averages. It provides a nuanced understanding of how each city's unique Airbnb landscape aligns with, or diverges from, broader global patterns.
        """
augmented_data_dictionary = """ 
        - `id`: Identifier number of the listing (numeric).
        - `name`: The name or title of the listing (text).
        - `host_id`: Identifier number of the host (numeric).
        - `host_name`: Name of the host (text).
        - `calculated_host_listings_count`: Number of listings for an host_id (numeric).
        - `neighbourhood`: Neighborhood of the property (text).
        - `latitude` and `longitude`: Geographical coordinates of the property (numeric).
        - `Location`: The city of the listing (Text). 
        - `room_type`: Type of room offered (text, categorical).
        - `Bedrooms` and `Beds` The number of Bedrooms, Beds and Baths associated to the listing (numeric). 
        - `Baths` The number of bathrooms / toilets associated to the listing (numeric).
        - `price`: Price per night in local currency (numeric). 
        - `price_in_euros`: Price per night in Euros (numeric).
        - `Housing Types`: Type of accommodation from ad title, e.g. Condo, Chalet, Yurt... (Text).
        - `Property Type Cluster`: Accommodation category, grouping of accommodation types into clusters, for example: Waterfront Lodgings, Apartments, Unique and Unusual Lodgings... (Text).
        - `minimum_nights`: Minimum number of nights required (numeric).
        - `number_of_reviews`: Total number of reviews (numeric).
        - `last_review`: Date of the last review (date).
        - `reviews_per_month`: Number of reviews per month (numeric).
        - `availability_365`: Number of days available over the next 365 days (numeric).
        - `number_of_reviews_ltm`: Number of reviews in the last 12 months (numeric).
        """

market_dynamics_A = """
        - **Amsterdam** has a relatively low total of listings with moderate availability and a high average number of reviews per listing. Its average rating is very high, suggesting that while there may not be as many options as in some other cities, the quality of the stays is highly regarded.

        - **Barcelona** shows a high number of total listings with more availability than Amsterdam, but a lower average number of reviews and rating, which might indicate a more competitive market with more choices for consumers.

        - **Berlin** has a moderate number of listings and availability, with fewer reviews on average and a high rating. This suggests a balanced market with a good reputation for quality stays.

        - **Brussels** has the lowest number of listings among the provided cities, yet has a high availability and a moderate number of reviews and rating, pointing towards a less saturated market.

        - **Florence** has a high number of listings with a high availability and the highest average number of reviews, coupled with a high rating, indicating a popular and well-reviewed market for Airbnb stays.

        - **Lisbon** also has a high number of listings and the highest average availability, with the highest number of reviews on average and a good rating, which might reflect a tourist-friendly market with a lot of choices and frequent stays.

        - **London** boasts the highest number of listings by far but has moderate availability and the lowest average number of reviews, along with a solid average rating. This could indicate a highly diverse market where guests have a plethora of options and possibly shorter stays.

        - **Paris** has slightly fewer listings than London but less availability and slightly more reviews on average, with a high rating as well. This could suggest a high demand for listings in Paris, with consistent quality experiences.
        """
market_dynamics_S = """
        In summary, we can suggests that : 

        - Larger cities like *London* and *Paris* have a **vast number of listings and high demand**, reflected in lower availability and a larger spread in the quality of experiences. 
        
        - Smaller cities or those with fewer listings like *Brussels* and *Amsterdam* may offer **higher quality stays** on average, as reflected in their high ratings. 
        
        - Cities like *Lisbon* and *Florence*, with **high availability and many reviews, might have a seasonal market** with a lot of tourism and frequent turnover of guests.
        """
global_distribution_S = """
        ### Individual vs. Shared Accommodations:

        - **'Entire home/apt'** room types are most prevalent across all cities, indicating a strong preference for individual accommodations.
        - 'Private room' is the second most common, suggesting that shared accommodations also have a market, albeit smaller.
        - 'Shared room' types are the least common across all cities.
        - **London** and **Paris** show the highest counts for 'Entire home/apt', suggesting a significant demand for individual accommodations.
        - 'Hotel room' types are minimal but are more noticeable in Paris, likely due to its significant tourism industry.

        ### Standard vs. Unique Accommodations:

        - **Standard** accommodations, which include categories like 'Apartments', 'Private Houses', and 'Urban Accommodations', overwhelmingly dominate in all cities.
        - **Unique** accommodations make up a small percentage of the listings, offering niche options for those seeking different experiences.

        """

global_distribution_A = """
        - **Amsterdam:** A mix of individual and shared accommodations with a very small portion of unique accommodations.

        - **Barcelona:** A strong preference for individual accommodations with very few unique options.

        - **Berlin:** Similar to Barcelona with a slightly higher percentage of shared accommodations.

        - **Brussels:** Higher percentages of individual accommodations, with a small market for unique accommodations.

        - **Florence:** Dominance of individual accommodations with few unique options.

        - **Lisbon:** A large market for individual accommodations with minimal unique accommodations.

        - **London:** The largest market for individual accommodations among the cities listed.

        - **Paris:** The highest count of individual accommodations and a noticeable presence of hotel rooms, indicating a robust tourism sector.
        """