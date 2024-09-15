# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import pandas as pd

# Load the Iris dataset
iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['species'] = iris.target

# Map species target numbers to actual species names
species_names = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
iris_df['species'] = iris_df['species'].map(species_names)

# Set up plotting style
sns.set(style="whitegrid")

# Scatter plot of Sepal Length vs Sepal Width
plt.figure(figsize=(8, 6))
sns.scatterplot(x='sepal length (cm)', y='sepal width (cm)', hue='species', data=iris_df, palette='Set1')
plt.title('Sepal Length vs Sepal Width')

# Save the plot to a PNG file
plt.savefig("sepal-length-vs-width.png")
plt.show()
