# K-Means Clustering - Intermediate Level
# Mall Customers Dataset Analysis with Elbow Method and Comprehensive Profiling

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import silhouette_score

# Set style for better visualizations
plt.style.use('default')
sns.set_palette("husl")

print("=== K-Means Clustering - Intermediate Level ===")
print("Dataset: Mall Customers")
print("Objective: Explore optimal clustering using Elbow method\n")

# 1. Load and Explore Dataset
print("1. Loading and Exploring Dataset")
print("-" * 35)

df = pd.read_csv('Mall_Customers.csv')
print(f"Dataset shape: {df.shape}")
print(f"Missing values: {df.isnull().sum().sum()}")
print(f"Gender distribution:\n{df['Gender'].value_counts()}")

# 2. Data Preprocessing
print("\n2. Data Preprocessing")
print("-" * 25)

# Create a copy for processing
df_processed = df.copy()

# Encode categorical variables
label_encoder = LabelEncoder()
df_processed['Gender_Encoded'] = label_encoder.fit_transform(df_processed['Gender'])
print(f"✅ Gender encoded: Female={label_encoder.transform(['Female'])[0]}, Male={label_encoder.transform(['Male'])[0]}")

# Select and scale features
features = ['Gender_Encoded', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)']
X = df_processed[features].copy()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns=features)
print(f"✅ Features scaled: {features}")

# 3. Elbow Method for Optimal k
print("\n3. Determining Optimal k using Elbow Method")
print("-" * 45)

k_range = range(1, 11)
wcss = []
silhouette_scores = []

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)
    
    if k > 1:
        silhouette_avg = silhouette_score(X_scaled, kmeans.labels_)
        silhouette_scores.append(silhouette_avg)
        print(f"k={k}: WCSS={kmeans.inertia_:.2f}, Silhouette={silhouette_avg:.3f}")
    else:
        silhouette_scores.append(np.nan)
        print(f"k={k}: WCSS={kmeans.inertia_:.2f}")

# Plot Elbow Curve
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

ax1.plot(k_range, wcss, 'bo-', linewidth=2, markersize=8)
ax1.set_xlabel('Number of Clusters (k)')
ax1.set_ylabel('WCSS')
ax1.set_title('Elbow Method for Optimal k')
ax1.grid(True, alpha=0.3)

valid_k = list(range(2, 11))
valid_silhouette = silhouette_scores[1:]
ax2.plot(valid_k, valid_silhouette, 'ro-', linewidth=2, markersize=8)
ax2.set_xlabel('Number of Clusters (k)')
ax2.set_ylabel('Silhouette Score')
ax2.set_title('Silhouette Score vs k')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Choose optimal k
optimal_k = valid_k[np.argmax(valid_silhouette)]
print(f"🎯 Optimal k based on silhouette score: {optimal_k}")
optimal_k = 5  # You can adjust this based on elbow visualization

# 4. Apply Final K-Means Clustering
print(f"\n4. Applying K-Means with k={optimal_k}")
print("-" * 35)

final_kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
cluster_labels = final_kmeans.fit_predict(X_scaled)
df_processed['Cluster'] = cluster_labels

final_silhouette = silhouette_score(X_scaled, cluster_labels)
print(f"✅ Clustering completed!")
print(f"Silhouette Score: {final_silhouette:.3f}")
print(f"WCSS: {final_kmeans.inertia_:.2f}")

# Cluster distribution
cluster_counts = pd.Series(cluster_labels).value_counts().sort_index()
print(f"\nCluster Distribution:")
for i in range(optimal_k):
    count = cluster_counts[i]
    percentage = (count / len(df_processed)) * 100
    print(f"Cluster {i}: {count} customers ({percentage:.1f}%)")

# 5. Cluster Profiling and Analysis
print(f"\n5. Cluster Profiling and Analysis")
print("-" * 35)

