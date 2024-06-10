import pandas as pd
from io import StringIO

df = pd.read_csv('qlt.txt', sep=' ', header=None, names=['key', 'type_id', 'column_family_id', 'value_size', 'access_timestamp_in_microseconds'])
df = df[['access_timestamp_in_microseconds', 'key', 'type_id', 'column_family_id', 'value_size']]
corrected_csv_file_path = 'qlt.csv'
df.to_csv(corrected_csv_file_path, index=False)