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
snapshot_local_vs_global = """
        Focusing on key metrics like pricing and ratings across major European cities, this interactive visualization contrasts local nuances with global dataset averages. It provides a nuanced understanding of how each city's unique Airbnb landscape aligns with, or diverges from, broader global patterns.
        """