import numpy as np
import pandas as pd

label =["a","b","c"]
my_lst = [10,20,30]
arr=np.array([10,20,30])
d = {"a":10,"b":20,"c":30}
print(arr)
print(pd.Series(data=my_lst))
print(pd.Series(arr,label))
print(pd.Series(d))
