import pymongo
import pandas as pd

# MongoDB connection details
mongo_uri = "mongodb://zk_admin:Zkteco*123@10.6.1.179:27019/?authMechanism=DEFAULT&authSource=ralvie_db"
client = pymongo.MongoClient(mongo_uri)

# Access the database and collection
db = client['ralvie_db']  
collection = db['your_collection']

# Fetch the data from the MongoDB collection
data = pd.DataFrame(list(collection.find()))  # Fetches the collection and converts it to a pandas DataFrame

# Check if data was retrieved
if data.empty:
    print("No data was ingested. Collection is empty.")
else:
    print("Ingested Data:\n", data.head())  # Shows the first 5 rows of the ingested data

# Save the data to a CSV file
data.to_csv('ingested_data.csv', index=False)
print("Data has been ingested and saved to 'ingested_data.csv'")
