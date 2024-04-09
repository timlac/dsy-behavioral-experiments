import pandas as pd
from glob import glob

zoom_df = pd.read_csv("../data/out/negotiation/zoom.csv")

empathy_questions = zoom_df.iloc[:, 7: 27]
experiment_questions = zoom_df.iloc[:, 27: 48]

codes = ["empathy_" + str(i + 1) for i in range(empathy_questions.shape[1])]
codes.extend(["experiment_" + str(i + 1) for i in range(experiment_questions.shape[1])])


df_1 = pd.DataFrame({"codes": codes,
                   'items': list(empathy_questions.columns) + list(experiment_questions.columns)})


F2F_df = pd.read_csv("../data/out/negotiation/f2f.csv")

F2F_df.columns = [col.lower() for col in F2F_df.columns]
F2F_df.columns = F2F_df.columns.str.strip()


empathy_questions = F2F_df.iloc[:, 6: 26]
experiment_questions = F2F_df.iloc[:, 28: 49]

codes = ["empathy_" + str(i + 1) for i in range(empathy_questions.shape[1])]
codes.extend(["experiment_" + str(i + 1) for i in range(experiment_questions.shape[1])])


df_2 = pd.DataFrame({"codes": codes,
                   'items': list(empathy_questions.columns) + list(experiment_questions.columns)})


unique_items = df_2[~df_2['items'].isin(df_1['items'])]

# Display the unique items
print(unique_items)

df_1.to_csv("data/out/items.csv", index=False)