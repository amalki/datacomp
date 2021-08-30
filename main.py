import functions

#informations about sql server and db
dsn = 'sqlserverdatasource'
user = 'SA'
password = 'Adam2020'
database = 'pocAdamAmmar'
table1 = 'Inventory'
table2 = 'Inventory'
#reading source and target
source_file_path = 'input/source/ford_escort.csv'
target_file_path = 'input/target/ford_escort.csv'


source_df = functions.csv_to_df(source_file_path)
target_df = functions.csv_to_df(target_file_path)

#comparing source with target
row_count_source = source_df.shape[0]
row_count_target = target_df.shape[0]

print('Does the source and target have the same number of rows?\n' + str(row_count_target==row_count_source))

sql_source = functions.sqls_table_to_list(dsn,user,password,database,table1)
sql_target = functions.sqls_table_to_list(dsn,user,password,database,table2)

#comparing source with target for SQL Server
sql_server_row_count_source=len(sql_source)
sql_server_row_count_target=len(sql_target)

print('Does the source and target have the same number of rows?\n' + str(sql_server_row_count_target==sql_server_row_count_source))

