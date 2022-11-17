from hash import *
import sqlite3
import pandas as pd
from datetime import date 
import re     
raw_password = input("password (8-25 characters, at least one uppercase, one lowercase, one number, and one special character): ")
valid = False
lower = False
upper = False
number = False
special = False
while valid == False:
    for char in raw_password:
        if char.islower():
            lower = True
        elif char.isupper():
            upper = True
        elif char.isdigit():
            number = True
        else: 
            special = True
    if (len(raw_password) >= 8 and len(raw_password) <= 25) and lower and upper and number and special:
        valid = True
    else:
        raw_password = input("enter a valid password (8-25 characters, at least one uppercase, one lowercase, one number, and one special character): ")
password = hash_pw(raw_password)