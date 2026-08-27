import pandas as pd 
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

print("Connecting to MySQL!")

connection = mysql.connector.connect(
    host=os.getenv("DB_HOST", "localhost"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME", "gaming_analytics_db")
)
query = """
SELECT * FROM player_statistics;
"""

df = pd.read_sql(query, connection)
# Create a copy for cleaning
df_clean = df.copy()

print("=====DATASET OVERVIEW=====")

print("-----First 5 Rows-----")
print(df.head())

print("-----Number of Rows-----")
print("Rows", len(df))

print("Columns Name",df.columns)

print("Data Types",df.dtypes)

print("Rows X Columns")
print(df.shape)

print(df.iloc[0])

print("-----DATA VALIDAtION-----")

print("Missing Values",df.isnull().sum())

print("Duplicate Values",df.duplicated().sum())

print("Total Rows",len(df))
print("Unique PlayerIDs",df["PlayerID"].nunique())
print("Unique InGamePurchase",df["InGamePurchases"].unique())

print("Age")
print("Minimum Age",df["Age"].min())
print("Maximum Age",df["Age"].max())
print("Mean Age",df["Age"].mean())

print("Minimum Playtime:", df["PlayTimeHours"].min())
print("Maximum Playtime:", df["PlayTimeHours"].max())
print("Average Playtime:", df["PlayTimeHours"].mean())

print("Minimum Sessions:", df["SessionsPerWeek"].min())
print("Maximum Sessions:", df["SessionsPerWeek"].max())
print("Average Sessions:", df["SessionsPerWeek"].mean())


# ==============================
# DATA CLEANING
# ==============================

print("===== DATA CLEANING =====")

df_clean = df_clean.drop_duplicates()

df_clean = df_clean[df_clean["Age"] >= 0]
df_clean = df_clean[df_clean["PlayTimeHours"] >= 0]
df_clean = df_clean[df_clean["SessionsPerWeek"] >= 0]

invalid_purchases = (
    ~df_clean["InGamePurchases"].isin([0, 1])
).sum()

print("Invalid Purchase Values:", invalid_purchases)

# ==============================
# CLEANING VERIFICATION
# ==============================

print("===== CLEANED DATASET =====")

print("Original Rows:", len(df))
print("Cleaned Rows:", len(df_clean))

print("Remaining Duplicates:",
      df_clean.duplicated().sum())

print("Remaining Missing Values:")
print(df_clean.isnull().sum())

print("===== DATA TYPES & STANDARDIZATION =====")

print("Data Types:")
print(df_clean.dtypes)

print("InGamePurchases Distribution:")
print(df_clean["InGamePurchases"].value_counts())

print("Genre Distribution:")
print(df_clean["GameGenre"].value_counts())

print("===== GENRE ANALYSIS =====")

genre_players = (
    df_clean
    .groupby("GameGenre")["PlayerID"]
    .nunique()
)

print("Players by Genre:")
print(genre_players)


largest_genre = genre_players.idxmax()
largest_genre_players = genre_players.max()

print("Largest Player Count Genre:", largest_genre)
print("Number of Players:", largest_genre_players)


genre_summary = (
    df_clean
    .groupby("GameGenre")
    .agg(
        TotalPlayers=("PlayerID", "nunique"),
        AveragePlaytime=("PlayTimeHours", "mean"),
        AverageSessions=("SessionsPerWeek", "mean"),
        AverageLevel=("PlayerLevel", "mean")
    )
)

genre_summary = genre_summary.round(2)

genre_summary = genre_summary.sort_values(
    "AveragePlaytime",
    ascending=False
)

print("===== GENRE SUMMARY =====")
print(genre_summary)

print("===== PLAYER ENGAGEMENT ANALYSIS =====")

engagement_summary = df_clean[
    ["PlayTimeHours", "SessionsPerWeek", "PlayerLevel"]
].agg(["min", "max", "mean"])

print(engagement_summary.round(2))

engagement_by_genre = (
    df_clean
    .groupby("GameGenre")
    .agg(
        AveragePlaytime=("PlayTimeHours", "mean"),
        AverageSessions=("SessionsPerWeek", "mean"),
        AverageLevel=("PlayerLevel", "mean")
    )
    .round(2)
)

print("===== ENGAGEMENT BY GENRE =====")
print(engagement_by_genre)

most_played_genre = (
    engagement_by_genre["AveragePlaytime"]
    .idxmax()
)

highest_playtime = (
    engagement_by_genre["AveragePlaytime"]
    .max()
)

print("Most Played Genre:", most_played_genre)
print("Average Playtime:", highest_playtime)

highest_session_genre = (
    engagement_by_genre["AverageSessions"]
    .idxmax()
)

highest_sessions = (
    engagement_by_genre["AverageSessions"]
    .max()
)

print("Highest Session Genre:", highest_session_genre)
print("Average Sessions:", highest_sessions)

df_clean["PlaytimeCategory"] = pd.cut(
    df_clean["PlayTimeHours"],
    bins=[-1, 10, 30, float("inf")],
    labels=["Low", "Medium", "High"]
)

print("===== PLAYTIME CATEGORIES =====")
print(df_clean["PlaytimeCategory"].value_counts())

segment_summary = (
    df_clean
    .groupby("PlaytimeCategory", observed=True)
    .agg(
        TotalPlayers=("PlayerID", "nunique"),
        AveragePlaytime=("PlayTimeHours", "mean"),
        AverageSessions=("SessionsPerWeek", "mean"),
        AverageLevel=("PlayerLevel", "mean"),
        PurchaseRate=("InGamePurchases", "mean")
    )
)

segment_summary["PurchaseRate"] = (
    segment_summary["PurchaseRate"] * 100
)

segment_summary = segment_summary.round(2)

print("===== PLAYER SEGMENT SUMMARY =====")
print(segment_summary)

# Sort the already-computed segment_summary by AveragePlaytime
segment_summary = segment_summary.sort_values(
    "AveragePlaytime",
    ascending=False
)

print("===== SORTED PLAYER SEGMENTS =====")
print(segment_summary)

print("===== PURCHASE ANALYSIS =====")

total_players = df_clean["PlayerID"].nunique()

purchasing_players = (
    df_clean.loc[
        df_clean["InGamePurchases"] == 1,
        "PlayerID"
    ].nunique()
)

print("Total Players:", total_players)
print("Purchasing Players:", purchasing_players)

purchase_rate = (
    purchasing_players / total_players
) * 100

print("Overall Purchase Rate:", round(purchase_rate, 2), "%")

purchase_by_genre = (
    df_clean
    .groupby("GameGenre")
    .agg(
        TotalPlayers=("PlayerID", "nunique"),
        PurchasingPlayers=("InGamePurchases", "sum")
    )
)
purchase_by_genre["PurchaseRate"] = (
    purchase_by_genre["PurchasingPlayers"]
    / purchase_by_genre["TotalPlayers"]
) * 100
purchase_by_genre = purchase_by_genre.round(2)
print("\n===== PURCHASE BY GENRE =====")
print(purchase_by_genre)

highest_purchase_genre = (
    purchase_by_genre["PurchaseRate"].idxmax()
)

highest_purchase_rate = (
    purchase_by_genre["PurchaseRate"].max()
)

print("Highest Purchase Rate Genre:",
      highest_purchase_genre)

print("Purchase Rate:",
      highest_purchase_rate, "%")

purchase_by_segment = (
    df_clean
    .groupby("PlaytimeCategory", observed=True)
    .agg(
        TotalPlayers=("PlayerID", "nunique"),
        PurchasingPlayers=("InGamePurchases", "sum"),
        AveragePlaytime=("PlayTimeHours", "mean"),
        AverageSessions=("SessionsPerWeek", "mean")
    )
)
purchase_by_segment["PurchaseRate"] = (
    purchase_by_segment["PurchasingPlayers"]
    / purchase_by_segment["TotalPlayers"]
) * 100
purchase_by_segment = purchase_by_segment.round(2)
print("===== PURCHASE BY ENGAGEMENT SEGMENT =====")
print(purchase_by_segment)

highest_purchase_segment = (
    purchase_by_segment["PurchaseRate"].idxmax()
)

highest_segment_rate = (
    purchase_by_segment["PurchaseRate"].max()
)

print("Highest Purchasing Segment:",
      highest_purchase_segment)

print("Purchase Rate:",
      highest_segment_rate, "%")

purchase_comparison = (
    df_clean
    .groupby("InGamePurchases")
    .agg(
        Players=("PlayerID", "nunique"),
        AveragePlaytime=("PlayTimeHours", "mean"),
        AverageSessions=("SessionsPerWeek", "mean"),
        AverageLevel=("PlayerLevel", "mean")
    )
)

purchase_comparison = purchase_comparison.round(2)

print("===== PURCHASERS VS NON-PURCHASERS =====")
print(purchase_comparison)

top_genres = (
    genre_summary
    .sort_values("TotalPlayers", ascending=False)
)

print("===== TOP GENRES BY PLAYERS =====")
print(top_genres)

top_purchase_genre = (
    purchase_by_genre
    .sort_values("PurchaseRate", ascending=False)
)

print("===== TOP GENRES BY PURCHASE RATE =====")
print(top_purchase_genre)

most_engaging_genre = (
    genre_summary
    .sort_values("AveragePlaytime", ascending=False)
)

print("===== MOST ENGAGING GENRES =====")
print(most_engaging_genre)

purchase_comparison.to_csv(
    "Python/outputs/purchase_comparison.csv"
)

genre_summary.to_csv(
    "Python/outputs/genre_summary.csv"
)

engagement_summary.to_csv(
    "Python/outputs/engagement_summary.csv"
)
connection.close()
print("\n===================================")
print("PYTHON ANALYSIS COMPLETED")
print("All analysis outputs have been saved.")
print("===================================")
print("\n======================================")
print("   PYTHON PHASE COMPLETED")
print("======================================")
print("Rows:", len(df_clean))
print("Unique Players:", df_clean["PlayerID"].nunique())
print("Duplicate Rows:", df_clean.duplicated().sum())
print("Missing Values:", df_clean.isnull().sum().sum())
print("======================================")

# ==========================================
# LESSON 33 - FILTERING WITH PANDAS
# ==========================================

# 1. High engagement players
high_engagement_players = df[
    df["EngagementLevel"] == "High"
]

print("High Engagement Players:")
print(high_engagement_players)


# 2. Medium engagement players
medium_engagement_players = df[
    df["EngagementLevel"] == "Medium"
]

print("Medium Engagement Players:")
print(medium_engagement_players)


# 3. Low engagement players
low_engagement_players = df[
    df["EngagementLevel"] == "Low"
]

print("Low Engagement Players:")
print(low_engagement_players)


# 4. Players with more than 20 hours of playtime
high_playtime_players = df[
    df["PlayTimeHours"] > 20
]

print("Players with more than 20 hours:")
print(high_playtime_players)


# 5. Players with more than 10 sessions per week
frequent_players = df[
    df["SessionsPerWeek"] > 10
]

print("Players with more than 10 sessions per week:")
print(frequent_players)


# 6. High engagement AND more than 20 hours
high_engagement_high_playtime = df[
    (df["EngagementLevel"] == "High") &
    (df["PlayTimeHours"] > 20)
]

print("High Engagement + High Playtime:")
print(high_engagement_high_playtime)


# 7. High OR Medium engagement
active_players = df[
    (df["EngagementLevel"] == "High") |
    (df["EngagementLevel"] == "Medium")
]

print("High or Medium Engagement Players:")
print(active_players)
