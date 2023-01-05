import pandas as pd
import numpy as np
import os

working_dir = (os.path.dirname(os.path.realpath(__file__))+"\data")
df_salaries = pd.read_csv(working_dir+"\Salaries.csv")
print(df_salaries.head())

police_department = df_salaries[df_salaries["JobTitle"].str.contains("POLICE DEPARTMENT")]
fire_department = df_salaries[df_salaries["JobTitle"].str.contains("FIRE DEPARTMENT")]

number_of_police = len(police_department)
number_of_ff = len(fire_department)

police_vs_ff = number_of_ff/number_of_police

police_mean_base_salary = round(police_department["BasePay"].mean(),2)
fire_mean_base_salary = round(fire_department["BasePay"].mean(),2)

print(f"The number of police is {number_of_police} and their meant base pay is ${police_mean_base_salary}") 
print(f"The number of police is {number_of_ff} and their meant base pay is ${fire_mean_base_salary}") 