import functions

#reading source and target
source_file_path = 'input/source/ford_escort.csv'
target_file_path = 'input/target/ford_escort.csv'


source_df = functions.file_to_df(source_file_path)
target_df = functions.file_to_df(target_file_path)

#comparing source with target
row_count_source = source_df.shape[0]
row_count_target = target_df.shape[0]

print('Does the source and target have the same number of rows?\n' + str(row_count_target==row_count_source))



