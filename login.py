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
can chose options from a menu, including adding a new user
"""


def get_role():
    """
    function to return global variable role
    """
    return role


def get_user():
    """
    function to return global variable user
    """
    return user

def verify(username, password):
    """ 
    read in login information and verify
    """
    username = sanitize(username)
    password = sanitize(password)

    u_success = False
    global role
    global user

    cur.execute("SELECT username FROM info;")
    usernames = cur.fetchall()

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

        if file_username == username:
            u_success = True
        if u_success and authenticate(file_password, password):
            success = True
            cur.execute("SELECT role FROM info where username = '"+ username +"';")
            role = cur.fetchall()[0][0]
            user = username
            return True
        else:
            return False


def generate_password():
    """
    function to generate a secure password
    """
    # how long is the password going to be
    pass_len = random.randint(8,25)

    # one random number for every character in the password
    # source 3
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
    """
    function adds a new user with username and new raw password
    """
    if username == "":
        return (False, "")

    cur.execute("SELECT username FROM info;")
    usernames = cur.fetchall()
    u_list = []
    for u in usernames:
        u_list.append(u[0])
    
    if username in u_list:
        return (False, "")

    if raw_password == "":
        raw_password = generate_password()
        password = hash_pw(raw_password)

        cur.execute("SELECT Count(*) FROM info;")
        number = cur.fetchall()[0][0]
        
        data_to_insert = [(number), (username), (password), ("user")]
        cur.execute(f'INSERT INTO info (number, username, hashed_password, role) VALUES (?,?,?,?)', data_to_insert)
        conn.commit()
        return (True, raw_password)
    else:
        valid = False
        lower = False
        upper = False
        digit = False
        special = False
        while valid == False:
            for char in raw_password:
                if char.islower():
                    lower = True
                elif char.isupper():
                    upper = True
                elif char.isdigit():
                    digit = True
                else: 
                    # making sure passwords don't have characters that I will filter out later for XSS
                    if char != "%" and char != "'" and char != '"':
                        special = True
            if (len(raw_password) >= 8 and len(raw_password) <= 25) and lower and upper and digit and special:
                valid = True
                password = hash_pw(raw_password)
                cur.execute("SELECT Count(*) FROM info;")
                number = cur.fetchall()[0][0]
                data_to_insert = [(number), (username), (password), (user)]
                print(data_to_insert)
                cur.execute('INSERT INTO info (number, username, hashed_password, role) VALUES (?,?,?,?)', data_to_insert)                
                conn.commit()
                return (True, raw_password)
            else:
                return (False, "")


def sanitize(inputted):
    """
    sanitizes input
    """
    inputted = inputted.replace("'", "")
    inputted = inputted.replace('"', "")
    inputted = inputted.replace("%", "")

    return inputted
