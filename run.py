import os, sys, shutil, subprocess

def run_fixed_compiler():
    file_input = input(" [•] Enter Script Path (filecr.py): ").strip()
    if not os.path.isfile(file_input): return

    # Exact name extraction
    module_name = os.path.basename(file_input).rsplit('.', 1)[0] # filecr
    temp_py = f"{module_name}.py" # Use same name as module
    
    # Internal logic injection
    with open(file_input, 'r') as f:
        original_code = f.read()

    # Original code lai temp file ma copy garne (Module name match garna)
    # Tyo hardcode logic yaha thapnuhos (get_ultimate_logic wala)
    with open(temp_py, 'w') as f:
        f.write(original_code)

    setup_code = f"""
from setuptools import setup
from Cython.Build import cythonize
setup(
    ext_modules = cythonize("{temp_py}", compiler_directives={{'language_level': "3"}})
)
"""
    with open("setup.py", "w") as f: f.write(setup_code)

    print(f" [•] Compiling module: {module_name}...")
    os.system(f"{sys.executable} setup.py build_ext --inplace")

    # Cleanup
    if os.path.exists("setup.py"): os.remove("setup.py")
    if os.path.exists(f"{module_name}.c"): os.remove(f"{module_name}.c")
    if os.path.isdir("build"): shutil.rmtree("build")

    print(f" [✓] Done! Naya {module_name}.so banyo. Aba run garnuhos.")

if __name__ == "__main__":
    run_fixed_compiler()
