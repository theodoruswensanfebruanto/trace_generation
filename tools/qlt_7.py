from io import StringIO
import pandas as pd

file_name = 'qlt.csv'
df = pd.read_csv(file_name)
number_of_characters = 7
start_point = 18 - number_of_characters
df['key'] = df['key'].apply(lambda x: x[start_point:start_point + number_of_characters])
df['key'] = df['key'].apply(lambda x: int(x, 16))
df.to_csv(file_name, index=False)