import pandas as pd
import numpy as np
import seaborn as sns
import glob
import matplotlib.pyplot as plt
import plotly.express as px

data_files = glob.glob(r"data"+"\*.xlsx")
dataframe_dict = {}
column_names = {}

for file in data_files:
    file_name = file.replace(".xlsx","").split("\\")
    df = pd.read_excel(file)
    dataframe_dict[file_name[1]] = df
    column_names[file_name[1]] = df.columns.values.tolist()
    
print(column_names)
    
Entries_gender = pd.melt(dataframe_dict["EntriesGender"].drop("Total", axis = 1),id_vars = "Discipline",var_name = "sex")
fig_1 = px.bar(Entries_gender, x = "Discipline", y = "value", color = "sex", title = "Gender split in each sports")
fig_1.update_layout(xaxis_tickangle = -45)
fig_1.show()

Athletes = dataframe_dict["Athletes"].drop("Name", axis = 1)
Athletes = Athletes.groupby("NOC").size().reset_index()
Athletes.rename(columns = {Athletes.columns[1]:"Number of Athletes"}, inplace = True)
fig_2 = px.bar(Athletes, x = "NOC",y = "Number of Athletes", title = "Number of athletes per country")
fig_2.update_layout(xaxis_tickangle = -45)
fig_2.show()

Teams = dataframe_dict["Teams"]
Teams["NOC"] = Teams["NOC"].astype('category')
Teams.drop("Name", axis = 1, inplace = True)
Teams = Teams.groupby("Discipline").size().reset_index()
Teams.rename(columns = {Teams.columns[1]:"Number of Teams"},inplace = True)
fig_3 = px.bar(Teams, x = "Discipline",y = "Number of Teams", title = "Number of teams in each discipline")
fig_3.update_layout(xaxis_tickangle = -45)
fig_3.show()

Medals = dataframe_dict["Medals"]
fig_4 = px.bar(Medals, x = "Team/NOC", y = ["Gold","Silver","Bronze"], title = "Each nation's medals")
fig_4.update_layout(xaxis_tickangle = -45)
fig_4.show()
