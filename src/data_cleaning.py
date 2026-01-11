import pandas as pd
import os

# Build absolute path safely
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "retail_sales.csv")

# Load data
df = pd.read_csv(DATA_PATH)

# Convert date column
df["Transaction Date"] = pd.to_datetime(df["Transaction Date"], errors="coerce")

# Handle missing values
df["Item"].fillna("Unknown Item", inplace=True)
df["Discount Applied"].fillna(False, inplace=True)

# Drop rows with critical missing values
df.dropna(subset=["Price Per Unit", "Quantity", "Total Spent"], inplace=True)

print("✅ Data cleaned successfully")
print(df.head())
df.info()
