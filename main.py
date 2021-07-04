import pandas as pd
import numpy as np

filepath = "datafile.xlsx"
data = pd.read_excel(filepath, header=0, index_col=None, usecols="A:J")

# print(data.head(10))

col_names = list(data.columns[1:])
print(col_names)

for col in col_names:
    data[col] = data[col] == 1.0
    data[col] = data[col].astype(int)
    data[col] = data[col].astype(str)
    
data['Pattern'] = data[col_names].agg('-'.join, axis=1)
    
print(data.head())
print(data.dtypes)

uniquePatterns = data["Pattern"].unique()

for pat in uniquePatterns:
    rows = data.loc[data["Pattern"] == pat]
    coy = list(rows["Dummy Code"])
    filename = "./output/output" + pat + ".csv"
    with open(filename, 'w') as file:
        rows.to_csv(file, index=None)