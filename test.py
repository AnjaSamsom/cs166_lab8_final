from hash import *
import sqlite3
import pandas as pd
import datetime
import random

# how long is the password going to be
pass_len = random.randint(8,25)

# one random number for every character in the password
password_list = [random.randint(-1000,1000) for i in range (0,pass_len)]
print(password_list)

special = "!@#$%^&*()_+-=<>?,./':;[]|"
lower = "qwertyuiopasdfghjklzxcvbnm"
upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
number = "1234567890"
password = ""

for num in password_list:
    if num >= 0:
        # make positive numbers letters, even are uppercase, odd are lowercase
        index = random.randint(0,25)
        if num%2 == 0:
            # uppercase
            password += upper[index]
        else:
            # lowercase
            password += lower[index]
        
    else:
        # make negative numbers numbers and special character, even are special characters, odd are numbers
        if num%2 == 0:
            # special character
            index = random.randint(0,len(special)-1)
            password += special[index]
        else:
            # number
            index = random.randint(0,len(number)-1)
            password += number[index]
print(password)






