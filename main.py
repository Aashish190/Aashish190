import os, sys

# .so file chha ki nai check garne
if not os.path.isfile('masu.so'):
    print(" [!] Component missing! Download again.")
    sys.exit()

try:
    # Timro encrypted code lai yaha bata run garchha
    import masu
except Exception as e:
    print(f" [!] Error: {e}")
    
