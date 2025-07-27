import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Load the dataset
df = pd.read_csv('ICRISAT-District Level Data.csv')

# Set style for better visualizations
plt.style.use('default')
plt.rcParams['figure.figsize'] = (12, 8)

print("Generating visualizations...")

# 1. Bar Chart - Crop Area Distribution
plt.figure(figsize=(10, 6))
crops = ['Rice', 'Wheat', 'Maize']
areas = [
    df['RICE AREA (1000 ha)'].sum(),
    df['WHEAT AREA (1000 ha)'].sum(),
    df['MAIZE AREA (1000 ha)'].sum()
]

plt.bar(crops, areas, color=['lightblue', 'wheat', 'gold'])
plt.title('Total Area Allocated to Major Crops', fontsize=16, fontweight='bold')
plt.xlabel('Crops', fontsize=12)
plt.ylabel('Area (1000 hectares)', fontsize=12)
plt.ticklabel_format(style='scientific', axis='y', scilimits=(0,0))
for i, v in enumerate(areas):
    plt.text(i, v + max(areas)*0.01, f'{v:,.0f}', ha='center', va='bottom')
plt.tight_layout()
plt.savefig('crop_area_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# 2. Line Chart - Yearly Rice Production
plt.figure(figsize=(14, 8))
yearly_rice = df.groupby('Year')['RICE PRODUCTION (1000 tons)'].sum()
plt.plot(yearly_rice.index, yearly_rice.values, linewidth=2, marker='o', markersize=4)
peak_year = yearly_rice.idxmax()
peak_value = yearly_rice.max()
plt.scatter(peak_year, peak_value, color='red', s=100, zorder=5, label=f'Peak: {peak_year}')
plt.title('Rice Production Over Years', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Rice Production (1000 tons)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig('yearly_rice_production.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. Horizontal Bar Chart - State Wheat Production
plt.figure(figsize=(12, 10))
state_wheat = df.groupby('State Name')['WHEAT PRODUCTION (1000 tons)'].sum().sort_values()
# Remove states with zero production for better visualization
state_wheat = state_wheat[state_wheat > 0]
plt.barh(range(len(state_wheat)), state_wheat.values)
plt.title('Wheat Production by State', fontsize=16, fontweight='bold')
plt.xlabel('Wheat Production (1000 tons)', fontsize=12)
plt.ylabel('States', fontsize=12)
plt.yticks(range(len(state_wheat)), state_wheat.index)
plt.ticklabel_format(style='scientific', axis='x', scilimits=(0,0))
plt.tight_layout()
plt.savefig('state_wheat_production.png', dpi=300, bbox_inches='tight')
plt.close()

# 4. Box Plot - Sorghum Yield Distribution
plt.figure(figsize=(10, 8))
sorghum_yield = df['SORGHUM YIELD (Kg per ha)'].replace([0, -1], np.nan).dropna()
plt.boxplot(sorghum_yield, vert=True)
plt.title('Distribution of Sorghum Yields', fontsize=16, fontweight='bold')
plt.ylabel('Yield (Kg per ha)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('sorghum_yield_boxplot.png', dpi=300, bbox_inches='tight')
plt.close()

# 5. Pie Chart - Vegetable Area by State
plt.figure(figsize=(12, 10))
state_veg = df.groupby('State Name')['VEGETABLES AREA (1000 ha)'].sum().sort_values(ascending=False)
# Take top 8 states and group others
top_states = state_veg.head(8)
others = state_veg.iloc[8:].sum()
if others > 0:
    top_states['Others'] = others

plt.pie(top_states.values, labels=top_states.index, autopct='%1.1f%%', startangle=90)
plt.title('Distribution of Vegetable Area by State', fontsize=16, fontweight='bold')
plt.axis('equal')
plt.tight_layout()
plt.savefig('vegetable_area_by_state.png', dpi=300, bbox_inches='tight')
plt.close()

# 6. Scatter Plot - Chickpea Area vs Production Correlation
plt.figure(figsize=(12, 8))
clean_chickpea = df[['CHICKPEA AREA (1000 ha)', 'CHICKPEA PRODUCTION (1000 tons)']].dropna()
clean_chickpea = clean_chickpea[(clean_chickpea > 0).all(axis=1)]
clean_chickpea = clean_chickpea[(clean_chickpea != -1).all(axis=1)]

if len(clean_chickpea) > 0:
    plt.scatter(clean_chickpea['CHICKPEA AREA (1000 ha)'], 
                clean_chickpea['CHICKPEA PRODUCTION (1000 tons)'], 
                alpha=0.6)
    
    # Add trend line
    z = np.polyfit(clean_chickpea['CHICKPEA AREA (1000 ha)'], 
                   clean_chickpea['CHICKPEA PRODUCTION (1000 tons)'], 1)
    p = np.poly1d(z)
    plt.plot(clean_chickpea['CHICKPEA AREA (1000 ha)'], 
             p(clean_chickpea['CHICKPEA AREA (1000 ha)']), "r--", alpha=0.8)
    
    from scipy.stats import pearsonr
    corr, _ = pearsonr(clean_chickpea['CHICKPEA AREA (1000 ha)'], 
                       clean_chickpea['CHICKPEA PRODUCTION (1000 tons)'])
    plt.text(0.02, 0.98, f'Correlation: {corr:.4f}', transform=plt.gca().transAxes, 
             fontsize=12, verticalalignment='top', 
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.title('Chickpea Area vs Production Correlation', fontsize=16, fontweight='bold')
plt.xlabel('Chickpea Area (1000 ha)', fontsize=12)
plt.ylabel('Chickpea Production (1000 tons)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('chickpea_area_production_correlation.png', dpi=300, bbox_inches='tight')
plt.close()

# 7. Bar Chart - Crop Diversity by State
plt.figure(figsize=(14, 8))
crop_columns = [col for col in df.columns if 'AREA' in col and '(1000 ha)' in col and 
               col not in ['FRUITS AND VEGETABLES AREA (1000 ha)', 'OILSEEDS AREA (1000 ha)']]

state_crop_diversity = {}
for state in df['State Name'].unique():
    state_data = df[df['State Name'] == state]
    crop_count = 0
    for crop_col in crop_columns:
        if (state_data[crop_col] > 0).any():
            crop_count += 1
    state_crop_diversity[state] = crop_count

diversity_df = pd.Series(state_crop_diversity).sort_values(ascending=False)
plt.bar(range(len(diversity_df)), diversity_df.values)
plt.title('Number of Different Crops Produced by State', fontsize=16, fontweight='bold')
plt.xlabel('States', fontsize=12)
plt.ylabel('Number of Crops', fontsize=12)
plt.xticks(range(len(diversity_df)), diversity_df.index, rotation=45, ha='right')
plt.tight_layout()
plt.savefig('crop_diversity_by_state.png', dpi=300, bbox_inches='tight')
plt.close()

# 8. Line Chart - Pulse Yield Trends Over Time
plt.figure(figsize=(14, 8))
pulse_crops = {
    'CHICKPEA YIELD (Kg per ha)': 'Chickpea',
    'PIGEONPEA YIELD (Kg per ha)': 'Pigeonpea', 
    'MINOR PULSES YIELD (Kg per ha)': 'Minor Pulses'
}

for pulse_col, pulse_name in pulse_crops.items():
    yearly_yield = df.groupby('Year')[pulse_col].mean()
    yearly_yield = yearly_yield[yearly_yield > 0]
    if len(yearly_yield) > 1:
        plt.plot(yearly_yield.index, yearly_yield.values, 
                marker='o', linewidth=2, label=pulse_name, markersize=4)

plt.title('Pulse Yield Trends Over Years', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Yield (Kg per ha)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('pulse_yield_trends.png', dpi=300, bbox_inches='tight')
plt.close()

# 9. Heatmap - Sorghum Production Patterns (Top Districts)
plt.figure(figsize=(16, 10))

# Get top districts for kharif and rabi sorghum
kharif_by_district = df.groupby(['State Name', 'Dist Name'])['KHARIF SORGHUM AREA (1000 ha)'].sum()
rabi_by_district = df.groupby(['State Name', 'Dist Name'])['RABI SORGHUM AREA (1000 ha)'].sum()

# Get top 15 districts for each
top_kharif = kharif_by_district.nlargest(15)
top_rabi = rabi_by_district.nlargest(15)

# Create combined data for heatmap
heatmap_data = []
labels = []

for (state, district), area in top_kharif.items():
    heatmap_data.append([area, 0])
    labels.append(f"{district}, {state}")

for (state, district), area in top_rabi.items():
    # Check if district already exists
    district_label = f"{district}, {state}"
    if district_label in labels:
        idx = labels.index(district_label)
        heatmap_data[idx][1] = area
    else:
        heatmap_data.append([0, area])
        labels.append(district_label)

heatmap_array = np.array(heatmap_data)
plt.figure(figsize=(10, 12))
sns.heatmap(heatmap_array, 
            xticklabels=['Kharif Sorghum', 'Rabi Sorghum'],
            yticklabels=labels[:20],  # Limit to top 20 for readability
            annot=True, fmt='.0f', cmap='YlOrRd')
plt.title('Sorghum Production Patterns (Top Districts)', fontsize=16, fontweight='bold')
plt.xlabel('Sorghum Season', fontsize=12)
plt.ylabel('Districts', fontsize=12)
plt.tight_layout()
plt.savefig('sorghum_production_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()

print("All visualizations generated successfully!")
