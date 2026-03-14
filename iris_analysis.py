import pandas as pd

# Load the dataset you committed earlier
df = pd.read_csv('Iris.csv')

# Show the first 5 rows
print("--- Iris Dataset Head ---")
print(df.head())

# Show basic stats
print("\n--- Basic Statistics ---")
print(df.describe())