from utils.interface import inface


def user_login():

    print("Welcome to OS.py 0.1.0!")

    username = input("Username: ")
    passcode = input("Passcode: ")

    if username == "root" and passcode == "password123":
        inface()

    elif username == "root" or passcode == "password123":
        print("Username or Password is Invalid.")

    else:
        print("Username and Passcode are Invalid.")
