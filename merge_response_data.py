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

zoom_points_df = pd.read_csv("data/out/points_zoom.csv")

merged_zoom_df = pd.merge(zoom_df, zoom_points_df, on='id', how='left')

merged_zoom_df["id"] = "Z" + merged_zoom_df["id"]

merged_zoom_df.to_csv("data/out/zoom.csv", index=False)

# zoom_df["id"] = "Z" + zoom_df["id"]
# zoom_df.to_csv("data/out/zoom.csv", index=False)


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

F2F_df["id"] = "F" + F2F_df["id"]

F2F_df.to_csv("data/out/f2f.csv", index=False)

# Merge zoom and F2F
# -------------------------

