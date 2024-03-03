import os
import pandas as pd
from glob import glob


# Zoom data
# -----------------------------
zoom_paths = "data/Zoom/**/*.xlsx"

globs = glob(zoom_paths)

dfs = []

for path in globs:
    df = pd.read_excel(path)
    dfs.append(df)
    print(df)

zoom_df = pd.concat(dfs, axis=0)
zoom_df.rename(columns={'Identity Code': 'id'}, inplace=True)
# Set all column names to lowercase
zoom_df.columns = [col.lower() for col in zoom_df.columns]
zoom_df.rename(columns={'highest education level': 'education'}, inplace=True)

# Select the range of columns you want to rename (27 to 48 in this case)
columns_to_rename = zoom_df.columns[27:48]

# Update the column names in the original DataFrame by prepending numbers
zoom_df.rename(columns={col: f"{i+1}. {col}" for i, col in enumerate(columns_to_rename)}, inplace=True)

# merge zoom df with points which are in a separate file
zoom_points_df = pd.read_csv("data/out/points_zoom.csv")
merged_zoom_df = pd.merge(zoom_df, zoom_points_df, on='id', how='left')


merged_zoom_df["id"] = "Z" + merged_zoom_df["id"]
merged_zoom_df.to_csv("data/out/zoom.csv", index=False)


# Face 2 Face data
# --------------------------------
print("globbing face 2 face")

F2F_paths = "data/Face-to-Face/**/*.xlsx"

globs = glob(F2F_paths)

dfs = []

for path in globs:
    df = pd.read_excel(path)
    dfs.append(df)
    print(df)

F2F_df = pd.concat(dfs, axis=0)
F2F_df.columns = [col.lower() for col in F2F_df.columns]

# Select the range of columns you want to rename (27 to 48 in this case)
columns_to_rename = F2F_df.columns[28:49]
# Update the column names in the original DataFrame by prepending numbers
F2F_df.rename(columns={col: f"{i+1}. {col}" for i, col in enumerate(columns_to_rename)}, inplace=True)


F2F_df["id"] = "F" + F2F_df["id"]

F2F_df.to_csv("data/out/f2f.csv", index=False)