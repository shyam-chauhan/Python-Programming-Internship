import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load the DataSet:
iris_df = sns.load_dataset('iris')

# 2. Exploratory Data Analysis (EDA):
print("Dataset information:")
print(iris_df.info())

print("\nSummary statistics:")
print(iris_df.describe())

print("\nFirst few rows of the dataset:")
print(iris_df.head())

# 3. Data Cleaning:
print("\nChecking for missing values:")
print(iris_df.isnull().sum())

print("\nChecking for duplicate rows:")
print(iris_df.duplicated().sum())

# 4. Aggregation:
species_mean = iris_df.groupby('species').mean()

# 5. Visualizations:
# Pairplot
sns.pairplot(iris_df, hue='species')
plt.suptitle('Pairplot of Iris Dataset', y=1.02)
plt.show()

# Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(iris_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# 6. Correlation Calculations:
correlation_matrix = iris_df.corr()
