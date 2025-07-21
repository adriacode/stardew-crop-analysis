# %%
import pandas as pd

# %%
df = pd.read_csv("../data/crops_data.csv", sep=",")
df_summer = pd.read_csv("../data/summer_crops_info.csv", sep=",")
df_fall = pd.read_csv("../data/fall_crop_info.csv", sep=",")
df_spring = pd.read_csv("../data/spring_crops_info.csv", sep=",")
df_winter = pd.read_csv("../data/winter_crop_info.csv", sep=",")


# %%
df_estacoes = pd.concat([df_summer, df_fall, df_spring, df_winter], ignore_index=True)
df_estacoes.rename(columns= {"crop_name": "name"}, inplace=True)
df_estacoes.drop(columns=["description", "season"], inplace=True)
df_estacoes

regrowth_times = {
    "Strawberry": 4,
    "Blueberry": 4,
    "Corn": 4,
    "Hot Pepper": 3,
    "Tomato": 4,
    "Coffee Bean": 2,
    "Hops": 1,
    "Eggplant": 5,
    "Cranberries": 5,
    "Artichoke": 6,
    "Amaranth": 5
}


df_estacoes["regrowth_time"] = df["name"].map(regrowth_times)

# %%
df_merged = (df.merge(df_estacoes, on="name", how="left")
               .drop_duplicates(keep="last", subset=["name"], ignore_index=True))

df_merged.to_csv("processed_data.csv", index=False)