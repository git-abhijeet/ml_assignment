# Swiggy Restaurant Dataset Analysis

## Easy Questions

### 1. Count Restaurants

8,680 restaurants in the dataset.

### 2. Maximum Price

₹2,500 is the highest restaurant price.

### 3. Average Ratings

3.66 is the average rating across all restaurants.

### 4. Total Ratings

1,359,590 total ratings across all restaurants.

### 5. Food Type Count

600 different food types present in the dataset.

## Medium Questions

### 1. City Analysis

Top 3 cities by restaurant count:

1. Kolkata: 1,346 restaurants
2. Mumbai: 1,277 restaurants
3. Chennai: 1,106 restaurants

### 2. Price Comparison by Food Type

Top food types by average price:

-   Chinese Pan-Asian Tibetan Oriental Mongolian: ₹1,800
-   Indonesian: ₹1,240
-   Korean: ₹1,200
-   Japanese: ₹1,162
-   Asian European Italian: ₹1,100

### 3. Visualization

Bar chart shows Chinese fusion cuisines command highest average prices, followed by international cuisines like Indonesian and Korean.

### 4. Rating Distribution

Histogram shows most restaurants cluster around 3.0-4.2 rating range with normal distribution pattern.

### 5. Delivery Time Analysis

51.99 minutes average delivery time for restaurants with rating above 4.

### 6. Top Rated Restaurants

Top 5 restaurants (all rated 5.0):

1. Diamond Market Pizza Jp (Mumbai) - Italian
2. Get In My Belly (Mumbai) - Indian
3. The Asian Pavilion (Mumbai) - Asian Chinese
4. Cafe Kokomo (Mumbai) - Beverages/Snacks/Desserts/Bakery
5. Papacream (Pune) - Ice Cream

## Hard Questions

### 1. Correlation Analysis

Correlation coefficient: 0.1136 (weak positive correlation)
P-value: 0.0000 (statistically significant)
Higher-priced restaurants tend to have slightly higher ratings, but relationship is weak.

### 2. Delivery Time Outliers

22 outliers detected using box plot analysis.
Outlier threshold: Below 14 minutes or Above 94 minutes.
Range: 20-109 minutes.
Outliers indicate either very efficient delivery systems or problematic logistics.

### 3. Price and Ratings Box Plot

Price distribution by rating categories:

-   Below 3: ₹326 average, ₹300 median
-   3-4: ₹319 average, ₹300 median
-   Above 4: ₹385 average, ₹300 median
    Higher-rated restaurants show greater price variability.

### 4. Grouped Analysis by City

Top 10 cities analysis:

-   Kolkata: ₹362 avg price, 3.70 avg rating, 1,346 restaurants
-   Mumbai: ₹394 avg price, 3.60 avg rating, 1,277 restaurants
-   Chennai: ₹356 avg price, 3.78 avg rating, 1,106 restaurants
-   Pune: ₹354 avg price, 3.55 avg rating, 1,090 restaurants
-   Hyderabad: ₹300 avg price, 3.70 avg rating, 1,075 restaurants

Mumbai has highest average prices while Chennai has highest average ratings among major cities.

## Key Insights

-   Dataset covers 8,680 restaurants across 9 major Indian cities
-   Kolkata dominates with most restaurants (1,346)
-   International cuisines command premium pricing
-   Most restaurants rated between 3.0-4.2
-   Weak positive correlation between price and ratings
-   22 delivery time outliers suggest operational inefficiencies
-   Mumbai restaurants most expensive, Chennai highest rated
