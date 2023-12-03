import csv

# Replace 'input_file.csv' and 'output_file.csv' with your actual file paths
input_file_path = 'data\FCID_Recipes.csv'
output_file_path = 'data\FCID_Recipes2.csv'

# Read the CSV file and filter rows where Mod_Code is not zero
with open(input_file_path, 'r') as input_file, open(output_file_path, 'w', newline='') as output_file:
    csv_reader = csv.reader(input_file)
    header = next(csv_reader)  # Read the header

    # Find the index of the Mod_Code column
    mod_code_index = header.index('Mod_Code')

    # Write the header to the output file
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(header)

    # Filter rows and write to the output file
    for row in csv_reader:
        if int(row[mod_code_index]) == 0:
            csv_writer.writerow(row)
