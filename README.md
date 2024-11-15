This project focuses on exploring two datasets: Exercise Data and Planets Data, to gain insights into health trends and exoplanetary discoveries through visualization. The purpose is to identify patterns and relationships in the data using statistical and graphical analysis, offering a comprehensive view of the interactions between variables like diet, exercise, planet mass, distance, and discovery methods. The project utilizes Python libraries such as pandas, matplotlib, and seaborn for data manipulation and visualization. The analysis demonstrates the role of visual storytelling in uncovering meaningful trends and biases in datasets.
Attributes:
self.data: Stores the raw or processed dataset.
self.file_path: Stores the path to the dataset file.
Methods:
load_data(): Loads data from a CSV file into a Pandas DataFrame.
clean_data(): Cleans and handles missing values or inconsistencies in the dataset.
melt_data(id_vars, value_vars, var_name, value_name): Transforms wide-format data into long-format for analysis.
create_heatmap(pivot_table_args, title, xlabel, ylabel, cmap='coolwarm'): Generates a heatmap using a pivot table.
create_boxplot(x, y, hue, title, xlabel, ylabel): Creates a box plot to compare distributions across categories.
create_scatterplot(x, y, title, xlabel, ylabel): Plots scatter plots to visualize relationships between two numerical variables.
create_lineplot(x, y, title, xlabel, ylabel): Generates line plots to show trends over time.
create_histplot(column, bins, kde, title, xlabel, ylabel): Displays a histogram with optional kernel density estimation.
create_kdeplot(column, title, xlabel, ylabel): Plots a kernel density estimation (KDE) for a continuous variable.
create_countplot(x, title, xlabel, ylabel): Creates a count plot to display the frequency of categorical variables.
