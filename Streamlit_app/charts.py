import streamlit as st

def show_players_by_genre(df):
    genre_counts = (
        df.groupby("GameGenre")["PlayerID"]
        .nunique()
        .sort_values(ascending=False)
    )
    st.bar_chart(genre_counts)

def show_average_playtime_by_genre(df):
    playtime = (
        df.groupby("GameGenre")["PlayTimeHours"]
        .mean()
        .round(2)
    )
    st.bar_chart(playtime)

def show_players_by_difficulty(df):
    difficulty_counts = (
        df.groupby("GameDifficulty")["PlayerID"]
        .nunique()
        .sort_values(ascending=False)
    )
    st.bar_chart(difficulty_counts)

def show_playtime_category(df):
    category_data = (
        df.groupby("PlaytimeCategory")["PlayerID"]
        .nunique()
        .sort_values(ascending=False)
    )
    st.bar_chart(category_data)

def show_purchase_comparison(df):

    purchase_data = (
        df.groupby("InGamePurchases")["PlayerID"]
        .nunique()
    )

    purchase_data.index = purchase_data.index.map({
        0: "Non-Purchasers",
        1: "Purchasers"
    })

    st.bar_chart(purchase_data)

def show_purchase_rate_by_genre(df):

    purchase_rate = (
        df.groupby("GameGenre")["InGamePurchases"]
        .mean()
        .mul(100)
        .round(2)
    )

    st.bar_chart(purchase_rate)