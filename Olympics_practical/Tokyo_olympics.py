import pandas as pd
import numpy as np
import copy
import glob

data_files = glob.glob(r"data"+"\*.xlsx")
file_name_list = []
dataframe_dict = {}

for file in data_files:
    print(file)
    file_name = file.replace(".xlsx","").split("\\")
    df = pd.read_excel(file)
    dataframe_dict[file_name[1]] = df
    
print(list(dataframe_dict.keys()))

