# main.py
import os
import sys

# Check if masu.so exists
if not os.path.isfile("masu.so"):
    print("[!] masu.so missing. Make sure it's in the same folder.")
    sys.exit()

try:
    import masu   # import the compiled module
except Exception as e:
    print("[!] Failed to load masu.so:", e)
    sys.exit()

print("[✓] masu.so loaded successfully!")
