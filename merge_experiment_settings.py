import pandas as pd

zoom_df = pd.read_csv("data/out/zoom.csv")
F2F_df = pd.read_csv("data/out/f2f.csv")
items_df = pd.read_csv("data/out/items.csv")


#
# Merge zoom and F2F
# -------------------------

zoom_df["setting"] = "zoom"
F2F_df["setting"] = "studio"

zoom_df.columns = zoom_df.columns.str.strip()
F2F_df.columns = F2F_df.columns.str.strip()

# Step 1: Identify common columns
common_columns = zoom_df.columns.intersection(F2F_df.columns)

# Step 2: Filter both DataFrames to only include common columns
df1_filtered = F2F_df[common_columns]
df2_filtered = zoom_df[common_columns]

# Step 3: Concatenate the filtered DataFrames
concatenated_df = pd.concat([df1_filtered, df2_filtered], ignore_index=True)

# ------ check that we've managed to extract all the questions correctly

# Convert the 'items' column of items_df to a set
items_set = set(items_df['items'])

# Convert the column names of concatenated_df to a set
column_names_set = set(concatenated_df.columns)

# Check if all items are in the column names
all_items_present = items_set.issubset(column_names_set)

# Print the result
print("Are all items in 'items_df' present in the column names of 'concatenated_df'? :", all_items_present)

concatenated_df.rename(columns={'poäng': 'points'}, inplace=True)

concatenated_df.to_csv("data/out/full_dataset.csv", index=False)
