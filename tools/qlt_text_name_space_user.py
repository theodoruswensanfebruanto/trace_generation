import pandas as pd
import re

file_name = 'qlt.csv'
df = pd.read_csv(file_name)

def hex_to_string(hex_string):
    modified_hex_string = hex_string[2:]
    byte_data = bytes.fromhex(modified_hex_string)
    result_string = byte_data.decode('latin')
    match = re.search(r'\d+', result_string)
    if match:
        user_number = match.group(0)
    else:
        user_number = -1
    return user_number

df['key'] = df['key'].apply(hex_to_string)
df.to_csv(file_name, index=False)