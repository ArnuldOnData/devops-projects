# Import necessary libraries
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import pandas as pd

# Load the Iris dataset
iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['species'] = iris.target

# Map species target numbers to actual species names
species_names = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
iris_df['species'] = iris_df['species'].map(species_names)

# Create a color map for the species
colors = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}

# Scatter plot using matplotlib
plt.figure(figsize=(8, 6))

for species, color in colors.items():
    subset = iris_df[iris_df['species'] == species]
    plt.scatter(subset['sepal length (cm)'], subset['sepal width (cm)'], 
                color=color, label=species)

plt.title('Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.legend(title='Species')
plt.grid(True)

# Save the plot as a PNG file
plt.savefig("sepal-length-vs-width.png")

# Show the plot
plt.show()
