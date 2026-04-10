import os
import sys

# 1. Check if .so file exists
if not os.path.exists("filecr.so"):
    print("Error: filecr.so bhetiyena! Please clone again.")
    sys.exit()

try:
    import filecr  # Import protected file
    
    # 2. Check if 'menu' exists and run it
    if hasattr(filecr, 'menu'):
        filecr.menu()
    elif hasattr(filecr, 'main'):
        filecr.main()
    else:
        # If function name is unknown, try to find and run any available function
        funcs = [f for f in dir(filecr) if not f.startswith('__')]
        if funcs:
            getattr(filecr, funcs[0])()
        else:
            print("Error: No executable function found in filecr.so")

except Exception as e:
    print(f"Error: {e}")
