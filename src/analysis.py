import pandas as pd
import os

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "retail_sales.csv")

# Load data
df = pd.read_csv(DATA_PATH)

# Basic cleaning
df.dropna(subset=["Total Spent"], inplace=True)

print("✅ Data loaded and cleaned successfully")

# --------------------------------------------------
# Total Revenue
# --------------------------------------------------
total_revenue = df["Total Spent"].sum()
print("\n💰 Total Revenue:", round(total_revenue, 2))

# --------------------------------------------------
# Revenue by Category
# --------------------------------------------------
category_revenue = (
    df.groupby("Category")["Total Spent"]
    .sum()
    .sort_values(ascending=False)
)

print("\n📊 Revenue by Category:")
print(category_revenue)

# --------------------------------------------------
# Top 5 Items by Revenue
# --------------------------------------------------
top_items = (
    df.groupby("Item")["Total Spent"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("\n🏆 Top 5 Items:")
print(top_items)

# --------------------------------------------------
# Average Spend per Transaction
# --------------------------------------------------
avg_spend = df["Total Spent"].mean()
print("\n🧾 Average Spend per Transaction:", round(avg_spend, 2))

# --------------------------------------------------
# Revenue by Payment Method
# --------------------------------------------------
payment_analysis = (
    df.groupby("Payment Method")["Total Spent"]
    .sum()
    .sort_values(ascending=False)
)

print("\n💳 Revenue by Payment Method:")
print(payment_analysis)

print("\n✅ Analysis completed successfully")
