import numpy as np
import pandas as pd

myindex = ['USA', 'CHINA', 'JAPAN']
mydata = [1772, 3123, 2233]

myser = pd.Series(data=mydata, index=myindex)
print(myser)
print()

ages = {'john': 12, 'johny': 52}
print(pd.Series(ages))
