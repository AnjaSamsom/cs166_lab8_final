from hash import *
import sqlite3
import pandas as pd
from datetime import * 
import random
conn = sqlite3.connect("login_info.db")
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
""" def main():
    role, success = verify()

    if success == True:
        choice = menu()
        enter(choice, role)

    # exits if login does not match
    else:
        print("Incorrect login, quitting...") """

# read in login information from csv and verify
def verify(username, password):
    role = ""
    success = False
    u_success = False

    # user input
    #username = input("username: ")
    #password = input("password: ")

    # use hash_pw method to get the hash of the password
    hashed_pw = hash_pw(password)

    cur.execute("SELECT username FROM info where username = '"+ username +"';")
    file_username = cur.fetchall()[0][0]

    cur.execute("SELECT hashed_password FROM info where username = '"+ username +"';")
    file_password = cur.fetchall()[0][0]

    cur.execute("SELECT role FROM info where username = '"+ username +"';")
    role = cur.fetchall()[0][0]

    print(file_username, username)
    if file_username == username:
        u_success = True
    if u_success and authenticate(file_password, password):
        success = True
        print("login successful")
    return (str(role).strip(), success)

def generate_password():
    # how long is the password going to be
    pass_len = random.randint(8,25)

    # one random number for every character in the password
    password_list = [random.randint(-1000,1000) for i in range (0,pass_len)]

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
    return password

def add_user():
    username = input("username: ")
    print("Add a password of type generate for a generated secure pasword")
    raw_password = input("password (8-25 characters, at least one uppercase, one lowercase, one number, and one special character): ")
    if raw_password == "generate":
        raw_password = generate_password()
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
    cur.execute("SELECT Count(*) FROM info;")
    number = cur.fetchall()[0][0]
    cur.execute(f'INSERT INTO info (number, username, hashed_password, role) VALUES ({number}, "{username}", "{password}", "user");')
    conn.commit()

# print menu
def menu():
    print("Options:")
    print("1 - order from manufacturer")
    print("2 - enter time")
    print("3 - schedule repair")
    print("4 - charge customer")
    print("5 - add new user")
    print("6 - display menu again")
    
    return input("Please enter an option: ")

# allows user to enter options
def enter(choice, role):
    choice = int(choice)
    if choice == 1:
        # allow access
        if role == "owner":
            print("Access to order from manufacturer granted")
        # do not allow access and let user select again
        else:
            print("You do not have access to this feature")
            choice = menu()
            enter(choice, role)
    if choice == 2:
        if role == "owner" or role == "employee":
            print("Access to enter time granted")
        else:
            print("You do not have access to this feature")
            choice = menu()
            enter(choice, role)
    if choice == 3:
        if role == "owner" or role == "employee" or role == "customer":
            print("Access to schedule repair granted")
        else:
            print("You do not have access to this feature")
            choice = menu()
            enter(choice, role)
    if choice == 4:
        if role == "owner" or role == "employee":
            print("Access to charge customer granted")
        else:
            print("You do not have access to this feature")
            choice = menu()
            enter(choice, role)
    if choice == 5:
        if role == "owner":
            print("Access to add user granted")
            add_user(cur, conn)
        else:
            print("You do not have access to this feature add a user")
            choice = menu()
            enter(choice, role, cur, conn)
    # redisplay menu
    if choice == 6:
        choice = menu()
        enter(choice, role)

#main()