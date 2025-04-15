import pandas as pd
from sqlalchemy import create_engine

warren = pd.read_csv("/workspace/data/Warren.csv")
warren_calories = pd.read_csv("/workspace/data/Warren_calories.csv")
west = pd.read_csv("/workspace/data/West.csv")
west_calories = pd.read_csv("/workspace/data/West_calories.csv")
marciano= pd.read_csv("/workspace/data/Marciano.csv")
marciano_calories = pd.read_csv("/workspace/data/Marciano_calories.csv")
granby = pd.read_csv("/workspace/data/Granby.csv")
granby_calories = pd.read_csv("/workspace/data/Granby_calories.csv")
dhall = pd.read_csv("/workspace/data/dining.csv")

engine = create_engine("postgresql://app_user:app_password@localhost:5432/app")  # adjust accordingly
warren.to_sql("Warren", engine, if_exists="replace", index=False)
warren_calories.to_sql("Warren_Calories", engine, if_exists="replace", index=False)
west.to_sql("West", engine, if_exists="replace", index=False)
west_calories.to_sql("West_Calories", engine, if_exists="replace", index=False)
marciano.to_sql("Marciano", engine, if_exists="replace", index=False)
marciano_calories.to_sql("Marciano_Calories", engine, if_exists="replace", index=False)
granby.to_sql("Granby", engine, if_exists="replace", index=False)
granby_calories.to_sql("Granby_Calories", engine, if_exists="replace", index=False)
dhall.to_sql("Dhall", engine, if_exists="replace", index=False)
print("Data should be loaded into Postgres")