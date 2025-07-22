# %%
import pandas as pd
# %%

df = pd.read_csv("../data/crops_data.csv", sep=",")
df_summer = pd.read_csv("../data/summer_crops_info.csv", sep=",")
df_fall = pd.read_csv("../data/fall_crop_info.csv", sep=",")
df_spring = pd.read_csv("../data/spring_crops_info.csv", sep=",")
df_winter = pd.read_csv("../data/winter_crop_info.csv", sep=",")

# %%

# Concating datasets of each season | Concatenando dados de cada estação
df_seasons = pd.concat([df_summer, df_fall, df_spring, df_winter], ignore_index=True)
df_seasons.rename(columns= {"crop_name": "name"}, inplace=True)
df_seasons.drop(columns=["description", "season"], inplace=True)


# %%

# Merging dataframe of seasons with the main dataframe | Mesclando o dataframa das estações com o dataframe principal
df = (df.merge(df_seasons, on="name", how="left")
               .drop_duplicates(keep="last", subset=["name"], ignore_index=True))
df
# %%

# Saving dataframe as csv | Salvando o dataframe como csv
df.to_csv("processed_data.csv", index=False)