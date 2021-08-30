import csv
import pandas as pd
import pyodbc

def sqls_table_to_list(dsn,user,password,database,table):
    con_string = 'DSN=%s;UID=%s;PWD=%s;DATABASE=%s;' % (dsn, user, password, database)
    cnxn = pyodbc.connect(con_string)
    cursor = cnxn.cursor()
    cursor.execute('SELECT * FROM '+table)
    list = []
    for row in cursor:
        list += [row]
    return list
    
def csv_to_df(file_path): #read a file as a pandas dataframe
    df = pd.read_csv(file_path)

    return df  

def csv_to_list(file_path): #read a file as a list of lists
    
    with open(file_path) as file:
        csv_reader = csv.reader(file, delimiter=',')
        list = []
        for row in csv_reader:
            list += [row]

    return list