import pandas as pd

# Replace 'your_excel_file.xlsx' with the actual file name
excel_file_path = '2019-2020 FNDDS At A Glance - Portions and Weights.xlsx'

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file_path)

# Replace 'output_file.csv' with the desired CSV file name
csv_file_path = 'FNDDS_Portions_Weights.csv'

# Write the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)

print(f"Conversion successful. CSV file saved at {csv_file_path}")