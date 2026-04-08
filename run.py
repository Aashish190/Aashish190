import os, sys

# .so file chha ki nai check garne
if not os.path.isfile('filecr.so'):
    print("\033[1;31m [!] Component missing! Download again.")
    sys.exit()

try:
    # Yesle sidhai .so vitra ko protection ra original code execute garchha
    import filecr
except Exception as e:
    print(f" [!] Error: {e}")

