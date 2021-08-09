import csv

def file_to_list(file_path):
    
    with open(file_path) as file:
        csv_reader = csv.reader(file, delimiter=',')
        list = []
        for row in csv_reader:
            list += [row]

    return list