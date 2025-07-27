import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
import warnings
warnings.filterwarnings('ignore')

# Load the dataset
df = pd.read_csv('ICRISAT-District Level Data.csv')

print("="*60)
print("ICRISAT DISTRICT LEVEL DATA ANALYSIS")
print("="*60)

print(f"\nDataset shape: {df.shape}")
print(f"Year range: {df['Year'].min()} - {df['Year'].max()}")
print(f"Number of states: {df['State Name'].nunique()}")
print(f"Number of districts: {df['Dist Name'].nunique()}")

print("\nColumns in dataset:")
for i, col in enumerate(df.columns, 1):
    print(f"{i:2d}. {col}")

print("\nStates in dataset:")
print(df['State Name'].unique())

# EASY QUESTIONS
print("\n" + "="*60)
print("EASY QUESTIONS")
print("="*60)

print("\n1. CROP AREA DISTRIBUTION:")
# Calculate total area for rice, wheat, and maize
rice_total = df['RICE AREA (1000 ha)'].sum()
wheat_total = df['WHEAT AREA (1000 ha)'].sum()
maize_total = df['MAIZE AREA (1000 ha)'].sum()

print(f"Total Rice Area: {rice_total:.2f} thousand hectares")
print(f"Total Wheat Area: {wheat_total:.2f} thousand hectares") 
print(f"Total Maize Area: {maize_total:.2f} thousand hectares")

print("\n2. YEARLY PRODUCTION - RICE:")
# Find year with highest rice production
yearly_rice_production = df.groupby('Year')['RICE PRODUCTION (1000 tons)'].sum()
peak_year = yearly_rice_production.idxmax()
peak_production = yearly_rice_production.max()
print(f"Year with highest rice production: {peak_year}")
print(f"Peak rice production: {peak_production:.2f} thousand tons")

print("\n3. STATE PRODUCTION - WHEAT:")
# Find states with highest and lowest wheat production
state_wheat_production = df.groupby('State Name')['WHEAT PRODUCTION (1000 tons)'].sum().sort_values(ascending=False)
highest_state = state_wheat_production.index[0]
lowest_state = state_wheat_production.index[-1]
print(f"State with highest wheat production: {highest_state} ({state_wheat_production.iloc[0]:.2f} thousand tons)")
print(f"State with lowest wheat production: {lowest_state} ({state_wheat_production.iloc[-1]:.2f} thousand tons)")

print("\n4. CROP YIELDS - SORGHUM:")
# Calculate average yield for sorghum
sorghum_yield = df['SORGHUM YIELD (Kg per ha)'].replace([0, -1], np.nan).dropna()
avg_sorghum_yield = sorghum_yield.mean()
median_sorghum_yield = sorghum_yield.median()
std_sorghum_yield = sorghum_yield.std()
print(f"Average sorghum yield: {avg_sorghum_yield:.2f} kg per ha")
print(f"Median sorghum yield: {median_sorghum_yield:.2f} kg per ha")
print(f"Standard deviation: {std_sorghum_yield:.2f} kg per ha")

print("\n5. VEGETABLE AREA:")
# Calculate total vegetable area and find state with maximum
total_veg_area = df['VEGETABLES AREA (1000 ha)'].sum()
state_veg_area = df.groupby('State Name')['VEGETABLES AREA (1000 ha)'].sum().sort_values(ascending=False)
max_veg_state = state_veg_area.index[0]
print(f"Total vegetable area: {total_veg_area:.2f} thousand hectares")
print(f"State with maximum vegetable area: {max_veg_state} ({state_veg_area.iloc[0]:.2f} thousand hectares)")

# MEDIUM QUESTIONS
print("\n" + "="*60)
print("MEDIUM QUESTIONS")
print("="*60)

print("\n1. AREA vs PRODUCTION CORRELATION - CHICKPEA:")
# Calculate correlation between chickpea area and production
clean_chickpea = df[['CHICKPEA AREA (1000 ha)', 'CHICKPEA PRODUCTION (1000 tons)']].dropna()
clean_chickpea = clean_chickpea[(clean_chickpea != 0).all(axis=1)]
clean_chickpea = clean_chickpea[(clean_chickpea != -1).all(axis=1)]

if len(clean_chickpea) > 0:
    correlation_coeff, p_value = pearsonr(clean_chickpea['CHICKPEA AREA (1000 ha)'], 
                                          clean_chickpea['CHICKPEA PRODUCTION (1000 tons)'])
    print(f"Correlation coefficient: {correlation_coeff:.4f}")
    print(f"P-value: {p_value:.4f}")
    
    if abs(correlation_coeff) < 0.3:
        strength = "weak"
    elif abs(correlation_coeff) < 0.7:
        strength = "moderate"
    else:
        strength = "strong"
    
    print(f"Interpretation: {strength} positive correlation")

print("\n2. DIVERSITY OF CROPS:")
# Count number of different crops produced in each state
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

print("Number of crops produced per state:")
for state, count in sorted(state_crop_diversity.items(), key=lambda x: x[1], reverse=True):
    print(f"{state}: {count} crops")

# HARD QUESTIONS
print("\n" + "="*60)
print("HARD QUESTIONS")
print("="*60)

print("\n1. LONGITUDINAL YIELD TRENDS - MAJOR PULSES:")
# Analyze yield changes for major pulses over years
pulse_crops = ['CHICKPEA YIELD (Kg per ha)', 'PIGEONPEA YIELD (Kg per ha)', 'MINOR PULSES YIELD (Kg per ha)']

print("Yield trends for major pulses:")
for pulse in pulse_crops:
    yearly_yield = df.groupby('Year')[pulse].mean()
    yearly_yield = yearly_yield[yearly_yield > 0]  # Remove zeros
    
    if len(yearly_yield) > 1:
        start_yield = yearly_yield.iloc[0]
        end_yield = yearly_yield.iloc[-1]
        change_percent = ((end_yield - start_yield) / start_yield) * 100
        
        crop_name = pulse.replace(' YIELD (Kg per ha)', '')
        print(f"{crop_name}: {start_yield:.0f} -> {end_yield:.0f} kg/ha ({change_percent:+.1f}%)")

print("\n2. SORGHUM PRODUCTION PATTERNS:")
# Analyze kharif and rabi sorghum patterns
kharif_total = df.groupby(['State Name', 'Dist Name'])['KHARIF SORGHUM AREA (1000 ha)'].sum()
rabi_total = df.groupby(['State Name', 'Dist Name'])['RABI SORGHUM AREA (1000 ha)'].sum()

kharif_districts = len(kharif_total[kharif_total > 0])
rabi_districts = len(rabi_total[rabi_total > 0])

print(f"Districts growing Kharif sorghum: {kharif_districts}")
print(f"Districts growing Rabi sorghum: {rabi_districts}")

# Find top districts for each season
top_kharif = kharif_total.nlargest(5)
top_rabi = rabi_total.nlargest(5)

print(f"\nTop 5 districts for Kharif sorghum:")
for (state, district), area in top_kharif.items():
    print(f"  {district}, {state}: {area:.2f} thousand ha")

print(f"\nTop 5 districts for Rabi sorghum:")
for (state, district), area in top_rabi.items():
    print(f"  {district}, {district}: {area:.2f} thousand ha")

print("\nAnalysis complete!")
