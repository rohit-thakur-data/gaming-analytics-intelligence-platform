import pandas as pd

def load_data():
    df = pd.read_csv("data/player_statistics_cleaned.csv")
    return df