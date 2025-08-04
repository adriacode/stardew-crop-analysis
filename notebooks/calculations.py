# %%

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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


# %%

# 5 Most Profitable Crops (Spring) | 5 plantações mais lucrativas (Primavera)
spring_colors = ["#FFB7C5", "#C1E1C1", "#F7DC6F", "#AED6F1", "#E8DAEF"]

sns.barplot(data=spring_crops.head(5), x="name", y="profit_per_day", palette=spring_colors, hue="name", legend=False)
plt.ylabel("Profit per day / Lucro por dia")
plt.title("Profitable Crops (Spring) / Plantações mais lucrativas (Primavera)")
plt.xlabel("Name / Nome")
plt.show()

# 5 Most Profitable Crops (Summer) | 5 plantações mais lucrativas (Verão)
summer_colors = ["#FF6F61", "#FFD700", "#FFA07A", "#40E0D0", "#FF8C00"]
sns.barplot(summer_crops.head(5), x="name", y="profit_per_day", palette=summer_colors, hue="name", legend=False)
plt.ylabel("Profit per day / Lucro por dia")
plt.title("Profitable Crops (Summer) / Plantações mais lucrativas (Verão)")
plt.xlabel("Name / Nome")
plt.show()

# 5 Most Profitable Crops (Fall) | 5 plantações mais lucrativas (Outono)
fall_colors = ["#8B4513", "#D2691E", "#FF8C00", "#F4A460", "#A0522D"]
sns.barplot(fall_crops.head(5), x="name", y="profit_per_day", palette=fall_colors, hue="name", legend=False)
plt.ylabel("Profit per day / Lucro por dia")
plt.title("Profitable Crops (Fall) / Plantações mais lucrativas (Outono)")
plt.xlabel("Name / Nome")
plt.show()