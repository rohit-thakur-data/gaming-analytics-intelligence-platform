import pandas as pd

def answer_question(question,df):

    question = question.lower()

    if (
        "average play time" in question
        or "average playtime" in question
        or "average gaming time" in question
    ):
        
        average_play_time = df["PlayTimeHours"].mean()

        return f"Average Play Time is {average_play_time:.2f} Hours."

    elif (
        "total players" in question
        or "number of players" in question
        or "how many players" in question
    ):
        
        total_plaeyrs = len(df)

        return f"Total number of Players is {total_plaeyrs}."

    elif (
        "purchase" in question
        or "purchased" in question
        or "bought" in question
        or "buy" in question
    ):
        
        purchasers = (
            df["InGamePurchases"] == 1
        ).sum()

        return f"Number of players who made a purchase is {purchasers}."

    elif (
        "average sessions" in question
        or "average session" in question
        or "sessions per week" in question
    ):

        average_sessions = df["SessionsPerWeek"].mean()

        return f"Average Sessions Per Week is {average_sessions:.2f}."

    elif (
        "average leve" in question
        or "player level" in question
        or "average player level" in question
    ):
        
        average_level = df["PlayerLevel"].mean()

        return f"Average Player Level is {average_level:.2f}."

    elif (
        "purchase rate" in question
        or "percentage of players who purchased" in question
        or "purchase percentage" in question
    ):
        
        purchase_rate = (
            df["InGamePurchases"].mean() * 100
        )
        return f"Purchase Rate is {purchase_rate:.2f}%"

    else:
        return "Sorry, I don't Know the answer to that question yet."