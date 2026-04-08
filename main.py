import os, sys

# 1. Check garne file chha ki nai
if not os.path.isfile('Masu_Encrypted.so'):
    print(" [!] Component missing! Downloading...")
    # Yaha timi os.system('curl ...') garera download garne command pani halna sakchau
    exit()

# 2. .so file lai import garera run garne
try:
    import Masu_Encrypted
    # Yadi timro original script ma main() function thiyo bhane:
    # Masu_Encrypted.main() 
except Exception as e:
    print(f" [!] Error: {e}")
