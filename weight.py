import pandas as pd
import plotly.figure_factory as ff
df=pd.read_csv('C:/Users/khada/Downloads/python/c108/data.csv')
weight=df['Weight(Pounds)'].tolist()
graph=ff.create_distplot([weight],['bell graph'],show_hist=False)
graph.show()