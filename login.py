from hash import *
import sqlite3
import pandas as pd
from datetime import date  

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
def main():
    conn = sqlite3.connect("login_info.db")
    cur = conn.cursor()
    role, success = verify(cur)

    if success == True:
        choice = menu()
        enter(choice, role)

    # exits if login does not match
    else:
        print("Incorrect login, quitting...")

# read in login information from csv and verify
def verify(cur):
    role = ""
    success = False
    u_success = False

    # user input
    username = input("username: ")
    password = input("password: ")

    # use hash_pw method to get the hash of the password
    hashed_pw = hash_pw(password)

    # get list from read_file
    info = read_file("info.csv")

    cur.execute("SELECT username FROM info where username = '"+ username +"';")
    file_username = cur.fetchall()[0][0]

    cur.execute("SELECT hashed_password FROM info where username = '"+ username +"';")
    file_password = cur.fetchall()[0][0]

    print(file_username, username)
    if file_username == username:
        u_success = True
    if u_success and authenticate(file_password, password):
        success = True
        print("login successful")
    return (str(role).strip(), success)

# print menu
def menu():
    print("Options:")
    print("1 - order from manufacturer")
    print("2 - enter time")
    print("3 - schedule repair")
    print("4 - charge customer")
    print("5 - display menu again")
    
    return input("Please enter an option: ")

# read in information from file and put into 2D list
def read_file(filename):
    info = []
    try:
        f = open(filename, "r")

    except:
        print("file could not be opened")
    else:
        for line in f.readlines():
            user_info = line.split(",")
            info.append(user_info)
    return info

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
    # redisplay menu
    if choice == 5:
        choice = menu()
        enter(choice, role)

main()