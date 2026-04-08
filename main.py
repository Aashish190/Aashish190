import os, sys

# .so file chha ki nai check garne
if not os.path.isfile('Masu_Encrypted.so'):
    print(" [!] Component missing! Download again.")
    sys.exit()

try:
    # Timro encrypted code lai yaha bata run garchha
    import Masu_Encrypted
except Exception as e:
    print(f" [!] Error: {e}")
    
