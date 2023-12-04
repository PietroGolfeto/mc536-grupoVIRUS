import sqlite3
import csv

conn = sqlite3.connect('project-2-final/src/database.db')
cursor = conn.cursor()

#testando query
cursor.execute("""SELECT * FROM FCID_Food_Code_Description R, FNDDS_Nutrient_Values N 
            WHERE R.Food_Code = N.Food_code LIMIT 5""")
rows = cursor.fetchall()

column_names = [description[0] for description in cursor.description]
print(column_names)
for row in rows:
    print(row)

# Obter os nomes das colunas
column_names = (description[0] for description in cursor.description)

# Nome do arquivo CSV de saída
csv_file = 'project-2-final/src/output.csv'

# Escrever os resultados no arquivo CSV
with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    # Escrever o cabeçalho
    csv_writer.writerow(column_names)
    # Escrever os dados
    csv_writer.writerows(rows)

