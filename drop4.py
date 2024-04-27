import pandas as pd
import numpy as np
scores_df= pd.DataFrame({'NAME':['SAM','SONIYA','SARRITA'],
                         'MATH':[46,np.nan,76],'HISTORY':[45,65,np.nan],'SCIENCE':[np.nan,69,74]})

df=pd.DataFrame(scores_df)
print(df)

