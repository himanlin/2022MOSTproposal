import pandas as pd
import pandas
from pandas.core.frame import DataFrame
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df2 = pd.read_csv('output1024.csv')
df2 = df2.T # or df1.transpose()
name=[0,0.25,0.5,0.75,1]
df2.columns=name
#df2=df.iloc[[20000]]

df = pd.read_csv('output_250.csv')
df = df.T # or df1.transpose()
name=[0,0.25,0.5,0.75,1]
df.columns=name
df2=df2.append(df.iloc[[20000]])

df = pd.read_csv('output_50.csv')
df = df.T # or df1.transpose()
name=[0,0.25,0.5,0.75,1]
df.columns=name
df2=df2.append(df.iloc[[20000]])

df = pd.read_csv('output_10.csv')
df = df.T # or df1.transpose()
name=[0,0.25,0.5,0.75,1]
df.columns=name
df2=df2.append(df.iloc[[20000]])

df = pd.read_csv('output_5.csv')
df = df.T # or df1.transpose()
name=[0,0.25,0.5,0.75,1]
df.columns=name
df2=df2.append(df.iloc[[20000]])

df = pd.read_csv('output_2.csv')
df = df.T # or df1.transpose()
name=[0,0.25,0.5,0.75,1]
df.columns=name
df2=df2.append(df.iloc[[20000]])



df2.index = [1250,250,50,10,5,2,51]
df2.drop(51 , inplace=True)
'''
df = df.drop('Unnamed: 0')
lines = df.plot.line()
plt.rcParams["figure.figsize"] = (8,4)
plt.ylabel('fraction of cooperation')
plt.xlabel('iteration')
plt.title("Peer pressure")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.rcParams.update({'font.size': 16})
plt.ylim(0, 1)
plt.xlim(0, 20000)
plt.tight_layout()
#plt.savefig("cooperation.png", format="png")
plt.show()
'''
df = pd.read_csv('out2.csv',header=None)
name=[1,2,4,8,16,32,64,128,256,512]
df.columns=name
df=df.sort_index(ascending=False)

yticks = np.array([1,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1,0])
#YlGnBu,magma
fig = sns.heatmap(df, annot=False,cmap="YlGnBu",yticklabels=yticks,vmax=1,cbar_kws={'label': 'Final fraction of cooperators'})
#sns.set(font_scale=2)
plt.yticks(rotation=0) 
plt.rcParams["figure.figsize"] = (6,5)
plt.ylabel("peer pressure", fontsize = 24)
plt.xlabel("Group", fontsize = 24)
fig.figure.axes[-1].yaxis.label.set_size(20)
plt.tight_layout()
#plt.savefig("cooperation.png", format="png") # You can comment this line out if you don't need title
plt.show(fig)