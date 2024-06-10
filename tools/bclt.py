import pandas as pd

trace_file_name = 'bclt.csv'
df = pd.read_csv(trace_file_name)
df = df.drop('column_family_name', axis=1)
df.to_csv(trace_file_name, index=False)