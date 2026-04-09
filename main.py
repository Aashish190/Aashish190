import os, sys

# फाइल छ कि नाइ चेक गर्ने
if not os.path.isfile('masu.so'):
    print(" [!] masu.so not found!")
    sys.exit()

try:
    import masu  # यदि masu.so छ भने यसले काम गर्नुपर्छ
    masu.__EXECUTE_CORE__() # तपाईंको स्क्रिप्टको मुख्य फङ्सन रन गर्न
except Exception as e:
    print(f" [!] Error: {e}")
