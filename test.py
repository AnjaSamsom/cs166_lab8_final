import sqlite3
from login import *
from hash import *

conn = sqlite3.connect("login_info.db", check_same_thread=False)
cur = conn.cursor()

n = add_user("anja", "(&(^TGJVJvhjv67")

print(n[0])
print(n[1])
