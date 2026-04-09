import os
import sys

# masu.so file current directory ma cha ki chaina check garne
if not os.path.exists("masu.so"):
    print("Error: masu.so file bhetiyena!")
    print("Kripaya full repository clone garnu hola.")
    sys.exit()

try:
    import masu  # .so file lai direct import garcha
    
    if __name__ == "__main__":
        # masu.py ko main logic function call gara
        # Example: masu.start() or masu.main()
        masu.run() 
except ImportError as e:
    print(f"Import Error: {e}")
    print("Check gara ki .so file timro architecture (aarch64/arm) ko lagi ho ki haina.")
