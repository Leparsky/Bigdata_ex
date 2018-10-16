
import numpy as np
import pandas as pd

data=None
data1=None

#for i in range(1880,2011):
for i in range(1880,1885):
    data1 = pd.read_csv(r'.\babynames\yob{}.txt'.format(i), sep=",", header=None)
    data1['Year']=i
    data1.columns=["name","gender","number","year"]
    data = pd.concat([data,data1], ignore_index=True)
data.info
#data1[(data1["Name"].isin(["Rene","Mary"]))]
