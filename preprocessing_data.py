import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the ingested data
data = pd.read_csv('ingested_data.csv')

# Example preprocessing steps

# Step 1: Handle missing values by dropping rows with NaN values
data_cleaned = data.dropna()  # Removes rows with missing values

# Step 2: Feature scaling (if necessary)
# Assuming numerical features, scale the features using StandardScaler
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_cleaned)  # Scales the cleaned data

# Step 3: Split the data into training and testing sets (80/20 split)
X_train, X_test = train_test_split(data_scaled, test_size=0.2, random_state=42)

# Step 4: Save the preprocessed data
pd.DataFrame(X_train).to_csv('train_data.csv', index=False)
pd.DataFrame(X_test).to_csv('test_data.csv', index=False)

print("Data preprocessing completed. Train and test data saved as 'train_data.csv' and 'test_data.csv'")
