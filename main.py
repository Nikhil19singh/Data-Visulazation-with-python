import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv("//Users//nikhilsingh//Downloads//water_pollution_disease.csv")

# -----------------------------
# 1. Data Cleaning
# -----------------------------
print("Initial Shape:", df.shape)
print("\nMissing Values:\n", df.isnull().sum())
print("\nDuplicates:", df.duplicated().sum())
print("\nData Types:\n", df.dtypes)

# Drop duplicates
df.drop_duplicates(inplace=True)

# Fill or drop missing values (example: fill with median)
for col in df.select_dtypes(include=['float64', 'int64']).columns:
    df[col] = df[col].fillna(df[col].median())

df.dropna(inplace=True)  # drop remaining rows with nulls

# Rename columns for consistency (if needed)
df.columns = [col.strip().replace(" ", "_").title() for col in df.columns]

# -----------------------------
# 2. Data Visualization
# -----------------------------

# Histogram
plt.figure(figsize=(8,5))
df['Contaminant_Level_(Ppm)'].hist(bins=20, color='skyblue', edgecolor='black')
plt.title("Distribution of Contaminant Level (ppm)")
plt.xlabel("Contaminant Level (ppm)")
plt.ylabel("Frequency")
plt.grid(False)
plt.tight_layout()
plt.show()

# Heatmap of correlations
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()

# Bar plot: Disease Cases by Region
plt.figure(figsize=(10,5))
df.groupby('Region')['Disease_Cases'].sum().sort_values().plot(kind='barh', color='teal')
plt.title("Total Disease Cases by Region")
plt.xlabel("Disease Cases")
plt.tight_layout()
plt.show()

# Boxplot: Contaminant Level across Regions
plt.figure(figsize=(12,6))
sns.boxplot(x='Region', y='Contaminant_Level_(Ppm)', data=df)
plt.xticks(rotation=90)
plt.title("Contaminant Level (ppm) by Region")
plt.tight_layout()
plt.show()

# -----------------------------
# 3. EDA & Statistical Analysis
# -----------------------------

# Correlation between Contaminant Level and Disease Cases
correlation = df[['Contaminant_Level_(Ppm)', 'Disease_Cases']].corr()
print("\nCorrelation between Contaminant Level (ppm) and Disease Cases:\n", correlation)

# Grouped statistics
group_stats = df.groupby('Region')[['Contaminant_Level_(Ppm)', 'Disease_Cases']].mean()
print("\nAverage Contaminant Level & Disease Cases by Region:\n", group_stats)

# -----------------------------
# 4. Creativity & Innovation
# -----------------------------

# Interactive Scatter Plot
