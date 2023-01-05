import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

working_dir = (os.path.dirname(os.path.realpath(__file__)))
csv_file = working_dir + "\India_Air_Quality.csv"
df = pd.read_csv(csv_file,encoding= 'cp1252')

column_names = list(df.columns.values)
print(column_names)
Number_of_NANs = {}

for column in column_names:
    Number_of_NANs[column] = df[column].isna().sum()
    
print(Number_of_NANs)
    