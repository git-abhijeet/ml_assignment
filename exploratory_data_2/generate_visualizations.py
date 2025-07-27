import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Load the dataset
df = pd.read_csv('swiggy.csv')

# Set style for better visualizations
plt.style.use('default')
plt.rcParams['figure.figsize'] = (12, 8)

# 1. Average price by food type (Top 15)
print("Generating visualizations...")

# Extract and calculate average prices for major food types
food_type_prices = {}
for idx, row in df.iterrows():
    if pd.notna(row['Food type']) and pd.notna(row['Price']):
        types = [ft.strip() for ft in str(row['Food type']).split(',')]
        for food_type in types:
            if food_type not in food_type_prices:
                food_type_prices[food_type] = []
            food_type_prices[food_type].append(row['Price'])

# Filter food types with at least 10 restaurants
major_food_types = {ft: prices for ft, prices in food_type_prices.items() if len(prices) >= 10}
avg_prices_by_type = {ft: np.mean(prices) for ft, prices in major_food_types.items()}
sorted_food_prices = sorted(avg_prices_by_type.items(), key=lambda x: x[1], reverse=True)

# Plot 1: Average price by food type
plt.figure(figsize=(14, 8))
top_15_food = dict(sorted_food_prices[:15])
plt.bar(range(len(top_15_food)), list(top_15_food.values()))
plt.title('Average Price by Food Type (Top 15)', fontsize=16, fontweight='bold')
plt.xlabel('Food Type', fontsize=12)
plt.ylabel('Average Price (₹)', fontsize=12)
plt.xticks(range(len(top_15_food)), list(top_15_food.keys()), rotation=45, ha='right')
plt.tight_layout()
plt.savefig('avg_price_by_food_type.png', dpi=300, bbox_inches='tight')
plt.close()

# Plot 2: Rating distribution histogram
plt.figure(figsize=(12, 8))
plt.hist(df['Avg ratings'], bins=30, edgecolor='black', alpha=0.7)
plt.title('Distribution of Restaurant Ratings', fontsize=16, fontweight='bold')
plt.xlabel('Average Rating', fontsize=12)
plt.ylabel('Number of Restaurants', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('rating_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# Plot 3: Price vs Rating scatter plot
plt.figure(figsize=(12, 8))
plt.scatter(df['Price'], df['Avg ratings'], alpha=0.6)
plt.title('Correlation: Restaurant Price vs Average Rating', fontsize=16, fontweight='bold')
plt.xlabel('Price (₹)', fontsize=12)
plt.ylabel('Average Rating', fontsize=12)
plt.grid(True, alpha=0.3)
# Add correlation coefficient to plot
from scipy.stats import pearsonr
clean_df = df.dropna(subset=['Price', 'Avg ratings'])
corr_coeff, _ = pearsonr(clean_df['Price'], clean_df['Avg ratings'])
plt.text(0.02, 0.98, f'Correlation: {corr_coeff:.4f}', transform=plt.gca().transAxes, 
         fontsize=12, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
plt.tight_layout()
plt.savefig('price_rating_correlation.png', dpi=300, bbox_inches='tight')
plt.close()

# Plot 4: Delivery time box plot
plt.figure(figsize=(12, 8))
plt.boxplot(df['Delivery time'], vert=True)
plt.title('Box Plot: Delivery Time Distribution (Outlier Detection)', fontsize=16, fontweight='bold')
plt.ylabel('Delivery Time (minutes)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('delivery_time_boxplot.png', dpi=300, bbox_inches='tight')
plt.close()

# Plot 5: Price distribution by rating categories
df['Rating_Category'] = pd.cut(df['Avg ratings'], 
                               bins=[0, 3, 4, 5], 
                               labels=['Below 3', '3-4', 'Above 4'],
                               include_lowest=True)

plt.figure(figsize=(12, 8))
df.boxplot(column='Price', by='Rating_Category', ax=plt.gca())
plt.title('Price Distribution by Rating Categories', fontsize=16, fontweight='bold')
plt.xlabel('Rating Category', fontsize=12)
plt.ylabel('Price (₹)', fontsize=12)
plt.suptitle('')  # Remove automatic title
plt.tight_layout()
plt.savefig('price_by_rating_categories.png', dpi=300, bbox_inches='tight')
plt.close()

# Plot 6: Grouped analysis by city
city_analysis = df.groupby('City').agg({
    'Price': 'mean',
    'Avg ratings': 'mean',
    'Restaurant': 'count'
}).round(2)
city_analysis.columns = ['Avg_Price', 'Avg_Rating', 'Restaurant_Count']
top_cities = city_analysis.nlargest(10, 'Restaurant_Count')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Average price by city
ax1.bar(range(len(top_cities)), top_cities['Avg_Price'])
ax1.set_title('Average Price by City (Top 10)', fontsize=14, fontweight='bold')
ax1.set_xlabel('City', fontsize=12)
ax1.set_ylabel('Average Price (₹)', fontsize=12)
ax1.set_xticks(range(len(top_cities)))
ax1.set_xticklabels(top_cities.index, rotation=45, ha='right')

# Average rating by city
ax2.bar(range(len(top_cities)), top_cities['Avg_Rating'])
ax2.set_title('Average Rating by City (Top 10)', fontsize=14, fontweight='bold')
ax2.set_xlabel('City', fontsize=12)
ax2.set_ylabel('Average Rating', fontsize=12)
ax2.set_xticks(range(len(top_cities)))
ax2.set_xticklabels(top_cities.index, rotation=45, ha='right')

plt.tight_layout()
plt.savefig('city_analysis_grouped.png', dpi=300, bbox_inches='tight')
plt.close()

print("All visualizations generated successfully!")
