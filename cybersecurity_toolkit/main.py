# Cybersecurity Toolkit - A collection of basic security tools.

from toolkit.password_tools import password_strength_checker, secure_password_generator
from toolkit.hash_tools import hash_generator
from toolkit.file_tools import file_hash_checker
from toolkit.network_tools import ip_domain_checker, port_checker


def main():
    """
    Displays the main menu of the Cybersecurity Toolkit to the user,
    and handles the initial user interaction.

    Returns:
        None
    """
    
    print('=' * 50)
    print("||" + " " * 46 + "||")
    print("||" + " " * 12 + "CYBERSECURITY TOOLKIT" + " " * 13 + "||")
    print("||" + " " * 17 + "Version 1.0" + " " * 18 + "||")
    print("||" + " " * 46 + "||")
    print("||" + " " * 5 + "A collection of basic security tools" + " " * 5 + "||")
    print("||" + " " * 46 + "||")
    print('=' * 50 + "\n")

    print("[1] Password Strength Checker")
    print("[2] Secure Password Generator")
    print("[3] Hash Generator")
    print("[4] File Hash Checker")
    print("[5] IP / Domain Checker")
    print("[6] Port Checker")
    print("[0] Exit\n")

    while True:
        choice = input("Choose a tool: ")
        if choice == "0":
            print("Cybersecurity Toolkit Terminating...")
            return
        
        print()
    
        if choice == "1":
    
            print("-" * 10 + " Password Strength Checker " + "-" * 11 + "\n")
            user_password = input("Enter password: ")
            print(password_strength_checker(user_password))
    
        elif choice == "2":
    
            print("-" * 10 + " Secure Password Generator " + "-" * 11 + "\n")
            try:
                password_length = int(input("Enter the desired password's length (length >= 4): "))
                print(secure_password_generator(password_length) + "\n")
            except ValueError:
                print("Invalid input! Please try again.")

        elif choice == "3":

            print("-" * 16 + " Hash Generator " + "-" * 16 + "\n")
            text = input("Enter text to hash: ")
            algorithm = input("Enter algorithm (SHA-256 / SHA-512): ")
            print(f"Hash Generated: \n{hash_generator(text, algorithm)}\n")

        elif choice == "4":

            print("-" * 14 + " File Hash Checker " + "-" * 15 + "\n")
            try:
                file_path = input("Enter file name: ")
                algorithm = input("Enter algorithm (SHA-256 / SHA-512): ")
                print(f"File's Hash: \n{file_hash_checker(file_path, algorithm)}\n")
            except FileNotFoundError:
                print("Error! File not found.\nMake sure the file is in your current working directory.\n")

        elif choice == "5":

            print("-" * 13 + " IP / Domain Checker " + "-" * 14 + "\n")
            target = input("Enter IP / Domain: ")
            print(ip_domain_checker(target) + "\n")

        elif choice == "6":

            print("-" * 17 + " Port Checker " + "-" * 17 + "\n")
            try:
                target = input("Enter IP / Domain: ")
                port_number = int(input("Enter port number: "))
                print(port_checker(target, port_number) + "\n")
            except ValueError:
                print("Invalid port number! Please enter a number.\n")

        else:
            print("Invalid input! Please try again.")


if __name__ == "__main__":
    main()