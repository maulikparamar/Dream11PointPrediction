import pandas as pd
# data = pd.read_csv("./IPL_Ball_by_Ball_2008_2022.csv")
data = pd.read_csv("./IPL_Matches_2008_2022.csv")
columns = list(data.columns)
# print(columns)
# print(data.isnull().mean())
columns.remove('City')
columns.remove('SuperOver')
columns.remove('TossDecision')
columns.remove('method')
columns.remove('Umpire1')
columns.remove('Umpire2')

# for i in columns:        # If you have columns of strings, check for trailing whitespaces
#     data[i] = data[i].str.strip()

print(data.isnull().sum())
# print(data.describe())
# print(data['Player_of_Match'].isnull().to_list())
# rows = []
# for i in range(len(data)):
#     if data['Player_of_Match'].iloc[i] == "":
#         rows.append(i)

# print(rows)