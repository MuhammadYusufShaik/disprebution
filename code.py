import pandas as pd
import plotly.figure_factory as ff
df=pd.read_csv('C:/Users/khada/Downloads/python/c108/data.csv')
height=df['Height(Inches)'].tolist()
graph=ff.create_distplot([height],['bell graph'],show_hist=False)
graph.show()