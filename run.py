import os, sys, importlib.util

# 1. Check if .so exists
so_file = 'filecr.so'
if not os.path.isfile(so_file):
    print("\033[1;31m [!] Component missing! Download again.")
    sys.exit()

try:
    # 2. Force Load Module (Internal name mismatch fix)
    # Yesle PyInit_filecr ko error lai bypass garna khojcha
    spec = importlib.util.spec_from_file_location("filecr", os.path.abspath(so_file))
    module = importlib.util.module_from_spec(spec)
    sys.modules["filecr"] = module
    spec.loader.exec_module(module)
    
except Exception as e:
    # 3. Yadi mathi ko le kaam garena bhane, compiler mai error chha
    print(f"\033[1;31m [!] Error: {e}")
    print("\033[1;33m [•] Note: Tapai ko .so file 'filecr.py' name bata compile bhayeko huna parcha.")
