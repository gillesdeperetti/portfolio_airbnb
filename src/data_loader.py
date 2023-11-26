import pandas as pd
import numpy as np
import streamlit as st

def load_data():
    data = pd.read_csv("data/data_augmented.csv")  
    return data