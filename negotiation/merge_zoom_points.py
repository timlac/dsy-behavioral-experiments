import pandas as pd


# Convert each string in the list to an integer, handling errors gracefully
def convert_to_int(item):
    try:
        return int(item)
    except ValueError:
        # Return None or 0 if the conversion fails, or handle the error as needed
        return None


path = "../data/negotiation/Points_Zoom_dyads.xlsx"

df = pd.read_excel(path, header=None)

df.rename(columns={0: 'id',
                   1: 'point_str_array'}, inplace=True)

# Exclude rows where 'point_str_array' is "Data Missing"
df = df.loc[df['point_str_array'] != "Data Missing"]

df["point_array"] = df["point_str_array"].str.split(",")

# Convert each string in the list to an integer
df["point_array_int"] = df["point_array"].apply(lambda x: [int(item) for item in x])

# Sum the integers in the list
df["poäng"] = df["point_array_int"].apply(lambda x: sum(x))

df = df[["id", "poäng"]]

df['id'] = df['id'].str.strip()

print(df["id"])

df.to_csv("data/out/points_zoom.csv", index=False)



#



# # Convert each string in the list to an integer
# df["point_array_int"] = df["point_array"].apply(lambda x: [convert_to_int(item) for item in x])
#
# # Sum the integers in the list
# df["points"] = df["point_array_int"].apply(lambda x: sum(item for item in x if item is not None))


