import streamlit as st
from data_loader import load_data
from charts import (
    show_players_by_genre,
    show_average_playtime_by_genre,
    show_players_by_difficulty,
    show_playtime_category,
    show_purchase_comparison,
    show_purchase_rate_by_genre
)
from analysis import(
    get_playtime_category_summary,
    get_engagement_summary,
    get_pruchase_comparison,
    get_purchase_rate_by_genre
)

from chatbot import answer_question


st.set_page_config(
    page_title="Gaming Analytics Platform",
    page_icon="🎮",
    layout="wide"
)

df = load_data()

st.title("🎮 Gaming Analytics Platform")
st.write(
    "Interactive gaming analytics using Python, Pandas, and Streamlit."
)

st.write("Players Loaded", df["PlayerID"].count())

total_players = df["PlayerID"].nunique()
average_playtime = df["PlayTimeHours"].mean()
average_sessions = df["SessionsPerWeek"].mean()
average_level = df["PlayerLevel"].mean()
purchase_rate = df["InGamePurchases"].mean() * 100

col1,col2,col3,col4,col5 = st.columns(5)
with col1:
    st.metric("Total Players", f"{total_players:,}")

with col2:
    st.metric("Avg Sessions", f"{average_sessions:.2f}")

with col3:
    st.metric("Avg Playtime", f"{average_playtime:.2f}")

with col4:
    st.metric("Avg Level", f"{average_level:.2f}")

with col5:
    st.metric("Purchase Rate", f"{purchase_rate:.2f}%")

st.subheader("Players by Genre Genre")
show_players_by_genre(df)

st.subheader("Average Platime by Game Genre")
show_average_playtime_by_genre(df)

st.subheader("Players by Difficulty Level")
show_players_by_difficulty(df)

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to:",
    [
        "Overview",
        "Player Engagement",
        "Monetization",
        "Ask a Question"
    ]
)
if page == "Overview":
    st.subheader("Gaming Overview")

    st.subheader("Players by Game Genre")
    show_players_by_genre(df)

    st.subheader("Average Playtime by Game Genre")
    show_average_playtime_by_genre(df)

    st.subheader("Players by Difficulty Level")
    show_players_by_difficulty(df)

elif page == "Player Engagement":
    st.subheader("📈 Player Engagement")

    engagement = get_engagement_summary(df)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Avg Playtime", f"{average_playtime:.2f}")

    with col2:
        st.metric("Avg Sessions", f"{average_sessions:.2f}")

    with col3:
        st.metric("Avg Level", f"{average_level:.2f}")

    st.subheader("Players by Playtime Category")
    show_playtime_category(df)
    
elif page == "Monetization":
    st.subheader("💰 Monetization")

    total_players = df["PlayerID"].nunique()

    purchase_rate = df["InGamePurchases"].mean() * 100

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Players", f"{total_players:,}")

    with col2:
        st.metric("Purchase Rate", f"{purchase_rate:.2f}%")

    st.subheader("Purchasers vs Non-Purchasers")

    show_purchase_comparison(df)

    st.subheader("Purchase Rate by Game Genre")

    show_purchase_rate_by_genre(df)

elif page == "Ask a Question":

    st.subheader("💬 Ask a Question")

    question = st.text_input(
        "Ask something about the gaming data:"
    )

    if st.button("Get Answer"):

        if question:
            answer = answer_question(
                question,
                df
            )
            st.success(answer)

        else:
            st.warning(
                "Please enter a question."
            )

