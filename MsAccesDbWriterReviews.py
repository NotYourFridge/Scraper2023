import os
import pyodbc

cnxn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\MrFre\Documents\Kleuren.accdb;')
cursor = cnxn.cursor()

cursor.execute('CREATE TABLE Reviews (ID AUTOINCREMENT PRIMARY KEY, Name TEXT)')


file_path = os.path.join(os.getcwd(), 'resultsReviews', 'results.txt')
with open(file_path, 'r') as f:
 
    for line in f:
        Mood = line.strip()
        cursor.execute('INSERT INTO Reviews (Name) VALUES (?)', Mood)


cnxn.commit()
cnxn.close()
