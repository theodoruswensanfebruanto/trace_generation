import csv

input_file = 'iolt.txt'
output_file = 'iolt_raw.csv'

with open(input_file, 'r') as f_in, open(output_file, 'w', newline='') as f_out:
    csv_writer = csv.writer(f_out)
    csv_writer.writerow(['access_timestamp_in_microseconds', 'file_name', 'file_operation', 'latency', 'io_status', 'file_size', 'length', 'offset'])
    for _ in range(3):
        next(f_in)
    for line in f_in:
        parts = line.strip().split(',')
        access_time = parts[0].split(':')[1].strip()
        file_name = parts[1].split(':')[1].strip()
        file_operation = parts[2].split(':')[1].strip()
        latency = parts[3].split(':')[1].strip()
        io_status = parts[4].split(':')[1].strip()
        length = '-1'
        offset = '-1'
        file_size = '-1'
        for part in parts:
            if 'File Size' in part:
                file_size = part.split(':')[1].strip()
                break
            if 'Length' in part:
                length = part.split(':')[1].strip()
                break
            if 'Offset' in part:
                offset = part.split(':')[1].strip()
                break 
        csv_writer.writerow([access_time, file_name, file_operation, latency, io_status, file_size, length, offset])