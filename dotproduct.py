import numpy as np 
import pandas as pd

v1 = pd.np.array([1,2,3])
v2 = pd.np.array([2,3,4])

#sum
result = sum([x1 * x2 for x1, x2 in zip(v1, v2)])
print(v1.dot(v2))
print(result)