import platform
import sys

def print_system_info():
    # Get and print the Python version
    python_version = sys.version
    print(f"Python Version: {python_version}")

    # Get and print the operating system name
    os_name = platform.system()
    print(f"Operating System: {os_name}")



print_system_info()
