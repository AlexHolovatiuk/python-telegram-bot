import sqlite3

con = sqlite3.connect('test1.db')
cur = con.cursor()

# cur.execute("CREATE TABLE user(name, year, title);")
# cur.execute('''CREATE TABLE user_1(
#         id INTEGER PRIMARY KEY,
#         name TEXT DEFAULT 'Невідомий',
#         year INTEGER DEFAULT 0,
#         title TEXT NOT NULL
#     );''')
#
#
# con.commit()

cur.execute("INSERT INTO user_1 (name, year, title) VALUES ('Едік', 2000, 'Дідусь') ")
con.commit()

con.close()