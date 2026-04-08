import os, sys

# .so file chha ki nai check garne
# filecr.so tapaiko compiled file ko naam ho
if not os.path.isfile('filecr.so'):
    print("\033[1;31m [!] Critical Error: filecr.so not found!")
    print("\033[1;37m [•] Please compile your script first.")
    sys.exit()

try:
    print("\033[1;32m [•] Starting Secured Module...")
    # Compiled .so file lai import gareko
    import filecr
    
    # Yadi .so vitra kunai specific function run garnu parne chha bhane:
    # filecr.main() 
    
except ImportError as e:
    print(f"\033[1;31m [!] Executable Error: {e}")
except Exception as e:
    print(f"\033[1;31m [!] Runtime Error: {e}")
