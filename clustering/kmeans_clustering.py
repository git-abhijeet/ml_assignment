# K-Means Clustering Assignment - Mall Customers Dataset
# Easy Level Implementation

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Set style for better plots
plt.style.use('default')
sns.set_palette("husl")

print("=== K-Means Clustering Assignment ===")
print("Dataset: Mall Customers")
print("Objective: Basic K-Means clustering with 2 features\n")

# Task 1: Load the Dataset
print("Task 1: Loading the Dataset")
print("-" * 30)

# Load the dataset
df = pd.read_csv('Mall_Customers.csv')

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head())
print(f"\nDataset shape: {df.shape}")
print(f"Columns: {list(df.columns)}")

# Check for missing values
print(f"\nMissing values:")
print(df.isnull().sum())

if df.isnull().sum().sum() == 0:
    print("✓ No missing values found!")
else:
    print("⚠ Missing values detected - handling required")

print("\n" + "="*50 + "\n")

# Task 2: Perform EDA (Exploratory Data Analysis)
print("Task 2: Exploratory Data Analysis")
print("-" * 35)

# Basic statistics
print("Dataset Info:")
print(df.info())
print("\nBasic Statistics:")
print(df.describe())

# Create visualizations
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Exploratory Data Analysis - Mall Customers', fontsize=16)

# Histogram for Age
axes[0, 0].hist(df['Age'], bins=20, alpha=0.7, color='skyblue', edgecolor='black')
axes[0, 0].set_title('Distribution of Age')
axes[0, 0].set_xlabel('Age')
axes[0, 0].set_ylabel('Frequency')

# Histogram for Annual Income
axes[0, 1].hist(df['Annual Income (k$)'], bins=20, alpha=0.7, color='lightgreen', edgecolor='black')
axes[0, 1].set_title('Distribution of Annual Income')
axes[0, 1].set_xlabel('Annual Income (k$)')
axes[0, 1].set_ylabel('Frequency')

# Box plot for Age
axes[1, 0].boxplot(df['Age'])
axes[1, 0].set_title('Box Plot - Age')
axes[1, 0].set_ylabel('Age')

# Box plot for Annual Income
axes[1, 1].boxplot(df['Annual Income (k$)'])
axes[1, 1].set_title('Box Plot - Annual Income')
axes[1, 1].set_ylabel('Annual Income (k$)')

plt.tight_layout()
plt.show()

# Additional EDA - Gender distribution
print(f"\nGender Distribution:")
print(df['Gender'].value_counts())

# Correlation analysis
numeric_columns = df.select_dtypes(include=[np.number]).columns
correlation_matrix = df[numeric_columns].corr()
print(f"\nCorrelation Matrix:")
print(correlation_matrix)

print("\n" + "="*50 + "\n")

# Task 3: Feature Selection
print("Task 3: Feature Selection")
print("-" * 25)

# Select 2 features for clustering: Annual Income and Spending Score
features = ['Annual Income (k$)', 'Spending Score (1-100)']
X = df[features].copy()

print(f"Selected features for clustering: {features}")
print(f"Feature matrix shape: {X.shape}")
print(f"\nFirst 5 rows of selected features:")
print(X.head())

# Visualize the selected features
plt.figure(figsize=(10, 6))
plt.scatter(X['Annual Income (k$)'], X['Spending Score (1-100)'], alpha=0.6, s=50)
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.title('Scatter Plot: Annual Income vs Spending Score (Before Clustering)')
plt.grid(True, alpha=0.3)
plt.show()

print("\n" + "="*50 + "\n")

# Task 4: Implement K-Means Clustering
print("Task 4: K-Means Clustering Implementation")
print("-" * 40)

# Apply K-Means with k=3
k = 3
print(f"Applying K-Means clustering with k = {k}")

# Initialize and fit K-Means
kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X)

# Add cluster labels to the original dataframe
df['Cluster'] = clusters

print(f"✓ K-Means clustering completed!")
print(f"Cluster centers:")
print(kmeans.cluster_centers_)

# Display cluster statistics
print(f"\nCluster Distribution:")
cluster_counts = pd.Series(clusters).value_counts().sort_index()
for i in range(k):
    count = cluster_counts[i]
    percentage = (count / len(df)) * 100
    print(f"Cluster {i}: {count} customers ({percentage:.1f}%)")

# Calculate cluster statistics
print(f"\nCluster Statistics:")
cluster_stats = df.groupby('Cluster')[features].mean()
print(cluster_stats)

print("\n" + "="*50 + "\n")

# Task 5: Visualize Clusters
print("Task 5: Cluster Visualization")
print("-" * 30)

# Create a 2D scatter plot with clusters
plt.figure(figsize=(12, 8))

# Define colors for clusters
colors = ['red', 'blue', 'green', 'purple', 'orange']

# Plot each cluster with different colors
for i in range(k):
    cluster_data = X[clusters == i]
    plt.scatter(cluster_data['Annual Income (k$)'], 
               cluster_data['Spending Score (1-100)'], 
               c=colors[i], 
               label=f'Cluster {i}', 
               alpha=0.6, 
               s=50)

# Plot cluster centers
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], 
           c='black', marker='x', s=200, linewidths=3, 
           label='Centroids')

plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.title('K-Means Clustering Results (k=3)\nMall Customers Segmentation')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# Additional analysis - cluster interpretation
print("Cluster Interpretation:")
print("-" * 20)

for i in range(k):
    cluster_data = df[df['Cluster'] == i]
    avg_income = cluster_data['Annual Income (k$)'].mean()
    avg_spending = cluster_data['Spending Score (1-100)'].mean()
    avg_age = cluster_data['Age'].mean()
    
    print(f"\nCluster {i} ({len(cluster_data)} customers):")
    print(f"  - Average Income: ${avg_income:.1f}k")
    print(f"  - Average Spending Score: {avg_spending:.1f}")
    print(f"  - Average Age: {avg_age:.1f} years")
    
    # Simple interpretation
    if avg_income < 40 and avg_spending < 40:
        interpretation = "Low Income, Low Spending"
    elif avg_income < 40 and avg_spending > 60:
        interpretation = "Low Income, High Spending"
    elif avg_income > 60 and avg_spending < 40:
        interpretation = "High Income, Low Spending"
    elif avg_income > 60 and avg_spending > 60:
        interpretation = "High Income, High Spending"
    else:
        interpretation = "Moderate Income, Moderate Spending"
    
    print(f"  - Profile: {interpretation}")

print(f"\n" + "="*50)
print("✓ K-Means Clustering Assignment Completed!")
print("Summary:")
print(f"- Dataset: {len(df)} mall customers")
print(f"- Features used: {features}")
print(f"- Number of clusters: {k}")
print(f"- No missing values detected")
print("- Clusters successfully visualized and interpreted")
print("="*50)
