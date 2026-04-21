import pandas as pd
import numpy as np

## SERIES ##
# contiguous memory; 

a = np.array(['a', 'b', 'c', 1])
a = a + "a"
series1 = pd.Series(a)

print(a)
print(series1)
print(series1[1])

series1 = pd.Series(a, index = ["1", "2", "3", "4"])
print(series1)
print(series1["1"])

dataframe1 = pd.DataFrame(a)
print(dataframe1)

