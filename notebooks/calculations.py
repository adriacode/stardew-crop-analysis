# %%

import pandas as pd

# %%
df = pd.read_csv("../data/processed_data.csv", sep=";")
df.head()

# %%
df["growth_time"] = pd.to_numeric(df["growth_time"], errors="coerce")
df["regrowth_time"] = pd.to_numeric(df["regrowth_time"], errors="coerce")

# %%
# Calculate the numbers of harvest per crop.
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


# %%
df["sell_price_regular"] = pd.to_numeric(df["sell_price_regular"], errors="coerce")
df["seed_price_standard"] = pd.to_numeric(df["seed_price_standard"], errors="coerce")
df = df.drop("general_store_price", axis=1)
# %%
# Calculate the total profit of each harvest| Calcula o lucro total de cada plantação

def calculate_total_profit(row):

    return (row["sell_price_regular"] - row["seed_price_standard"]) * row["qt_harvest"]

    
df["total_profit"] = df.apply(calculate_total_profit, axis=1)
df
# %%

# Calculate the profit per day | Calcula o lucro diário

def calculate_profit_day(row):
    return row["total_profit"] / 28

df["profit_per_day"] = df.apply(calculate_profit_day, axis=1)
df

# %%

# Separate crops per seasons | Separa plantações por estação
spring_crops = df[df["spring"] == True].reset_index(drop=True)
summer_crops = df[df["summer"] == True].reset_index(drop=True)
fall_crops = df[df["fall"] == True].reset_index(drop=True)


# %%

# Sorting values by profit per day | Ordenando valores pelo lucro diário
spring_crops = spring_crops.sort_values(by="profit_per_day", ascending=False, ignore_index=True)
summer_crops = summer_crops.sort_values(by="profit_per_day", ascending=False, ignore_index=True)
fall_crops = fall_crops.sort_values(by="profit_per_day", ascending=False, ignore_index=True)

