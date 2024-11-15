import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
exercise_data = pd.read_csv('C:/Users/desir/Downloads/Exercise_Data.csv')

print("Exercise Data Sample:")
print(exercise_data.head())

exercise_data_melted = exercise_data.melt(id_vars=['id', 'diet', 'kind'], 
                                          value_vars=['1 min', '15 min', '30 min'], 
                                          var_name='Time', 
                                          value_name='Pulse')

heatmap_data = exercise_data_melted.pivot_table(index="diet", columns="Time", values="Pulse")

plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data, annot=True, cmap='coolwarm')
plt.title('Heatmap of Pulse Data by Diet and Time')
plt.xlabel('Time')
plt.ylabel('Diet')
plt.show()

plt.figure(figsize=(10, 6))
sns.catplot(data=exercise_data_melted, x='diet', y='Pulse', hue='kind', kind='box')
plt.title('Pulse by Diet and Exercise Type')
plt.xlabel('Diet')
plt.ylabel('Pulse')
plt.show()

#The heatmap shows that people with a "no fat" diet tend to have higher pulse rates over time compared to those on a "low fat" diet. This suggests that diet can affect how the heart responds during exercise or rest. Understanding this can help students see how food choices might impact their bodies during different activities.
#The box plot reveals that pulse rates are lowest when resting, increase a bit when walking, and are highest when running. It also shows that a "no fat" diet leads to slightly higher pulse rates, especially during running. This helps students see how both diet and exercise type can influence heart rate, highlighting the importance of balanced exercise and healthy eating.

planets = sns.load_dataset('planets')

print("Planets Data Sample:")
print(planets.head())

plt.figure(figsize=(10, 6))
sns.scatterplot(data=planets, x='orbital_period', y='mass')
plt.title('Orbital Period vs. Mass')
plt.xlabel('Orbital Period')
plt.ylabel('Mass')
plt.show()
#This scatter plot shows that most planets have a low orbital period and mass. However, there are a few planets with extremely high orbital periods, indicating that they orbit their stars at a much slower rate. This graph highlights the diversity of exoplanetary characteristics and helps visualize the relationship between mass and orbital period.

plt.figure(figsize=(10, 6))
sns.lineplot(data=planets, x='year', y='distance')
plt.title('Year vs. Distance')
plt.xlabel('Year')
plt.ylabel('Distance')
plt.show()
#The line plot demonstrates how the distance of discovered planets has varied over the years, with peaks around certain years. The peak in distance around 2005 might indicate a period when technology allowed for the discovery of more distant planets. This plot emphasizes how advancements in technology and exploration techniques have expanded our reach into distant space.

plt.figure(figsize=(10, 6))
sns.histplot(planets['mass'].dropna(), bins=30, kde=True)
plt.title('Distribution of Planet Mass')
plt.xlabel('Mass')
plt.ylabel('Frequency')
plt.show()
#The histogram shows that most discovered planets have relatively low mass, with only a few having a significantly higher mass. This skewed distribution suggests that lower-mass planets are more commonly detected, possibly due to detection biases in the technology used.

plt.figure(figsize=(10, 6))
sns.kdeplot(planets['distance'].dropna())
plt.title('Distribution of Planet Distance')
plt.xlabel('Distance')
plt.ylabel('Density')
plt.show()
#The KDE plot reveals that most planets are located at closer distances, with very few found at extreme distances. This highlights detection limitations and shows that nearby planets are more easily discovered.

plt.figure(figsize=(10, 6))
sns.boxplot(data=planets, x='method', y='orbital_period')
plt.title('Orbital Period by Discovery Method')
plt.xlabel('Discovery Method')
plt.ylabel('Orbital Period')
plt.xticks(rotation=90)
plt.show()
#This box plot shows the variability in orbital periods based on the discovery method. For example, planets discovered through "Imaging" tend to have a much higher orbital period range compared to other methods, likely due to the method's focus on planets farther from their stars. This graph illustrates how different detection methods affect the types of planets identified.

plt.figure(figsize=(10, 6))
sns.countplot(data=planets, x='method')
plt.title('Discovery Methods Count')
plt.xlabel('Discovery Method')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.show()
#The bar plot clearly shows that "Radial Velocity" and "Transit" are the most common discovery methods. This suggests that these methods are the most effective or widely used in finding exoplanets, providing insight into trends in exoplanet discovery techniques.

#The most notable graphs are the Year vs. Distance and Discovery Methods Count plots. The Year vs. Distance line plot demonstrates the impact of technological advancements on the distances of detected planets, while the Discovery Methods Count bar plot highlights the popularity and effectiveness of specific detection methods.