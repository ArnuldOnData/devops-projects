# Import necessary libraries
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

# Load the Iris dataset
iris_data = load_iris()
iris_df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
iris_df['species'] = iris_data.target

# Map the species target numbers to species names
species_mapping = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
iris_df['species'] = iris_df['species'].map(species_mapping)

# Count the occurrences of each species
species_counts = iris_df['species'].value_counts()

# Create the plot using Matplotlib
plt.figure(figsize=(8, 5))
plt.bar(species_counts.index, species_counts.values, color=['blue', 'orange', 'green'])

# Add title and labels
plt.title('Count of Each Species in the Iris Dataset', fontsize=14)
plt.xlabel('Species', fontsize=12)
plt.ylabel('Count', fontsize=12)

# Save the plot as a PNG file
plt.savefig('output.png')
