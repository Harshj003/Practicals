import pandas as pd
data1 = {'Name':['Jai','Ram','Shyam','Mohan'],
        'Age':[27,24,22,32],
        'Address':['Nagpur','Kanpur','Allahabad','Surat'],
        'Qualification':['BE','ME','MTech','Phd']}
data2 = {'Name':['Abhi','Ayushi','Mayank','Dipesh'],
        'Age':[17,14,12,52],
        'Address':['Nagpur','Kanpur','Allahabad','Surat'],
        'Qualification':['BTech','BA','Bcom','BSC']}
df = pd.DataFrame(data1,index=[0,1,2,3])
df1 = pd.DataFrame(data2,index=[4,5,6,7])
print(df,"\n\n",df1)
frames = [df,df1]
res1 = pd.concat(frames)
res1
