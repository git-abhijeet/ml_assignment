import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
import warnings
warnings.filterwarnings('ignore')

# Load the dataset
df = pd.read_csv('swiggy.csv')

print("="*60)
print("SWIGGY RESTAURANT DATASET ANALYSIS")
print("="*60)

print(f"\nDataset shape: {df.shape}")
print(f"Columns: {list(df.columns)}")

# Display first few rows to understand data
print("\nFirst 5 rows:")
print(df.head())

print("\nData types:")
print(df.dtypes)

print("\nBasic statistics:")
print(df.describe())

print("\nMissing values:")
print(df.isnull().sum())

# EASY QUESTIONS
print("\n" + "="*60)
print("EASY QUESTIONS")
print("="*60)

print("\n1. COUNT RESTAURANTS:")
restaurant_count = len(df)
print(f"Total restaurants in dataset: {restaurant_count}")

print("\n2. MAXIMUM PRICE:")
max_price = df['Price'].max()
print(f"Highest price: ₹{max_price}")

print("\n3. AVERAGE RATINGS:")
avg_rating = df['Avg ratings'].mean()
print(f"Average rating across all restaurants: {avg_rating:.2f}")

print("\n4. TOTAL RATINGS:")
total_ratings = df['Total ratings'].sum()
print(f"Total ratings across all restaurants: {total_ratings:,}")

print("\n5. FOOD TYPE COUNT:")
# Split food types and count unique ones
all_food_types = []
for food_types in df['Food type'].dropna():
    types = [ft.strip() for ft in str(food_types).split(',')]
    all_food_types.extend(types)
unique_food_types = len(set(all_food_types))
print(f"Number of different food types: {unique_food_types}")

# MEDIUM QUESTIONS
print("\n" + "="*60)
print("MEDIUM QUESTIONS")
print("="*60)

print("\n1. CITY ANALYSIS:")
city_counts = df['City'].value_counts()
print("Top 3 cities by restaurant count:")
for i, (city, count) in enumerate(city_counts.head(3).items(), 1):
    print(f"{i}. {city}: {count} restaurants")

print("\n2. PRICE COMPARISON BY FOOD TYPE:")
# Calculate average price for each unique food type
food_type_prices = {}
for idx, row in df.iterrows():
    if pd.notna(row['Food type']) and pd.notna(row['Price']):
        types = [ft.strip() for ft in str(row['Food type']).split(',')]
        for food_type in types:
            if food_type not in food_type_prices:
                food_type_prices[food_type] = []
            food_type_prices[food_type].append(row['Price'])

avg_prices_by_type = {ft: np.mean(prices) for ft, prices in food_type_prices.items()}
sorted_food_prices = sorted(avg_prices_by_type.items(), key=lambda x: x[1], reverse=True)

print("Top 10 food types by average price:")
for i, (food_type, avg_price) in enumerate(sorted_food_prices[:10], 1):
    print(f"{i}. {food_type}: ₹{avg_price:.2f}")

print("\n3. DELIVERY TIME ANALYSIS:")
high_rated_df = df[df['Avg ratings'] > 4]
avg_delivery_time = high_rated_df['Delivery time'].mean()
print(f"Average delivery time for restaurants with rating > 4: {avg_delivery_time:.2f} minutes")

print("\n4. TOP RATED RESTAURANTS:")
top_rated = df.nlargest(5, 'Avg ratings')[['Restaurant', 'Avg ratings', 'Food type', 'City']]
print("Top 5 restaurants by average rating:")
for i, (idx, row) in enumerate(top_rated.iterrows(), 1):
    print(f"{i}. {row['Restaurant']} ({row['City']}) - Rating: {row['Avg ratings']}, Food: {row['Food type']}")

# HARD QUESTIONS
print("\n" + "="*60)
print("HARD QUESTIONS")
print("="*60)

print("\n1. CORRELATION ANALYSIS:")
# Remove any missing values for correlation
clean_df = df.dropna(subset=['Price', 'Avg ratings'])
correlation_coeff, p_value = pearsonr(clean_df['Price'], clean_df['Avg ratings'])
print(f"Correlation coefficient between Price and Average Ratings: {correlation_coeff:.4f}")
print(f"P-value: {p_value:.4f}")

if abs(correlation_coeff) < 0.3:
    strength = "weak"
elif abs(correlation_coeff) < 0.7:
    strength = "moderate"
else:
    strength = "strong"

direction = "positive" if correlation_coeff > 0 else "negative"
print(f"Interpretation: {strength} {direction} correlation")

print("\n2. DELIVERY TIME OUTLIERS:")
Q1 = df['Delivery time'].quantile(0.25)
Q3 = df['Delivery time'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['Delivery time'] < lower_bound) | (df['Delivery time'] > upper_bound)]
print(f"Delivery time outliers detected: {len(outliers)}")
print(f"Outlier range: Below {lower_bound:.1f} or Above {upper_bound:.1f} minutes")
print(f"Min delivery time: {df['Delivery time'].min()} minutes")
print(f"Max delivery time: {df['Delivery time'].max()} minutes")

print("\n3. RATING CATEGORIES ANALYSIS:")
df['Rating_Category'] = pd.cut(df['Avg ratings'], 
                               bins=[0, 3, 4, 5], 
                               labels=['Below 3', '3-4', 'Above 4'],
                               include_lowest=True)

price_by_rating = df.groupby('Rating_Category')['Price'].agg(['mean', 'median', 'std']).round(2)
print("Price statistics by rating category:")
print(price_by_rating)

print("\n4. GROUPED ANALYSIS BY CITY:")
city_analysis = df.groupby('City').agg({
    'Price': 'mean',
    'Avg ratings': 'mean',
    'Restaurant': 'count'
}).round(2)
city_analysis.columns = ['Avg_Price', 'Avg_Rating', 'Restaurant_Count']
city_analysis = city_analysis.sort_values('Restaurant_Count', ascending=False)

print("City-wise analysis (top 10 cities):")
print(city_analysis.head(10))

print("\nAnalysis complete!")
