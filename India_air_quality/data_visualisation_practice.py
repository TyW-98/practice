import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
import json

working_dir = (os.path.dirname(os.path.realpath(__file__)))
csv_file = working_dir + "\India_Air_Quality.csv"
df = pd.read_csv(csv_file,encoding= 'cp1252')

column_names = list(df.columns.values)
print(column_names)
Number_of_NANs = {column: df[column].isna().sum() for column in column_names}
    
print(Number_of_NANs)

fig_1 = px.scatter(df, x = "so2", y = "no2", color = "pm2_5", title = "so2 vs no2 vs pm2_5")
fig_1.show()

States = df.groupby("state")

India_states_geojson = working_dir + "\india_state.geojson"

with open(India_states_geojson) as india_geojson_file:
    india_geojson = json.load(india_geojson_file)

fig = px.choropleth(States, geojson = india_geojson, locations = "state", color = "so2", scope = "india") 