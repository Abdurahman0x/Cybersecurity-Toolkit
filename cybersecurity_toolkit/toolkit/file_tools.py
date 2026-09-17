import hashlib


def file_hash_checker(file_path: str, algorithm: str):
    """
    Generates a cryptographic hash of a file,
    using the specified hashing algorithm.

    Args:
        file_path (str): The path of the file to hash.
        algorithm (str): The hashing algorithm to use.

    Returns:
        str: The generated file hash.
    """

    with open(file_path, "rb") as file:

        while True:
        
            if algorithm.upper() == "SHA-256":
                hash_function = hashlib.sha256()
                break

            elif algorithm.upper() == "SHA-512":
                hash_function = hashlib.sha512()
                break

            else:
                print("\nUnsupported algorithm! Please use SHA-256 or SHA-512.")
                algorithm = input("Enter algorithm (SHA-256 / SHA-512): ")

        while True:

            chunk = file.read(4096)

            if not chunk:
                break

            hash_function.update(chunk)

        return hash_function.hexdigest()