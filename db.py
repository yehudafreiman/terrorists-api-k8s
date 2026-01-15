import pandas as pd
from pymongo import MongoClient
from models import Terrorist
from pandantic import Pandantic

def terrorist_data_processing(csv):
    # Load CSV file into a DataFrame
    df = pd.read_csv(csv)
    # Sort by danger rate
    sorted_df = df.sort_values(by='danger_rate',ascending=False)
    # Return top 5 danger rate
    top_5_danger_rate = sorted_df.head(5)
    # Filter out invalid rows
    validator = Pandantic(schema=Terrorist)
    df_invalid = top_5_danger_rate
    df_valid = validator.validate(dataframe=df_invalid, errors="skip")
    # selected columns
    df_selected_columns = df_valid[['name', 'location', 'danger_rate']]
    # Converse to JSON format
    result = df_selected_columns.to_json(orient='records')
    return result

# Insert to MongoDB
# Read from environment variables
MONGO_HOST = "mongo-0.mongo"
MONGO_PORT = "27017"
MONGO_USERNAME = "admin"
MONGO_PASSWORD = "secretpass"
MONGO_DB = "threat_db"
MONGO_AUTH_SOURCE = "admin"

# Create connection
client = MongoClient(f"mongodb://{MONGO_HOST}:{MONGO_PORT}/")
db = client[MONGO_DB]
collection = db.contacts

