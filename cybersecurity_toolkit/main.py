# Cybersecurity Toolkit - A collection of basic security tools.
from colorama import Fore
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
    
    print(Fore.LIGHTGREEN_EX + '=' * 50)
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
    print('=' * 50 + "\n")

    while True:
        choice = input("Choose a tool: ")
        if choice == "0":
            print("Cybersecurity Toolkit Terminating...")
            return
        
    
        if choice == "1":
    
            print("\n" + "=" * 11 + " Password Strength Checker " + "=" * 12 + "\n")
            user_password = input("Enter password: ")
            print(password_strength_checker(user_password))
    
        elif choice == "2":
    
            print("\n" + "=" * 11 + " Secure Password Generator " + "=" * 12 + "\n")
            try:
                password_length = int(input("Enter the desired password's length (length >= 8): "))
                print(secure_password_generator(password_length) + "\n")
            except ValueError:
                print(Fore.RED + "Invalid input! Please try again.\n\n" + Fore.LIGHTGREEN_EX + '=' * 50 + "\n") 

        elif choice == "3":

            print("\n" + "=" * 17 + " Hash Generator " + "=" * 17 + "\n")
            text = input("Enter text to hash: ")
            algorithm = input("Enter algorithm (SHA-256 / SHA-512): ")
            print(f"Hash Generated: \n{hash_generator(text, algorithm)}\n")

        elif choice == "4":

            print("\n" + "=" * 15 + " File Hash Checker " + "=" * 16 + "\n")
            try:
                file_path = input("Enter file name: ")
                algorithm = input("Enter algorithm (SHA-256 / SHA-512): ")
                print(f"File's Hash: \n{file_hash_checker(file_path, algorithm)}\n")
            except FileNotFoundError:
                print(Fore.RED + "Error! File not found.\n" + Fore.LIGHTGREEN_EX + "Make sure the file is in your current working directory.\n\n" + '=' * 50 + "\n")

        elif choice == "5":

            print("\n" + "=" * 14 + " IP / Domain Checker " + "=" * 15 + "\n")
            target = input("Enter IP / Domain: ")
            print(ip_domain_checker(target) + "\n")

        elif choice == "6":

            print("\n" + "=" * 18 + " Port Checker " + "=" * 18 + "\n")
            try:
                target = input("Enter IP / Domain: ")
                port_number = int(input("Enter port number: "))
                print(port_checker(target, port_number) + "\n")
            except ValueError:
                print(Fore.RED + "Invalid port number!" + Fore.LIGHTGREEN_EX + "\nPlease enter a valid integer.\n\n" + "=" * 50 + "\n" )

        else:
            print(Fore.RED + "Invalid input! Please try again.\n" + Fore.LIGHTGREEN_EX)


if __name__ == "__main__":
    main()