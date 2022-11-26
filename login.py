from hash import *
import sqlite3
import pandas as pd
from datetime import * 
import random
conn = sqlite3.connect("login_info.db", check_same_thread=False)
cur = conn.cursor()


"""
Lab 8 Final
Anja Samsom
CS 166
this program is a computer repair company's computer.
owner can access everything, employees and customers
have limited access
the user types in a username and password and then
can chose options from a menu
"""


def get_role():
    return role

# read in login information and verify
def verify(username, password):
    u_success = False
    global role

    cur.execute("SELECT username FROM info;")
    usernames = cur.fetchall()

    print(usernames)
    print(username)


    u_list = []
    for u in usernames:
        u_list.append(u[0])

    print("made new list")

    if username in u_list:
        print("in usernames: " + username)
        cur.execute("SELECT username FROM info where username = '"+ username +"';")
        file_username = cur.fetchall()[0][0]

        cur.execute("SELECT hashed_password FROM info where username = '"+ username +"';")
        file_password = cur.fetchall()[0][0]
        print(file_password)

        if file_username == username:
            u_success = True
        if u_success and authenticate(file_password, password):
            print("matched")
            success = True
            cur.execute("SELECT role FROM info where username = '"+ username +"';")
            role = cur.fetchall()[0][0]
            return True
        else:
            return False

def generate_password():
    # how long is the password going to be
    pass_len = random.randint(8,25)

    # one random number for every character in the password
    password_list = [random.randint(-1000,1000) for i in range (0,pass_len)]

    special = "!@#$^&*()_+-=<>?,./:;[]|"
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
    return password

def add_user(username, raw_password):
    if raw_password == "":
        raw_password = generate_password()
        password = hash_pw(raw_password)
        cur.execute("SELECT Count(*) FROM info;")
        number = cur.fetchall()[0][0]
        cur.execute(f'INSERT INTO info (number, username, hashed_password, role) VALUES ({number}, "{username}", "{password}", "user");')
        conn.commit()
        return True
    else:
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
                    # making sure passwords don't have characters that I will filter out later for XSS
                    if char != "%" and char != "'" and char != '"':
                        special = True
            if (len(raw_password) >= 8 and len(raw_password) <= 25) and lower and upper and number and special:
                valid = True
                password = hash_pw(raw_password)
                cur.execute("SELECT Count(*) FROM info;")
                number = cur.fetchall()[0][0]
                cur.execute(f'INSERT INTO info (number, username, hashed_password, role) VALUES ({number}, "{username}", "{password}", "user");')
                conn.commit()
                return True
            else:
                return False


def sanitize(inputted):
    inputted = inputted.replace("'", "")
    inputted = inputted.replace('"', "")
    inputted = inputted.replace("%", "")

    return inputted
