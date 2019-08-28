import pandas as pd

df=pd.read_excel('D:/data/Camera4/line17_segments.xlsx')
# head=data.head()
data=df.ix[:].values
print(data)
# print(head)
debug=1