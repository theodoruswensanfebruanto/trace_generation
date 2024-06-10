import pandas as pd

df = pd.read_csv('iolt.csv')
numeric_col = pd.to_numeric(df['file_name'], errors='coerce')
non_numerical_values = df['file_name'][numeric_col.isna()]

print(non_numerical_values)