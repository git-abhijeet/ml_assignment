# K-Means Clustering Assignments

This folder contains both **Easy** and **Intermediate** level K-Means clustering assignments using the Mall Customers dataset.

## Dataset

-   **File**: `Mall_Customers.csv`
-   **Size**: 200 customers
-   **Features**: CustomerID, Gender, Age, Annual Income (k$), Spending Score (1-100)

---

## 🟢 Easy Level Assignment

### Objective

Understand and apply basic K-Means clustering using key features.

### Tasks Completed

-   ✅ Data loading and exploration
-   ✅ EDA with histograms and box plots
-   ✅ Feature selection (2 features)
-   ✅ K-Means with k=3
-   ✅ Basic visualization and interpretation

### Files

-   `kmeans_clustering.py` - Python script
-   `kmeans_clustering.ipynb` - Jupyter notebook

### How to Run

```bash
python kmeans_clustering.py
```

---

## 🟡 Intermediate Level Assignment

### Objective

Explore optimal clustering using the Elbow method and comprehensive analysis.

### Tasks Completed

-   ✅ **Preprocessing**: Normalize/scale numerical data and encode categorical variables
-   ✅ **Optimal k Determination**: Use Elbow Method with WCSS and Silhouette Score
-   ✅ **Cluster Profiling**: Comprehensive analysis of Age, Income, Spending Score per cluster
-   ✅ **Distance Metrics**: Compare performance with different initialization methods
-   ✅ **Business Insights**: Detailed customer segment analysis

### Advanced Features

-   Feature scaling with StandardScaler
-   Gender encoding with LabelEncoder
-   Elbow curve visualization
-   Silhouette score analysis
-   Multiple clustering configurations comparison
-   Comprehensive cluster profiling
-   Business recommendations

### Files

-   `kmeans_intermediate.py` - Python script
-   `kmeans_intermediate.ipynb` - Jupyter notebook (recommended)

### How to Run

```bash
# Python script
python kmeans_intermediate.py

# Or open the Jupyter notebook
jupyter notebook kmeans_intermediate.ipynb
```

---

## 📊 Results Summary

### Easy Level Results

-   3 clusters identified
-   Basic customer segmentation
-   Simple visualization

### Intermediate Level Results

-   **5 optimal clusters** determined via Elbow Method
-   **Customer Segments Identified**:
    1. 💡 **Budget-Conscious Shoppers** - Lower income, conservative spending
    2. 🎯 **Young Spenders** - Lower income but high spending
    3. 💼 **Conservative High Earners** - High income but low spending
    4. 💎 **Premium Customers** - High income and high spending
    5. ⚖️ **Moderate Shoppers** - Balanced income and spending

### Business Value

-   Targeted marketing strategies
-   Customer relationship management insights
-   Product positioning recommendations
-   Revenue optimization opportunities

---

## 🛠️ Requirements

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

## 📁 Files Structure

```
clustering/
├── Mall_Customers.csv           # Dataset
├── README.md                    # This file
├── kmeans_clustering.py         # Easy level script
├── kmeans_clustering.ipynb      # Easy level notebook
├── kmeans_intermediate.py       # Intermediate level script
└── kmeans_intermediate.ipynb    # Intermediate level notebook (recommended)
```

---

## 🎯 Assignment Levels

| Level               | Complexity | Features                               | Audience              |
| ------------------- | ---------- | -------------------------------------- | --------------------- |
| 🟢 **Easy**         | Basic      | Simple K-Means, fixed k=3              | Beginners             |
| 🟡 **Intermediate** | Advanced   | Elbow method, preprocessing, profiling | Intermediate learners |

Both assignments provide clear, educational implementations without unnecessary complexity while covering all required concepts thoroughly! 📊✨
