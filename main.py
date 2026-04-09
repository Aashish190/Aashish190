import os
import sys

# File check garne
if not os.path.exists("masu.so"):
    print("[!] Error: masu.so bhetiyena!")
    sys.exit()

try:
    import masu
    
    if __name__ == "__main__":
        # Timro masu.py ko menu function call gareko
        masu.menu() 
        
except AttributeError:
    print("[!] Error: 'menu' function yo module ma bhetiyena.")
except Exception as e:
    print(f"[!] Error: {e}")
