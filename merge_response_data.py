import os
import pandas as pd
from glob import glob


zoom_paths = "data/Zoom/**/*.xlsx"

globs = glob(zoom_paths)

dfs = []

for path in globs:
    df = pd.read_excel(path)
    dfs.append(df)
    print(df)

zoom_df = pd.concat(dfs, axis=0)

zoom_df.to_csv("zoom.csv")


print("globbing face 2 face")

F2F_paths = "data/Face-to-Face/**/*.xlsx"

globs = glob(F2F_paths)

dfs = []

for path in globs:
    df = pd.read_excel(path)
    dfs.append(df)
    print(df)

F2F_data = pd.concat(dfs, axis=0)

F2F_data.to_csv("f2f.csv")
