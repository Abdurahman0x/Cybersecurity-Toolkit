import secrets


def password_strength_checker(password: str):
    """
    Checks the strength of the given password,
    based on its length and character types.
    
    Args:
        password (str): The user's password to check.
        
    Returns:
        str: The strength level of the password.
    """

    strength_level = 4  # Start with the maximum strength level
    note_for_user = "\n"  # Stores suggestions for the user

    if len(password) < 8:
        note_for_user = "Password must be at least 8 characters.\n"
        return "Password Strength Level: Weak\n" + note_for_user

    has_uppercase = False
    has_lowercase = False
    has_number = False
    has_special_character = False

    # Check for uppercase, lowercase, numbers, and special characters
    for character in password:

        if character.isupper():
            has_uppercase = True
        if character.islower():
            has_lowercase = True
        if character.isdigit():
            has_number = True
        if not character.isalnum():
            has_special_character = True


    if not has_uppercase:
        strength_level -= 1
        note_for_user += "Password must contain at least one uppercase letter.\n"
    
    if not has_lowercase:
        strength_level -= 1
        note_for_user += "Password must contain at least one lowercase letter.\n"

    if not has_number:
        strength_level -= 1
        note_for_user += "Password must contain at least one number.\n"

    if not has_special_character:
        strength_level -= 1
        note_for_user += "Password must contain at least one special character.\n"


    if strength_level <= 2:
        strength_level = "Weak"

    elif strength_level <= 3:
        strength_level = "Medium"

    else:
        strength_level = "Strong"

    return "Password Strength Level: " + str(strength_level) + note_for_user


def secure_password_generator(password_length: int):
    """
    Generates a secure random password of the given length.
    
    Args:
        password_length (int): The desired length of the password.

    Returns:
        str: The generated secure password.
    """

    if password_length < 4:
        return "Password length must be at least 4 characters."

    numbers = "0123456789"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    special_characters = "!@#$%^&*"

    secure_password = ""

    secure_password += secrets.choice(numbers)
    secure_password += secrets.choice(uppercase)
    secure_password += secrets.choice(lowercase)
    secure_password += secrets.choice(special_characters)
     
    allowed_characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*"

    for _ in range(password_length - 4):
        secure_password += secrets.choice(allowed_characters)

    password_list = list(secure_password)
    secrets.SystemRandom().shuffle(password_list)
    secure_password = "".join(password_list)

    return "Generated Password: " + secure_password