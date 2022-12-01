import sqlite3
from login import *
from hash import *

conn = sqlite3.connect("login_info.db", check_same_thread=False)
cur = conn.cursor()


