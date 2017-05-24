import csv

def csv_to_dict(input_file):
    reader = csv.DictReader(open(input_file, 'r'))
    data = dict.fromkeys(reader.fieldnames)
    
    for i_iter, row in enumerate(reader):
        for key in data.keys():
            if i_iter <= 0:
                data[key] = [row[key]]
            else:
                data[key].append(row[key])
    return data
