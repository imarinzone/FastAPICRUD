import sqlite3
def SQLite3Connect(PORT):
    con = sqlite3.connect(PORT)
    cur = con.cursor()
    return con, cur