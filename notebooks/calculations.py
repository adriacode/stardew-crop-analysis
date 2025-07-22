# %%

import pandas as pd

# %%
df = pd.read_csv("../data/processed_data.csv", sep=",")
df.head()

# %%
df["growth_time"] = pd.to_numeric(df["growth_time"], errors="coerce")
df["regrowth_time"] = pd.to_numeric(df["regrowth_time"], errors="coerce")

# %%

def calculate_harvest(row):

    regrowth = row["regrowth_time"]
    growth = row["growth_time"]


    if pd.isna(growth) or growth <= 0:
        return 0

    if regrowth > 0 and pd.notna(regrowth):
        return 1 + ((28 - growth) // regrowth)
    
    else:
        return 28 // growth

df["qt_harvest"] = df.apply(calculate_harvest, axis=1)
df   

# %%
