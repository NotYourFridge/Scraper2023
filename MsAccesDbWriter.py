import os
import pyodbc

cnxn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\MrFre\Documents\Kleuren.accdb;')
cursor = cnxn.cursor()

cursor.execute('CREATE TABLE Colors (ID AUTOINCREMENT PRIMARY KEY, Name TEXT)')


file_path = os.path.join(os.getcwd(), 'kleuren', 'rgb_color_names.txt')
with open(file_path, 'r') as f:
 
    for line in f:
        color_name = line.strip()
        cursor.execute('INSERT INTO Colors (Name) VALUES (?)', color_name)


cnxn.commit()
cnxn.close()


