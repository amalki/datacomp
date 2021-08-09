import functions

#reading source and target
source_file_path = 'input/source/ford_escort.csv'
target_file_path = 'input/target/ford_escort.csv'


source_list = functions.file_to_list(source_file_path)
target_list = functions.file_to_list(source_file_path)

#comparing source with target
row_count_source = len(source_list)
row_count_target = len(target_list)

print('Does the source and target has the same number of rows?\n' + str(row_count_target==row_count_source))



