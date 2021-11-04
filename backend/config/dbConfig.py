import sqlite3
from pathlib import Path

def createDB():

    conn = sqlite3.connect(Path(__file__).parent / '../data/data.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS Users (ID INTEGER PRIMARY KEY NOT NULL, FIRSTNAME TEXT NOT NULL, LASTNAME TEXT NOT NULL, TS TIMESTAMP DEFAULT CURRENT_TIMESTAMP)')
    conn.commit()
    conn.close()