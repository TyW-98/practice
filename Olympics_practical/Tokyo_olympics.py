import pandas as pd
import numpy as np
import seaborn as sns
import glob
import matplotlib.pyplot as plt

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
f = plt.figure(1)
sns.barplot(data = Entries_gender, x = "Discipline", y = "value", hue = "sex")

Athletes = dataframe_dict["Athletes"].drop("Name", axis = 1)
Athletes = Athletes.groupby("NOC").size().reset_index()
print(Athletes.columns.values.tolist())
f = plt.figure(2)
sns.barplot(x = Athletes["NOC"], y = Athletes.iloc[:,1])

Teams = dataframe_dict["Teams"]
Teams["NOC"] = Teams["NOC"].astype('category')
f = plt.figure(3)
Teams.drop("Name", axis = 1, inplace = True)
sns.countplot(data = Teams, x = "Discipline")
plt.show()

Medals = dataframe_dict["Medals"]
print(Medals)
