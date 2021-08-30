import csv
import pandas as pd

def file_to_df(file_path): #read a file as a pandas dataframe
    df = pd.read_csv(file_path)

    return df  

def file_to_list(file_path): #read a file as a list of lists
    
    with open(file_path) as file:
        csv_reader = csv.reader(file, delimiter=',')
        list = []
        for row in csv_reader:
            list += [row]

    return list