# %%
import pandas as pd
# %%
df = pd.read_csv("../data/crops_data.csv", sep=",")
df_summer = pd.read_csv("../data/summer_crops_info.csv", sep=",")
df_fall = pd.read_csv("../data/fall_crop_info.csv", sep=",")
df_spring = pd.read_csv("../data/spring_crops_info.csv", sep=",")
df_winter = pd.read_csv("../data/winter_crop_info.csv", sep=",")

# %%
df_seasons = pd.concat([df_summer, df_fall, df_spring, df_winter], ignore_index=True)
df_seasons.rename(columns= {"crop_name": "name"}, inplace=True)
df_seasons.drop(columns=["description", "season"], inplace=True)


# %%
df = (df.merge(df_seasons, on="name", how="left")
               .drop_duplicates(keep="last", subset=["name"], ignore_index=True))
df
# %%

df.to_csv("processed_data.csv", index=False)