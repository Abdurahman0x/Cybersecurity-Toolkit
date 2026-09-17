# Cybersecurity Toolkit

A Python-based collection of basic cybersecurity tools designed for learning and practicing fundamental cybersecurity concepts.

## Features

* **Password Strength Checker**

  * Checks password length and character types.
  * Identifies missing uppercase letters, lowercase letters, numbers, or special characters.

* **Secure Password Generator**

  * Generates random passwords using Python's `secrets` module.
  * Ensures the password contains different character types.

* **Hash Generator**

  * Generates SHA-256 and SHA-512 hashes for text.

* **File Hash Checker**

  * Generates SHA-256 and SHA-512 hashes for files.
  * Reads files in chunks to handle large files efficiently.

* **IP / Domain Checker**

  * Resolves domain names to IP addresses.
  * Performs reverse DNS lookups for IP addresses.

* **Port Checker**

  * Checks whether a TCP port is reachable on a target.

## Project Structure

```text
cybersecurity_toolkit/
│
├── main.py
├── requirements.txt
│
└── toolkit/
    ├── __init__.py
    ├── password_tools.py
    ├── hash_tools.py
    ├── file_tools.py
    └── network_tools.py
```

#### Usage

Run the project using:

```bash
python main.py
```

After running the program, choose a tool by entering its corresponding number:

* Type `1` to use the **Password Strength Checker** and enter a password to check its strength.
* Type `2` to use the **Secure Password Generator** and enter the desired password length.
* Type `3` to use the **Hash Generator**, then enter the text and hashing algorithm (`SHA-256` or `SHA-512`).
* Type `4` to use the **File Hash Checker**, then enter the file path and hashing algorithm (`SHA-256` or `SHA-512`).
* Type `5` to use the **IP / Domain Checker** and enter an IP address or domain name.
* Type `6` to use the **Port Checker**, then enter an IP address or domain name and the port number.
* Type `0` to exit the program.