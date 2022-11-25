import sqlite3

conn = sqlite3.connect("login_info.db", check_same_thread=False)
cur = conn.cursor()
cur.execute("SELECT username FROM info;")
usernames = cur.fetchall()

for u in usernames:
    print(u[0])

