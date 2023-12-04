import sqlite3

conn = sqlite3.connect('project-2-final/src/database.db')
cursor = conn.cursor()

#testando query
cursor.execute("SELECT * FROM FCID_Code_Description LIMIT 5")
rows = cursor.fetchall()

for row in rows:
     print(row)
