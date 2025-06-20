#import matplotlib.pyplot as plt

'''
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 7, 5]


x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 7, 5]

plt.plot(x, y,marker='s',color='pink',linestyle='--')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Groth rate')

# Show the graph
plt.show()

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 7, 5]

plt.subplot(1,2,1)

plt.plot(x,y,'r--')
plt.subplot(1,2,2)
plt.plot(x,y,'g*-')
plt.show()

'''

'''
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 7, 5]
fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])
axes1.plot(x,y,'b*-')
axes1.set_xlabel('X_lable_axes1')
axes1.set_ylabel('Y_lable_axes1')
axes1.set_title('Axes 1 Title')

axes2.plot(x,y,'r--')
axes2.set_xlabel('X_lable_axes1')
axes2.set_ylabel('Y_lable_axes1')
axes2.set_title('Axes 2 Title')
fig.savefig("Graph.png")

plt.show()
'''

'''
import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]

fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])

ax.plot(x, [i ** 2 for i in x], label="x**2",alpha=0.6,lw=10)
ax.plot(x, [i ** 3 for i in x], label="x**3")
ax.legend()
plt.scatter()
plt.show()
'''

'''
age = [12,14,14,17,18,19,37]
plt.hist(age,bins=5,color='skyblue',edgecolor='black')
plt.title("Histogram")
plt.xlabel("Age")
plt.ylabel("Count")

plt.show()
'''
'''
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
# Sample data
data = {
    'Subject': ['Math', 'Math', 'Math', 'Science', 'Science', 'Science'],
    'Marks': [85, 90, 95, 70, 75, 80]
}

# Convert to DataFrame
df = pd.DataFrame(data) 

sns.boxplot(x='Subject', y='Marks', data=df)
plt.title('Boxplot of Marks by Subject')
plt.show()
'''
'''
import seaborn as sns
import matplotlib.pyplot as plt
# Small list of test scores
scores = [60, 62, 65, 67, 70, 72, 75, 78, 80]
sns.kdeplot(scores, fill=True, color='skyblue', linewidth=2)
plt.title('KDE Plot of Test Scores')
plt.xlabel('Score')
plt.ylabel('Density')
plt.show()
'''
'''
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create a small dataset
data = {
    'Height': [150, 160, 170, 180, 190],
    'Weight': [50, 60, 70, 80, 90],
    'Age': [10, 20, 30, 40, 50],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male']
}

df = pd.DataFrame(data)

# Create a pairplot
sns.pairplot(df, hue='Gender', palette='Set2')
#sns.pairplot(df, hue='Gender', diag_kind='hist')
plt.show()

'''


'''


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample dataset: Average scores by subject
data = pd.DataFrame({
    'Subject': ['Math', 'Science', 'English', 'History'],
    'Average_Score': [85, 90, 78, 88]
    })

sns.barplot(x='Subject', y='Average_Score', data=data)

# Add Labels and title
plt.title("Average Scores by Subject")
plt.ylabel("Average| Score")
plt.xlabel("Subject")
plt.show()

'''
'''
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    'Day': ['Mon', 'Mon', 'Tue', 'Tue', 'Mon', 'Tue', 'Mon', 'Tue' ],
    'Score': [5, 6, 6, 7, 8, 5, 9, 6],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Female', 'Male']
})
sns.violinplot(
    X='Day',
    y='Score',
    hue='Gender',
    data=data,
    split=True,
    palette='Set2'
)
plt.title("Violin Plot of Scores by Day and Gender")
plt.show()

'''
'''
import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')


plt.figure(figsize=(8, 5))
sns.violinplot(x='species', y='petal_length', data=iris, palette='muted')


plt.title('Violin Plot of Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Petal Length')

'''
'''
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


data = pd.DataFrame({
    'Day': ['Mon', 'Mon', 'Tue', 'Tue', 'Mon', 'Tue', 'Mon', 'Tue'],
    'Score': [5, 6, 6, 7, 8, 5, 9, 6],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Female', 'Male'],
})


sns.stripplot(
    x='Day',
    y='Score',
    hue='Gender',
    data=data,
    dodge=True,
    jitter=True,
    palette='Set2',
    linewidth=1,
    edgecolor='gray'
)

plt.title("Strip Plot of Scores by Day and Gender")
plt.show()
'''























































































































































































