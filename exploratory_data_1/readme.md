# Startup Funding Dataset Analysis

## Easy Questions

### 1. Missing Values Percentage

-   Sr No: 0.00%
-   Date dd/mm/yyyy: 0.00%
-   Startup Name: 0.00%
-   Industry Vertical: 5.62%
-   SubVertical: 30.75%
-   City Location: 5.91%
-   Investors Name: 0.79%
-   InvestmentType: 0.13%
-   Amount in USD: 31.54%
-   Remarks: 86.24%

### 2. Data Type Verification

Not appropriate. Dates are object type (need datetime), amounts are object type (need numeric).

### 3. Date Format Standardization

8 dates need correction from 3,044 records.

### 4. Duplicate Rows

0 duplicate rows.

### 5. Average Funding Amount

Overall average: $18,429,897.27
Top industries: Transportation ($979M), E-Commerce & M-Commerce ($680M), Ecommerce Marketplace ($500M).

### 6. Visualization

Bar chart shows Transportation has highest average funding, followed by E-Commerce sectors.

## Medium Questions

### 1. Outlier Detection (IQR Method)

283 outliers detected. Threshold: Below $-10,825,000 or Above $19,295,000.

### 2. Visualization

Box plot shows multiple extreme outliers in funding amounts.

### 3. Unique Industry Verticals

821 unique industry verticals.

### 4. Investment Type Distribution

Private Equity: 1,356 (44.5%), Seed Funding: 1,355 (44.5%), Seed/Angel: 107 (3.5%).

### 5. Visualization

Pie chart shows Private Equity and Seed Funding dominate equally.

### 6. City with Highest Funding Count

Bangalore: 700 startup fundings.

### 7. Visualization

Bar chart shows Bangalore leads, followed by Mumbai and Gurgaon.

### 8. Funding Trends Over Time

2015: $8.60B, 2016: $3.83B, 2017: $10.43B (Peak), 2018: $5.12B, 2019: $9.69B, 2020: $0.39B.

### 9. Visualization

Line chart shows peak in 2017, decline in 2018, recovery in 2019, drop in 2020.

## Hard Questions

### 1. Correlation Analysis

Strong positive correlation between industry type and investment amount. Technology and Consumer Internet sectors receive highest funding concentrations.

### 2. Visualization

Heatmap shows Consumer Internet and eCommerce dominate funding across major cities.

### 3. Top Investor Analysis

Westbridge Capital: $3.90B (1 investment), Softbank: $2.50B (1 investment), SoftBank Group: $1.46B (2 investments).

### 4. Visualization

Bar chart shows Westbridge Capital as top single investor by amount.

### 5. Funding Variability by Industry

Highest standard deviation: Transportation ($1.95B), Online Marketplace ($495M), B2B ($412M).

### 6. Visualization

Bar chart shows Transportation has highest funding variability.

### 7. Most Funded Industry

Consumer Internet: $6.25B, eCommerce: $5.00B, Transportation: $3.92B.

### 8. Visualization

Bar chart shows Consumer Internet leads total funding.

### 9. Comparative Analysis

Top combinations: Bangalore+eCommerce ($4.33B), Bengaluru+Transportation ($3.90B), Bangalore+Consumer Internet ($1.79B).

### 10. Visualization

Heatmap reveals Bangalore dominates across multiple industries, especially eCommerce and Consumer Internet.

## Summary

-   Dataset: 3,044 records, 31.54% missing funding amounts
-   Peak year: 2017 ($10.43B), Leading city: Bangalore (700 fundings)
-   Top industry: Consumer Internet ($6.25B total), Top investor: Westbridge Capital ($3.90B)
-   283 funding outliers detected, 821 unique industry verticals identified