print("Detailed Cluster Insights:")
for cluster_id in range(optimal_k):
    cluster_data = df_processed[df_processed['Cluster'] == cluster_id]
    
    avg_age = cluster_data['Age'].mean()
    avg_income = cluster_data['Annual Income (k$)'].mean()
    avg_spending = cluster_data['Spending Score (1-100)'].mean()
    female_pct = (cluster_data['Gender'] == 'Female').sum() / len(cluster_data) * 100
    
    print(f"\n🏷️  Cluster {cluster_id} ({len(cluster_data)} customers):")
    print(f"   👤 Average Age: {avg_age:.1f} years")
    print(f"   💰 Average Income: ${avg_income:.1f}k")
    print(f"   🛒 Average Spending Score: {avg_spending:.1f}")
    print(f"   👩 Female Percentage: {female_pct:.1f}%")
    
    # Segment interpretation
    if avg_income < 40 and avg_spending < 40:
        segment = "💡 Budget-Conscious Shoppers"
    elif avg_income < 40 and avg_spending > 60:
        segment = "🎯 Young Spenders"
    elif avg_income > 70 and avg_spending < 40:
        segment = "💼 Conservative High Earners"
    elif avg_income > 70 and avg_spending > 60:
        segment = "💎 Premium Customers"
    else:
        segment = "⚖️ Moderate Shoppers"
    
    print(f"   🎯 Segment: {segment}")

# 6. Visualizations
print(f"\n6. Creating Cluster Visualizations")
print("-" * 35)

# Main scatter plot
plt.figure(figsize=(12, 8))
colors = ['red', 'blue', 'green', 'purple', 'orange']

for i in range(optimal_k):
    cluster_data = df_processed[df_processed['Cluster'] == i]
    plt.scatter(cluster_data['Annual Income (k$)'], 
               cluster_data['Spending Score (1-100)'], 
               c=colors[i], 
               label=f'Cluster {i}', 
               alpha=0.6, 
               s=60)

# Add centroids
centers_original = scaler.inverse_transform(final_kmeans.cluster_centers_)
centers_df = pd.DataFrame(centers_original, columns=features)

plt.scatter(centers_df['Annual Income (k$)'], 
           centers_df['Spending Score (1-100)'], 
           c='black', marker='x', s=200, linewidths=3, label='Centroids')

plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.title(f'K-Means Clustering Results (k={optimal_k})\nMall Customer Segmentation')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# Summary statistics
summary_stats = df_processed.groupby('Cluster').agg({
    'Age': 'mean',
    'Annual Income (k$)': 'mean', 
    'Spending Score (1-100)': 'mean'
}).round(1)

summary_stats['Size'] = df_processed['Cluster'].value_counts().sort_index()
summary_stats['Female_Pct'] = df_processed.groupby('Cluster')['Gender'].apply(lambda x: (x == 'Female').sum() / len(x) * 100).round(1)

print(f"\n📊 Summary Statistics by Cluster:")
print(summary_stats)

# 7. Distance Metrics Comparison (Optional)
print(f"\n7. Comparing Different K-Means Configurations")
print("-" * 45)

configs = [
    {'init': 'k-means++', 'n_init': 10},
    {'init': 'random', 'n_init': 10},
    {'init': 'k-means++', 'n_init': 20}
]

config_names = [
    'K-means++ (default)',
    'Random initialization', 
    'K-means++ (more runs)'
]

for config, name in zip(configs, config_names):
    kmeans = KMeans(n_clusters=optimal_k, random_state=42, **config)
    labels = kmeans.fit_predict(X_scaled)
    
    wcss = kmeans.inertia_
    silhouette_avg = silhouette_score(X_scaled, labels)
    
    print(f"{name}:")
    print(f"  WCSS: {wcss:.2f}")
    print(f"  Silhouette Score: {silhouette_avg:.3f}")

print(f"\n" + "="*60)
print("✅ K-Means Intermediate Assignment Completed!")
print(f"📊 Results Summary:")
print(f"- Dataset: {len(df)} mall customers")
print(f"- Optimal clusters: {optimal_k}")
print(f"- Features used: {features}")
print(f"- Final silhouette score: {final_silhouette:.3f}")
print(f"- Customer segments identified and profiled")
print(f"- Comprehensive analysis with business insights")
print("="*60)
