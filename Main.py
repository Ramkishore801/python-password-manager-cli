import random
import string

# Track login status
logged_in = False


# ------------------ REGISTER ------------------
def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")

    print("User registered successfully\n")


# ------------------ LOGIN ------------------
def login():
    global logged_in

    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        with open("users.txt", "r") as file:
            for line in file:
                user, pwd = line.strip().split(",")

                if user == username and pwd == password:
                    print("Login successful\n")
                    logged_in = True
                    return

        print("Invalid username or password\n")

    except FileNotFoundError:
        print("No users found. Please register first\n")


# ------------------ GENERATE PASSWORD ------------------
def generate_password():
    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("Please enter a valid number\n")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    print(f"Generated Password: {password}\n")


# ------------------ SAVE PASSWORD ------------------
def save_password():
    if not logged_in:
        print("Please login first\n")
        return

    site = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("vault.txt", "a") as file:
        file.write(f"{site},{username},{password}\n")

    print("Password saved successfully\n")


# ------------------ VIEW PASSWORDS ------------------
def view_passwords():
    if not logged_in:
        print("Please login first\n")
        return

    try:
        with open("vault.txt", "r") as file:
            print("\nSaved Passwords:\n")
            print(file.read())

    except FileNotFoundError:
        print("No saved passwords found\n")


# ------------------ MAIN PROGRAM ------------------
def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Generate Password")
        print("4. Save Password")
        print("5. View Passwords")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            generate_password()
        elif choice == "4":
            save_password()
        elif choice == "5":
            view_passwords()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice\n")


# Run the program
main()
