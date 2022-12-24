'''
Welcome to OS.py 0.1.0 Terminal Source Code!

Don't mess things up!
'''

# Building Terminal

def initialise():

    command = ""

    while command.lower() != "shutdown":
        command = input("> ")

        if command.lower() == "show":
            print("""
What do you want to show?
            
Exmaple: show users
""")

        elif command.lower() == "show users":
            print("""
1 user:

1. root
""")

        elif command.lower() == "refresh":
            print("Refreshed")

        elif command.lower() == "exit":
            question = input('Do you mean "shutdown"[y/n]? ')
            if question.lower() == "y":
                print("shutting down...")
                break

            else:
                continue

        elif command == "restart terminal":
            print("restarting...")
            initialise()

        # Building a simple Calculator

        elif command.lower() == "calc":
            print("Welcome to the OS.py Calculator!")
            print('''
Note: You can put in the "Arithmetic Sign" Field only: *, +, -, /,
// (returns an integer, like 1, 2, 3),
% (returns the remainder of division),
** (means exponentiation, x ** y means x to the power of y).
                ''')
            FirstNum = int(input("First Number: "))
            ArithSign = input("Arithmetic sign: ")
            SecondNum = int(input("Second Number: "))

            if ArithSign == "*":
                print(f"Result: {FirstNum * SecondNum}.")

            elif ArithSign == "+":
                print(f"Result: {FirstNum + SecondNum}")

            elif ArithSign == "/":
                print(f"Result: {FirstNum / SecondNum}")

            elif ArithSign == "-":
                print(f"Result: {FirstNum - SecondNum}")

            elif ArithSign == "//":
                print(f"Result: {FirstNum // SecondNum}")

            elif ArithSign == "%":
                print(f"Result: {FirstNum % SecondNum}")

            elif ArithSign == "**":
                print(f"Result: {FirstNum ** SecondNum}")

            else:
                print("Error: Arithmetic Sign is not defined")

        # End of Building the Calculator

    # --------------------

        elif command == "OS.py":
            print("""is the OS you're using now""")

        elif command.lower() == "info":
            print("""OS.py - 0.1.0

Created by: Husayn al-Qurashi.

This is the first Project I created in Python, and I'm very Happy with it!

Thank you for reading.
            """)

        elif command == "":
            continue

        elif command == "ID8":
            print("""
ID8 = info
            """)

        elif command == "ID7":
            print("""
ID7 = calc
            """)

        elif command == "ID6":
            print("""
ID6 = restart terminal
            """)

        elif command == "ID5":
            print("""
ID5 = refresh
            """)

        elif command == "ID4":
            print("""
ID4 = show users
            """)

        elif command == "ID3":
            print("""
ID3 = shutdown
            """)

        elif command == "ID1":
            print("""
ID1 = help
            """)

        elif command == "help":
            print("""
Welcome to the help menu in the Terminal!

You can Do:
ID6 = restart terminal - restarts the terminal (not the system).
ID1 = help - shows help menu.
ID7 = calc - opens OS.py calculator.
ID5 = refresh - refreshes the screen.
ID8 = info - shows OS.py version, Credits and more.
ID4 = show users - shows users.
ID3 = shutdown - turns the Computer off.
            """)

        elif command.lower() == "shutdown":
            print("shutting down...")
            break

        else:
            print("Error: Error")

# End of building the Terminal
