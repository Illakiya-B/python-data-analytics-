import pandas as pd

# Configuration

DATA_FILE = "data/processed_airline.csv"

# Load Dataset

df = pd.read_csv(DATA_FILE)

print("=" * 60)
print("BRITISH AIRWAYS CUSTOMER EXPERIENCE ANALYTICS")
print("=" * 60)

print("\nDataset loaded successfully!\n")

print("Shape")
print(df.shape)

print("\nColumns")
print(df.columns.tolist())

print("\nFirst Five Rows")
print(df.head())

print("\nData Types")
print(df.dtypes)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

print("\nSummary Statistics")
print(df.describe())
