import pandas as pd
scores_df= pd.DataFrame({'NAME':['SAM','SONIYA','SARRITA','MAYANK','SHIVANI','MONIKA','PRITAM'],
                         'MATH':[46,89,76,45,33,55,54],'HISTORY':[45,65,44,87,65,45,32],'SCIENCE':[85,69,74,34,21,97,21]
                         ,'PHYSICS':[46,89,76,35,35,55,54],'CHEMISTRY':[45,95,44,47,65,45,32]})
"""print(scores_df.mean(axis=1))
print(scores_df.mean())
scores_df.loc[(scores_df.NAME & it'SAM'),['HISTORY']] = 22
scores_df.loc[1,"NAME"]="RAHUL"
scores_df.loc[2,"SCIENCE"]="56"
print(scores_df.iloc[[0,1]])
print(scores_df)
print(scores_df.iloc[1:3,1:3])
a=scores_df.groupby(['NAME'])
print(a.first())
B=scores_df.groupby(['MATH'])
print(B.first())

SS=scores_df.sum(axis=1,skipna=True)
print(SS)
SS=scores_df.min(axis=0,skipna=True)
print(SS)
so=scores_df.agg(['sum','min','max'])
print(so)"""
so=scores_df.agg(['sum','min','max'])
print(so)

