import hashlib


def hash_generator(text: str, algorithm: str):
    """
    Generates a cryptographic hash of the given text,
    using the specified hashing algorithm.

    Args:
        text (str): The text to hash.
        algorithm (str): The hashing algorithm to use.

    Returns:
        str: The generated hash, or an error message.
    """

    while True:

        if algorithm.upper() == "SHA-256":
            return hashlib.sha256(text.encode()).hexdigest()
        
        elif algorithm.upper() == "SHA-512":
            return hashlib.sha512(text.encode()).hexdigest()
    
        else:
            print("\nUnsupported algorithm! Please use SHA-256 or SHA-512.")
            algorithm = input("Enter algorithm (SHA-256 / SHA-512): ")