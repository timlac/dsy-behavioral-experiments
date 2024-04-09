import pandas as pd

df = pd.read_excel("../data/deception/Questionnaire Data/decept_complete_quest_data.xlsx")

# Printing column names along with indices
for index, column_name in enumerate(df.columns):
    print(f"Column index: {index}, Column name: {column_name}")

participant_id = df.iloc[:, 0]
i_panas_sf = df.iloc[:, 1:11]
interaction = df.iloc[:, 11:14]
appreciation = df.iloc[:, 14:18]
bhi = df.iloc[:, 18:42]
s_pec = df.iloc[:, 42:61]
ecr_sr = df.iloc[:, 61:]

# Get all unique entries
unique_entries = i_panas_sf.values.flatten()  # Flatten the DataFrame to a 1D array
unique_entries = pd.unique(unique_entries)  # Get unique values
print(unique_entries)

# Mapping from word scale to numerical scale
mapping = {
    'Inte alls': 1,
    'Lite': 2,
    'I någon mån': 3,
    'Ganska bra': 4,
    'Väldigt mycket': 5
}

i_panas_sf_converted = i_panas_sf.replace(mapping)


