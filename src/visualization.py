import pandas as pd
import matplotlib.pyplot as plt
import os

# Base project directory
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Paths
DATA_PATH = os.path.join(BASE_DIR, "data", "retail_sales.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs", "charts")

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load data
df = pd.read_csv(DATA_PATH)
df.dropna(subset=["Total Spent"], inplace=True)

# Revenue by category
category_revenue = (
    df.groupby("Category")["Total Spent"]
    .sum()
    .sort_values(ascending=False)
)

# Plot
plt.figure(figsize=(10, 5))
category_revenue.plot(kind="bar")
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Total Revenue")
plt.tight_layout()

# Save chart
output_path = os.path.join(OUTPUT_DIR, "revenue_by_category.png")
plt.savefig(output_path)
plt.show()

print(f"✅ Chart saved at: {output_path}")
