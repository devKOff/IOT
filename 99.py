'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.array([1,2,3])
y = np.array([1,2,3])
x,y = np.meshgrid(x,y)
z = x*y

fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x, y, z, cmap='viridis')


ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
plt.title('Surface Plot of Z = X * Y')
plt.show()

x = np.array([1, 2, 3])
y = np.array([1, 2, 3])
x, y = np.meshgrid(x, y)
Z = x * y
'''
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = {
    'Maths': [90,33,80],
    'Physics': [70,63,60],
    'Bee': [80,84,90]
    }
df = pd.DataFrame(data,index=['Alice','Art','Jobe'])
print(df)
sns.heatmap(df, annot=True, cmap='YlnBu')
plt.title("Students Subject Scores")
plt.show()
'''
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Creating the DataFrame
data = {
    'Maths': [90, 33, 80],
    'Physics': [70, 63, 60],
    'Bee': [80, 84, 90]
}
df = pd.DataFrame(data, index=['Alice', 'Art', 'Jobe'])


print(df)


sns.heatmap(df, annot=True, cmap='YlGnBu')
plt.title("Students Subject Scores")
plt.show()

'''


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.DataFrame({
    'study_hours':[1,2,3,4,5,6],
    'score':[50,55,65,70,75,80],
    'Gender':['male','male','female','female','male','female']
    })
sns.lmplot(x='study_hours',y='score',data=data)

plt.show()




















