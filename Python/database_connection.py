import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

print("Connecting to MySQL....")

connection = mysql.connector.connect(
    host=os.getenv("DB_HOST", "localhost"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME", "gaming_analytics_db")
)

print("Connected Successfully!")

cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM player_statistics")

result = cursor.fetchone()

print('Total Players', result[0])

cursor.close()
connection.close()
print("Connection Close!")