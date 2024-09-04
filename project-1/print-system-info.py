import platform
import psutil

def print_system_info():
    print("System Information")
    print("------------------")

    # OS and version
    print(f"Operating System: {platform.system()} {platform.release()} ({platform.version()})")
    print(f"OS Architecture: {platform.machine()}")

    # Python and compiler details
    print(f"Python Version: {platform.python_version()}")
    print(f"Python Compiler: {platform.python_compiler()}")
    print(f"Python Build: {platform.python_build()}")

print_system_info()
