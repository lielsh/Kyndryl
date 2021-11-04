import sqlite3
from pathlib import Path

def openDB():
    return sqlite3.connect(Path(__file__).parent / '../data/data.db')

def getUsers():
    
    conn = openDB()
    c = conn.cursor()
    data = {}

    try:
        c.execute('SELECT * FROM Users ORDER BY TS ASC')
        data['users'] = c.fetchall()

    except sqlite3.Error as er:
        data['users'] = []
        print(er)

    conn.commit()
    conn.close()

    return data

def addUser(id, first, last):

    conn = openDB()
    c = conn.cursor()
    message = {}

    try:
        c.execute("INSERT INTO Users (ID, FIRSTNAME, LASTNAME) VALUES (?, ?, ?)", (id, first, last))
        message = { 'message': 'The user has been successfully added', 'Error': False }
    
    except sqlite3.Error as er:
        message = { 'message': str(er), 'Error': True }
        print(er)

    conn.commit()
    conn.close()

    return message