import getpass, subprocess, psutil, shutil, os, time, requests
from urllib.request import urlretrieve, urlopen
from colorama import Fore
from datetime import datetime
from win32com.client import GetObject

os.system("title RobloxErrorCode: 403 Bypasser")

def display_menu():
    print(f"""
    {Fore.LIGHTBLACK_EX}
                        ██████╗░░█████╗░██████╗░██╗░░░░░░█████╗░██╗░░██╗  ░░██╗██╗░█████╗░██████╗░
                        ██╔══██╗██╔══██╗██╔══██╗██║░░░░░██╔══██╗╚██╗██╔╝  ░██╔╝██║██╔══██╗╚════██╗
                        ██████╔╝██║░░██║██████╦╝██║░░░░░██║░░██║░╚███╔╝░  ██╔╝░██║██║░░██║░█████╔╝
                        ██╔══██╗██║░░██║██╔══██╗██║░░░░░██║░░██║░██╔██╗░  ███████║██║░░██║░╚═══██╗
                        ██║░░██║╚█████╔╝██████╦╝███████╗╚█████╔╝██╔╝╚██╗  ╚════██║╚█████╔╝██████╔╝
                        ╚═╝░░╚═╝░╚════╝░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝  ░░░░░╚═╝░╚════╝░╚═════╝░

                            ██████╗░██╗░░░██╗██████╗░░█████╗░░██████╗░██████╗███████╗██████╗░
                            ██╔══██╗╚██╗░██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗
                            ██████╦╝░╚████╔╝░██████╔╝███████║╚█████╗░╚█████╗░█████╗░░██████╔╝
                            ██╔══██╗░░╚██╔╝░░██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗██╔══╝░░██╔══██╗
                            ██████╦╝░░░██║░░░██║░░░░░██║░░██║██████╔╝██████╔╝███████╗██║░░██║
                            ╚═════╝░░░░╚═╝░░░╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝
                

                                                Created by @s.eths.                              

""")
    
def display_options():
    print("""
                                                
                                Select Method:             
                                [1] Fully Reinstall Roblox
                                [2] Delete RobloxCookies.dat
""")
    
def close_roblox():
    try:
        subprocess.call("TASKKILL /F /IM RobloxPlayerBeta.exe", shell = False)
        print("")
    except:
        pass

def get_version():
    return requests.get("https://setup.rbxcdn.com/version").text

def close_console():
    for process in GetObject("winmgmts:").ExecQuery("select * from Win32_Process where Name = 'cmd.exe'"):
        os.system(f"taskkill /pid {str(process.Properties_('ProcessId').Value)}")

if __name__ == "__main__":
    display_menu(), display_options()
    user_input = input("                                Input: ")
    if user_input.isdigit() and int(user_input) in [1, 2]:
        os.system("cls")
        display_menu()
        print(f"{Fore.LIGHTRED_EX}[{datetime.now().strftime('%H:%M:%S')}] Currently checking for any active roblox tasks.\n")

        while True:
            if list(p.name() for p in psutil.process_iter()).count("RobloxPlayerBeta.exe") != 0:
                close_roblox()
            else:
                break

        if int(user_input) == 1:
            try:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Attempting to remove old Roblox install.\n")
                shutil.rmtree(f"C:\\Users\\{getpass.getuser()}\\AppData\\Local\\Roblox")
            except Exception as e:
                print(f"ERROR: {e}\n")
        elif int(user_input) == 2:
            try:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Attempting to remove RobloxCookies.dat.\n")
                shutil.rmtree(f"C:\\Users\\{getpass.getuser()}\\AppData\\Local\\Roblox\\LocalStorage\\RobloxCookies.dat")
            except Exception as e:
                print(f"ERROR: {e}\n")
        
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Fetching RobloxPlayerLauncher {get_version()}.\n")
        urlretrieve(f"https://setup.rbxcdn.com/Roblox.exe", "RobloxPlayerLauncher.exe")
        subprocess.call("RobloxPlayerLauncher.exe", shell = True)

        os.startfile(r"uninstall.bat")
        os.system("cls")

        display_menu()
        print(f"{Fore.LIGHTRED_EX}[{datetime.now().strftime('%H:%M:%S')}] Error Code 403 has been successfully removed from RobloxPlayerLauncher {get_version()}.\n")
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Press any button to close this console.\n")
        input()
    else:
        print(f"\n{Fore.LIGHTRED_EX}[{datetime.now().strftime('%H:%M:%S')}] ERROR: Please input a correct integer; closing in 3 seconds.")
        time.sleep(3)