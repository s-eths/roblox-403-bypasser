import getpass, requests, json, subprocess, psutil, shutil, os, colorama
from urllib.request import urlretrieve
from colorama import Fore

os.system("title Roblox 403 Fixer")

def clear():
    os.system("cls")

def menu():
    print(f"""
    {Fore.LIGHTBLACK_EX}

        ____        __    __              __ __  ____ _____    _______               
       / __ \____  / /_  / /___  _  __   / // / / __ \__  /   / ____(_)  _____  _____
      / /_/ / __ \/ __ \/ / __ \| |/_/  / // /_/ / / //_ <   / /_  / / |/_/ _ \/ ___/
     / _, _/ /_/ / /_/ / / /_/ />  <   /__  __/ /_/ /__/ /  / __/ / />  </  __/ /    
    /_/ |_|\____/_.___/_/\____/_/|_|     /_/  \____/____/  /_/   /_/_/|_|\___/_/
    

                                       Created by sethxd.
                                       

    """)

def get_version():
    for i in requests.get("https://api.whatexploitsare.online/status").json():
        for name in i:
            if name == "ROBLOX":
                return i[name]["version"]

def close_roblox():
    try:
        subprocess.call("TASKKILL /F /IM RobloxPlayerBeta.exe", shell = False)
    except:
        pass
    

if __name__ == "__main__":
    menu()
    print(f"{Fore.LIGHTRED_EX}STATUS: Checking for active roblox tasks.\n")
    while True:
        if list(p.name() for p in psutil.process_iter()).count("RobloxPlayerBeta.exe") != 0:
            close_roblox()
        else:
            break
    try:
        print(f"STATUS: Removing old roblox tracer files.\n")
        shutil.rmtree(f"C:\\Users\\{getpass.getuser()}\\AppData\\Local\\Roblox")
    except Exception as e:
        print(f"ERROR: {e}\n")
    print("STATUS: Attempting to install a clean slate of roblox.\n")
    urlretrieve(f"https://setup.rbxcdn.com/{get_version()}-Roblox.exe", "RobloxPlayerLauncherFixer.exe")
    subprocess.call("RobloxPlayerLauncherFixer.exe", shell = True)
    os.startfile(r"uninstall.bat")
    print("STATUS: Error code 403 has now been fixed.")
