import os, sys
try:
    import filecr
    filecr.main() # वा filecr भित्रको मुख्य function जुन रन हुनुपर्ने हो
except Exception as e:
    print(f"Error: {e}")
