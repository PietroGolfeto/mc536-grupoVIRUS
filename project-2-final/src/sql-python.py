import sqlite3

conn = sqlite3.connect('project-2-final/src/database.db')
cursor = conn.cursor()

import csv

# Code_Description
with open('/Users/sarab/OneDrive/Documentos/GitHub/mc536-grupoVIRUS/data/FCID_Code_Description.csv', newline='') as csvfile:
    # Criando um leitor CSV
    csv_reader = csv.reader(csvfile)
    
    header = next(csv_reader)  # Lê a primeira linha como cabeçalho
    
    cursor.execute(f"DROP TABLE IF EXISTS FCID_Code_Description")
    cursor.execute(f"CREATE TABLE FCID_Code_Description (cgn VARCHAR(2), FCID_Code VARCHAR(10), FCID_Desc VARCHAR(80))")

    csvfile.seek(0)
    next(csv_reader)  # Pular o cabeçalho

    # Inserir os dados do CSV na tabela do banco de dados
    insert_query = f"INSERT INTO FCID_Code_Description VALUES ({', '.join(['?' for _ in header])})"
    for row in csv_reader:
        cursor.execute(insert_query, row)

    cursor.execute("SELECT * FROM FCID_Code_Description LIMIT 5")

    rows = cursor.fetchall()

    if not rows:
        print("Nenhum dado encontrado.")
    for row in rows:
        print(row)


#CropGroup_Description
with open('/Users/sarab/OneDrive/Documentos/GitHub/mc536-grupoVIRUS/data/FCID_CropGroup_Description.csv', newline='') as csvfile:
    # Criando um leitor CSV
    csv_reader = csv.reader(csvfile)
    
    header = next(csv_reader)  # Lê a primeira linha como cabeçalho
    
    cursor.execute(f"DROP TABLE IF EXISTS FCID_CropGroup_Description")
    cursor.execute(f"CREATE TABLE FCID_CropGroup_Description (CGN VARCHAR(2), Crop_Group_Description VARCHAR(80))")

    csvfile.seek(0)
    next(csv_reader)  # Pular o cabeçalho

    # Inserir os dados do CSV na tabela do banco de dados
    insert_query = f"INSERT INTO FCID_CropGroup_Description VALUES ({', '.join(['?' for _ in header])})"
    for row in csv_reader:
        cursor.execute(insert_query, row)

    cursor.execute("SELECT * FROM FCID_CropGroup_Description LIMIT 5")

    rows = cursor.fetchall()

    if not rows:
        print("Nenhum dado encontrado.")
    for row in rows:
        print(row)


# Food_Code_Description
with open('/Users/sarab/OneDrive/Documentos/GitHub/mc536-grupoVIRUS/data/FCID_Food_Code_Description.csv', newline='') as csvfile:
    # Criando um leitor CSV
    csv_reader = csv.reader(csvfile)
    
    header = next(csv_reader)  # Lê a primeira linha como cabeçalho
    
    cursor.execute(f"DROP TABLE IF EXISTS FCID_Food_Code_Description")
    cursor.execute(f"CREATE TABLE FCID_Food_Code_Description (Food_Code VARCHAR(10),Food_Desc VARCHAR(80))")

    csvfile.seek(0)
    next(csv_reader)  # Pular o cabeçalho

    # Inserir os dados do CSV na tabela do banco de dados
    insert_query = f"INSERT INTO FCID_Food_Code_Description VALUES ({', '.join(['?' for _ in header])})"
    for row in csv_reader:
        cursor.execute(insert_query, row)

    cursor.execute("SELECT * FROM FCID_Food_Code_Description LIMIT 5")


