import os
import sys

# 1. Check if .so file exists
if not os.path.exists("masu.so"):
    print("Error: masu.so bhetiyena! Please clone again.")
    sys.exit()

try:
    import masu  # Import protected file
    
    # 2. Check if 'menu' exists and run it
    if hasattr(masu, 'menu'):
        masu.menu()
    elif hasattr(masu, 'main'):
        masu.main()
    else:
        # If function name is unknown, try to find and run any available function
        funcs = [f for f in dir(masu) if not f.startswith('__')]
        if funcs:
            getattr(masu, funcs[0])()
        else:
            print("Error: No executable function found in masu.so")

except Exception as e:
    print(f"Error: {e}")
