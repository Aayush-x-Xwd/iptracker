import os
import platform
import time
import requests as re

#-----#GLOBAL VARIABLE#-----#

target_ip = ""
os_name = platform.system()
user_ip = re.get("https://api.ipify.org").text

#-----#LOGO#-----#

def logo():
    print("""  ________     __________  ___   ________ __    ___    _   ___________ __  __
   /  _/ __ \   /_  __/ __ \/   | / ____/ //_/   /   |  / | / /  _/ ___// / / /
   / // /_/ /    / / / /_/ / /| |/ /   / ,<     / /| | /  |/ // / \__ \/ /_/ / 
 _/ // ____/    / / / _, _/ ___ / /___/ /| |   / ___ |/ /|  // / ___/ / __  /  
/___/_/        /_/ /_/ |_/_/  |_\____/_/ |_|  /_/  |_/_/ |_/___//____/_/ /_/   
                                                                               



 IP TRACKER
 VERSION : 0.1
          """)

#-----#USEFULL DEFS#-----#

def clear():
    if os_name=="Windows":
         os.system("CLS")
    else:os.system("clear")
def line():
    print("="*40)
def exit():
    if os_name=="Windows":
         os.system("exit")
    else:os.system("exit")
def github():
    if os_name == 'Windows':
        os.system(f'start https://github.com/ANISHBAU')
    else:os.system(f'xdg-open https://github.com/ANISHBAU')
    menu()

#-----#MAIN MENU#-----#

def menu():
    clear()
    logo()
    line()
    print(f" YOUR PUBLIC IP : {user_ip}")
    line()
    print(""" [1] CHECK OWN IP\n [2] CHECK OTHERS IP \n [3] GITHUB REDIRECT \n [0] EXIT""")
    line()
    harry_menu = input(" CHOOSE : ")
    if harry_menu == '1':
        global target_ip
        target_ip = user_ip
        harry_check()
    elif harry_menu == '2':
        line()
        target_ip = input(" ENTER IP ADDRESS : ")
        harry_check()
    elif harry_menu == '3':
        github()
    elif harry_menu == '0':
        exit()
    else:
        line()
        print(" NO OPTION FOUND")
        time.sleep(1)
        menu()

#-----#CRAWL INFO#-----#

def get_details(target_ip):
    url = f"https://ipinfo.io/{target_ip}/json"
    response = re.get(url)
    if response.status_code == 200:
        details = response.json()
        return details
    else:
        return None

#-----#CHECKER#-----#

def harry_check():
    global target_ip
    get_details(target_ip)
    ip_details = get_details(target_ip)
    if ip_details:
        line()
        print(f" [>] IP Address: {ip_details['ip']}")
        print(f" [>] Hostname: {ip_details.get('hostname', 'N/A')}")
        print(f" [>] City: {ip_details.get('city', 'N/A')}")
        print(f" [>] Region: {ip_details.get('region', 'N/A')}")
        print(f" [>] Country: {ip_details.get('country', 'N/A')}")
        print(f" [>] Location: {ip_details.get('loc', 'N/A')}")
        print(f" [>] Organization: {ip_details.get('org', 'N/A')}")
    else:
        line()
        input(" ENTER TO EXIT ")


menu()