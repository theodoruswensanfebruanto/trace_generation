import csv

operation_mapping = {'Read': '0', 'Append': '1', 'GetFileSize': '2', 'Close': '3', 'NewWritableFile': '4', 'PositionedAppend': '5', 'Truncate': '6', 'Prefetch': '7'}
io_mapping = {'OK': '1'}
type_mapping = {'log': '0', 'sst': '1', 'MANIFEST': '2'}
input_file = 'iolt.csv'
output_file = 'iolt.csv'

with open(input_file, 'r', newline='') as csvfile, open(output_file, 'w', newline='') as outfile:
    reader = csv.DictReader(csvfile)
    fieldnames = ['access_timestamp_in_microseconds', 'file_name', 'file_type', 'file_operation', 'latency', 'io_status', 'file_size', 'length', 'offset']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in reader:
        row['file_operation'] = operation_mapping.get(row['file_operation'], row['file_operation'])
        row['io_status'] = io_mapping.get(row['io_status'], row['io_status'])
        row['file_type'] = row['file_name'].split('.')[-1]
        row['file_type'] = type_mapping.get(row['file_type'], row['file_type'])
        row['file_name'] = row['file_name'].split('.')[0].lstrip('0')
        row = {key: row[key] for key in fieldnames}
        writer.writerow(row)