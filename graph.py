import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

df = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [23, 45, 12, 36]
})

data = np.random.randn(1000)

iris = sns.load_dataset('iris')

# 1. Line Graph
plt.figure(figsize=(6, 4))
plt.plot(x, y, label="sin(x)", color='blue')
plt.title("Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()

# 2. Bar Chart
plt.figure(figsize=(6, 4))
plt.bar(df['Category'], df['Values'], color='green')
plt.title("Bar Chart")
plt.xlabel("Category")
plt.ylabel("Values")
plt.show()

# 3. Histogram
plt.figure(figsize=(6, 4))
plt.hist(data, bins=30, color='purple', edgecolor='black')
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot
plt.figure(figsize=(6, 4))
plt.scatter(iris['sepal_length'], iris['petal_length'], c=iris['species'].astype('category').cat.codes)
plt.title("Scatter Plot")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.show()

# 5. Pie Chart
plt.figure(figsize=(6, 6))
plt.pie(df['Values'], labels=df['Category'], autopct='%1.1f%%', startangle=140)
plt.title("Pie Chart")
plt.axis('equal')
plt.show()

# 6. Box Plot
plt.figure(figsize=(6, 4))
sns.boxplot(data=iris, x='species', y='sepal_width')
plt.title("Box Plot")
plt.show()

# 7. Heatmap
plt.figure(figsize=(6, 4))
corr = iris.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Heatmap")
plt.show()

# 8. Violin Plot
plt.figure(figsize=(6, 4))
sns.violinplot(data=iris, x='species', y='petal_length')
plt.title("Violin Plot")
plt.show()

# 9. Area Plot
df_area = pd.DataFrame({
    'A': np.random.rand(10),
    'B': np.random.rand(10),
    'C': np.random.rand(10)
}, index=range(1, 11))

df_area.plot.area(alpha=0.5)
plt.title("Area Plot")
plt.xlabel("Index")
plt.ylabel("Value")
plt.show()

# 10. Pair Plot
sns.pairplot(iris, hue='species')
plt.suptitle("Pair Plot", y=1.02)
plt.show()
