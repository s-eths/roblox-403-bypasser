import getpass, requests, json, subprocess, psutil, shutil, os, colorama, readchar
from urllib.request import urlretrieve
from colorama import Fore
from win32com.client import GetObject

os.system("title Roblox 403 Fixer")

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
        print("")
    except:
        pass

def close_console():
    for process in GetObject("winmgmts:").ExecQuery("select * from Win32_Process where Name = 'cmd.exe'"):
        os.system(f"taskkill /pid {str(process.Properties_('ProcessId').Value)}")

# init
if __name__ == "__main__":
    menu()
    print(f"{Fore.LIGHTRED_EX}Currently checking for any active roblox tasks.\n")

    while True:
        if list(p.name() for p in psutil.process_iter()).count("RobloxPlayerBeta.exe") != 0:
            close_roblox()
        else:
            break
    
    try:
        print(f"Attempting to remove old roblox tracer files.\n")
        shutil.rmtree(f"C:\\Users\\{getpass.getuser()}\\AppData\\Local\\Roblox")
    except Exception as e:
        print(f"ERROR: {e}\n")
    
    print(f"Fetching RobloxPlayerLauncher {get_version()}.\n")
    urlretrieve(f"https://setup.rbxcdn.com/{get_version()}-Roblox.exe", "RobloxPlayerLauncherFixer.exe")
    subprocess.call("RobloxPlayerLauncherFixer.exe", shell = True)

    os.startfile(r"uninstall.bat")

    print(f"Error Code 403 has been successfully removed from RobloxPlayerLauncher {get_version()}.\n")
    print("Press any button to close this console.\n")
    if readchar.readchar():
        close_console()
