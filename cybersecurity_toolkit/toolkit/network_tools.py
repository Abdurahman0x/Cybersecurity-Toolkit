import socket
import ipaddress
from colorama import Fore


def ip_domain_checker(target: str):
    """
    Checks an IP address or domain name,
    and retrieves its corresponding hostname or IP address.

    Args:
        target (str): The IP address or domain name to check.

    Returns:
        str: The resolved hostname or IP address,
        or an error message.
    """

    socket.setdefaulttimeout(3)

    try:
        # Validate whether the target is an IP address
        ipaddress.ip_address(target)

        try:
            result = socket.gethostbyaddr(target)
            return "Hostname: " + result[0] + "\n\n" + '=' * 50 
            
        except (socket.gaierror, socket.herror, socket.timeout):
            return "No reverse DNS record found.\n\n" + '=' * 50

    except ValueError:
        try:
            # ValueError is raised, so the target is a domain, not an IP.
            result = socket.gethostbyname(target)
            return "Resolved IP: " + result + "\n\n" + '=' * 50 
            
        except (socket.gaierror, socket.timeout):
            return Fore.RED + "Error! Unable to resolve the IP / Domain.\n\n" + Fore.LIGHTGREEN_EX + '=' * 50


def port_checker(target: str, port_number: int):
    """
    Checks whether a TCP port is open on the specified target.
    
    Args:
        target (str): The IP address or domain to check.
        port_number (int): The TCP port number to check.

    Returns:
        str: A message indicating whether the port is open or closed,
        or an error message if the target cannot be resolved.
    """

    if port_number < 1 or port_number > 65535:
        return Fore.RED + "Invalid port number!\n" + Fore.LIGHTGREEN_EX + "Port must be between 1 and 65535.\n\n" + '=' * 50

    # Create an IPv4 TCP socket and store it in client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(2)

    try:

        # Attempting to establish a TCP connection with target and port_number
        connection_result = client_socket.connect_ex((target, port_number))
        
        if connection_result == 0:
            return f"Port {port_number} is OPEN.\n\n" + '=' * 50
        else:
            return f"Port {port_number} is CLOSED.\n\n" + '=' * 50
        
    except socket.gaierror:
        return Fore.RED + "Error! Unable to resolve the IP / Domain.\n\n" + Fore.LIGHTGREEN_EX + '=' * 50 
    
    finally:
        client_socket.close()