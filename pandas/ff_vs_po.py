import pandas as pd
import numpy as np
import os
import datetime

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

unique_jobs = list(df_salaries["JobTitle"].unique())
number_of_unique_jobs = len(unique_jobs)

print(f"There is {number_of_unique_jobs} jobs and it includes {unique_jobs}")

first_name = df_salaries["EmployeeName"].apply(lambda x:x.split()[0])
number_of_johns = first_name.apply(lambda x: x.count("JOHN")).sum()
first_name_length = first_name[first_name.apply(lambda x: len(x) > 6)]

print(number_of_johns)
print(first_name_length)

df_salaries["last_updated"] = datetime.datetime.now().isoformat()

df_salaries["time_ratio"] = df_salaries["OvertimePay"]/df_salaries["BasePay"]

new_df = df_salaries[df_salaries["BasePay"] > 100000]

new_df["TotalPay"] = new_df["BasePay"] + new_df["OvertimePay"] + new_df["OtherPay"]
new_df = new_df.drop("BasePay", axis = 1)

print(new_df)