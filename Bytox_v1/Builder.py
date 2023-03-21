import os, time, json
from colorama import Fore as F, init

init()


banner = f'''{F.RED}██████╗ ██╗   ██╗████████╗ ██████╗ ██╗  ██╗
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔═══██╗╚██╗██╔╝
██████╔╝ ╚████╔╝    ██║   ██║   ██║ ╚███╔╝ 
██╔══██╗  ╚██╔╝     ██║   ██║   ██║ ██╔██╗ 
██████╔╝   ██║      ██║   ╚██████╔╝██╔╝ ██╗
╚═════╝    ╚═╝      ╚═╝    ╚═════╝ ╚═╝  ╚═╝''' + F.RESET


print("")
print(banner)
print(" - Developed by BlackoutDev -")
print("")
token = input(' [+] Discord Bot Token :: ')
prefix = input( '[+] Command Prefix :: ')
noti_channel = input(' [+] Notification Channel ID :: ')

print(f'{F.WHITE}[{F.YELLOW}!{F.WHITE}] Trying to install colorama')
try:
    os.popen('python3 -m pip install colorama')
    print(f'{F.WHITE}[{F.GREEN}+{F.WHITE}] Colorama installed')
except Exception:
    print(f'{F.WHITE}[{F.RED}-{F.WHITE}] Could not install colorama')

print(f'{F.WHITE}[{F.YELLOW}!{F.WHITE}] Trying to install discord.py')
try:
    os.popen('python3 -m pip install -U discord.py')
    print(f'{F.WHITE}[{F.GREEN}+{F.WHITE} Discord.py installed')
except Exception:
    print(f'{F.WHITE}[{F.RED}-{F.WHITE}] Could not install Discord.py')

if os.path.exists(os.getcwd() + '/conf.json'):
    print(f"{F.WHITE}[{F.GREEN}+{F.WHITE}] {F.YELLOW} conf.json {F.WHITE}already exists")
    time.sleep(2)
    exit()
else:
    new_conf = {"Token": f"{token}", "Prefix": f"{prefix}", "Channel": f"{noti_channel}"}
    print(f"{F.WHITE}[{F.GREEN}+{F.WHITE}] Creating new {F.YELLOW}conf.json")

try:
    with open(os.getcwd() + '/conf.json', 'w+') as f:
        json.dump(new_conf, f)
    print(f"{F.WHITE}[{F.GREEN}+{F.WHITE}] {F.YELLOW} conf.json {F.WHITE}has been created")
    time.sleep(2)
    exit()
except Exception as e:
    print(f"{F.WHITE}[{F.RED}!{F.WHITE}] {F.RED} Error: {F.YELLOW}{e}")