#Recipes
with open('/Users/sarab/OneDrive/Documentos/GitHub/mc536-grupoVIRUS/data/FCID_Recipes.csv', newline='') as csvfile:
    # Criando um leitor CSV
    csv_reader = csv.reader(csvfile)
    
    header = next(csv_reader)  # Lê a primeira linha como cabeçalho
    
    cursor.execute(f"DROP TABLE IF EXISTS FCID_Recipes")
    cursor.execute(f"CREATE TABLE FCID_Recipes (Food_Code VARCHAR(10), Ingredient_Num TINYINT, FCID_Code VARCHAR(10))")

    csvfile.seek(0)
    next(csv_reader)  # Pular o cabeçalho

    # Inserir os dados do CSV na tabela do banco de dados
    insert_query = f"INSERT INTO FCID_Recipes VALUES ({', '.join(['?' for _ in header])})"
    for row in csv_reader:
        cursor.execute(insert_query, row)

    cursor.execute("SELECT * FROM FCID_Recipes LIMIT 5")

    rows = cursor.fetchall()

    if not rows:
        print("Nenhum dado encontrado.")
    for row in rows:
        print(row)


#Nutrient Values
with open('/Users/sarab/OneDrive/Documentos/GitHub/mc536-grupoVIRUS/data/FNDDS_Nutrient_Values.csv', newline='') as csvfile:
    # Criando um leitor CSV
    csv_reader = csv.reader(csvfile)
    
    header = next(csv_reader)  # Lê a primeira linha como cabeçalho
    
    cursor.execute(f"DROP TABLE IF EXISTS FNDDS_Nutrient_Values")
    cursor.execute(f"CREATE TABLE FNDDS_Nutrient_Values (Food_code VARCHAR(10), Main_food_description VARCHAR(50),Energy FLOAT,Protein FLOAT,Carbohydrate FLOAT,Sugars_total FLOAT,Fiber_total_dietary FLOAT,Total_Fat FLOAT,Cholesterol FLOAT,Vitamin_A_RAE FLOAT,Vitamin_B6 FLOAT,Vitamin_C FLOAT,Calcium FLOAT,Iron FLOAT,Potassium FLOAT,Sodium FLOAT,Caffeine FLOAT, Alcohol FLOAT)")

    csvfile.seek(0)
    next(csv_reader)  # Pular o cabeçalho

    # Inserir os dados do CSV na tabela do banco de dados
    insert_query = f"INSERT INTO FNDDS_Nutrient_Values VALUES ({', '.join(['?' for _ in header])})"
    for row in csv_reader:
        cursor.execute(insert_query, row)

    cursor.execute("SELECT * FROM FNDDS_Nutrient_Values LIMIT 5")

    rows = cursor.fetchall()

    if not rows:
        print("Nenhum dado encontrado.")
    for row in rows:
        print(row)


# Food_Code_Description
with open('/Users/sarab/OneDrive/Documentos/GitHub/mc536-grupoVIRUS/data/recommended-nutritional-values.csv', newline='') as csvfile:
    # Criando um leitor CSV
    csv_reader = csv.reader(csvfile)
    
    header = next(csv_reader)  # Lê a primeira linha como cabeçalho
    
    cursor.execute(f"DROP TABLE IF EXISTS Recommended_Nutritional_Values")
    cursor.execute(f"CREATE TABLE Recommended_Nutritional_Values (Energy FLOAT,Protein FLOAT,Carbohydrate FLOAT,Sugars_total FLOAT,Fiber_total_dietary FLOAT,Total_Fat FLOAT,Cholesterol FLOAT,Vitamin_A_RAE FLOAT,Vitamin_B6 FLOAT,Vitamin_C FLOAT,Calcium FLOAT,Iron FLOAT,Potassium FLOAT,Sodium FLOAT)")

    csvfile.seek(0)
    next(csv_reader)  # Pular o cabeçalho

    # Inserir os dados do CSV na tabela do banco de dados
    insert_query = f"INSERT INTO Recommended_Nutritional_Values VALUES ({', '.join(['?' for _ in header])})"
    for row in csv_reader:
        cursor.execute(insert_query, row)

    cursor.execute("SELECT * FROM Recommended_Nutritional_Values LIMIT 5")

    rows = cursor.fetchall()

    if not rows:
        print("Nenhum dado encontrado.")
    for row in rows:
        print(row)
