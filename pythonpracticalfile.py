import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.express

sim= pd.DataFrame({'NAME':['A','B','C','D','E'],
                         'Python Marks':[20,40,30,37,25]})

df=pd.DataFrame(sim)
print(df)
plt.scatter(sim)
