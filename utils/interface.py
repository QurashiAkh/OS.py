from terminal.terminal import initialise


def inface():

    user_name = "root"
    user_fpl = "Python 3"

    print(f"Welcome {user_name}!")

    print(f"""Name: {user_name}, FPL: {user_fpl}.

OS.py Version 0.1.0.""")

    print("Do you want to do Something? Go to terminal.")
    initialise()
