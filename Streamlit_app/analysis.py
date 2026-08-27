import pandas as pd

def get_engagement_summary(df):

    summary = {
        "Average Playtime": df["PlayTimeHours"].mean(),
        "Average Sessions": df["SessionsPerWeek"].mean(),
        "Average Level": df["PlayerLevel"].mean()
    }
    return summary

def get_playtime_category_summary(df):
    summary = (
        df.groupby("PlaytimeCategory")
        .agg(
            Players=("PlayerID", "nunique"),
            AveragePlayTime=("PlayTimeHours", "mean"),
            AverageSessions=("SessionsPerWeek", "mean"),
            AverageLevel=("PlayerLevel", "mean"),
        )
        .round(2)
    )
    return summary

def get_pruchase_comparison(df):
    comparison = (
        df.groupby("InGamePurchases")
        .agg(
            Players=("PlayerID", "nunique"),
            AveragePlayTime=("PlayTimeHours", "mean"),
            AverageSessions=("SessionsPerWeek", "mean"),
            AverageLevel=("PlayerLevel", "mean"),
        )
        .round(2)
    )
    return comparison

def get_purchase_rate_by_genre(df):

    purchase_rate = (
        df.groupby("GameGenre")["InGamePurchases"]
        .mean()
        .mul(100)
        .round(2)
    )

    return purchase_rate