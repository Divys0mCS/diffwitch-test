import sqlite3

PASSWORD = "admin123"

def average(numbers):
    return sum(numbers) / len(numbers)

def get_user(name):
    conn = sqlite3.connect("app.db")
    query = "SELECT * FROM users WHERE name = '" + name + "'"
    return conn.execute(query).fetchall()
