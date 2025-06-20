
import numpy as np
import pandas as pd
"""
labels = ['a','b','c']
my_list = [10,20,30]
arr = np.array([10,20,30])
d = {'a':10,'b':20,'c':30}
#list
pd.Series(data=my_list)
pd.Series(data=my_list,index=labels)
pd.Series(my_list,labels)
#array
pd.Series(arr)
pd.Series(arr,labels)
print(pd.Series(data=my_list))
print(pd.Series(data=my_list,index=labels))
print(pd.Series(my_list,labels))

#dictionary
pd.Series(d)
pd.Series(data=labels)
# Even functions (although unlikely that you will use this)
pd.Series([sum,print,len])
ser1 = pd.Series([1,2,3,4],index = ['USA', 'Germany','USSR', 'Japan'])     
ser1
ser2 = pd.Series([1,2,5,4],index = ['USA', 'Germany','Italy', 'Japan'])  
ser2
ser1 + ser2
print(ser1.add(ser2, fill_value=0))
"""
"""

from numpy.random import randn
np.random.seed(101)
df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
print(df)
print(df['W'])
df['new']=df['W']+df['X']
print(df)
df.drop('new',axis=1,inplace = True)
print(df)
df.drop('A',axis=0,inplace = True)
print(df)
#print(df.loc['A'])

#df.loc[['A','B'],['W','Y']]
print(df>0)
print(df[df['W']>0])
print(df[df['W']>0]['Y'])
"""
"""
from numpy.random import randn
np.random.seed(101)
df = pd.DataFrame(randn(5,4),index='A B C D E'.split(),columns='W X Y Z'.split())
print(df)
print(df.reset_index())
newind='CA NY WY OR FG'.split()
df['States']=newind
print(df)
"""
"""
outside =['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index=list(zip(outside,inside))
hire_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)
"""
"""
df.loc['G1']
df.loc['G1'].loc[1]
df.index.names
df.index.names = ['Group','Num']
"""
"""
df = pd.DataFrame({'A':[1,2,np.nan],
                  'B':[5,np.nan,np.nan],
                  'C':[1,2,3]})


print(df)
print("--"*4)
print(df.dropna())
print("-__-"*4)
print(df.dropna(axis=1))
print("-_-"*4)
print(df.dropna(thresh=2))
print("__"*4)
print(df.fillna(value='FILL VALUE'))




import pandas as pd

data = {
    'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
    'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
    'Sales': [200, 120, 340, 124, 243, 350]
}

df = pd.DataFrame(data)

by_comp = df.groupby('Company')

# Mean sales only (numeric column)
print(by_comp['Sales'].mean())

# Std deviation sales only
print(by_comp['Sales'].std())

# Min of all columns (min for string column works)
print(by_comp.min())

# Max of all columns (max for string column works)
print(by_comp.max())


"""

"""
import pandas as pd

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7]) 

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])

print(df1)

print(df2)

print(df3)

pd.concat([df1,df2,df3])

pd.concat([df1,df2,df3],axis=1)






left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
   
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})

print(left)

print(right)

pd.merge(left,right,how='inner',on='key')

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
    
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                               'key2': ['K0', 'K0', 'K0', 'K0'],
                                  'C': ['C0', 'C1', 'C2', 'C3'],
                                  'D': ['D0', 'D1', 'D2', 'D3']})


print(left)

pd.merge(left, right, on=['key1', 'key2'])

pd.merge(left, right, how='outer', on=['key1', 'key2'])

pd.merge(left, right, how='right', on=['key1', 'key2'])

pd.merge(left, right, how='left', on=['key1', 'key2'])




left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2']) 

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])

print(left)

print(right)

left.join(right)

left.join(right, how='outer')

"""
"""
import pandas as pd
df = pd.DataFrame({'col1':[1,2,3,4, 5, 6, 7],'col2':[444,555,666,444, 555, 555, 666],'col3':['abc','def','ghi','xyz', 'jkl', 'mno', 'pqr']})
df.head()

df['col2'].unique()

df['col2'].nunique()

df['col2'].value_counts()

newdf = df[(df['col1']>2) & (df['col2']==444)]

def times2(x):
    return x*2

df['col1'].apply(times2)

df['col3'].apply(len)

df['col1'].sum()

del df['col1']

df

df.columns

df.index

df

df.sort_values(by='col2')

df.isnull()

df.dropna()

"""


import numpy as np

df = pd.DataFrame({'col1':[1,2,3,np.nan],
                   'col2':[np.nan,555,666,444],
                   'col3':['abc','def','ghi','xyz']})
df.head()

df.fillna('FILL')

data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)

print(df)

print(df.pivot_table(values='D',index=['A', 'B'],columns=['C']))

print(df.pivot_table(values='D',index=['A', 'B'],columns=['C']))




