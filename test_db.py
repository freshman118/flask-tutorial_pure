import MySQLdb

db = MySQLdb.connect("localhost", "root", "123456", "blog")
cursor = db.cursor()
# sql = "SELECT * FROM user WHERE USERNAME = {}".format(jackc)
# cursor.execute('SELECT * FROM user WHERE username = ?', (username,))
data = cursor.fetchall()
for user in data:
    print(f"id: {user[0]}")
    print(f"name: {user[1]}")
    print(f"password: {user[2]}")
db.close()
