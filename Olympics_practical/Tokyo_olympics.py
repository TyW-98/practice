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
    
Entries_gender = pd.melt(dataframe_dict["EntriesGender"].drop("Total", axis = 1),id_vars = "Discipline",var_name = "sex")
print(Entries_gender)
f = plt.figure(1)
sns.barplot(data = Entries_gender, x = "Discipline", y = "value", hue = "sex")
plt.show()