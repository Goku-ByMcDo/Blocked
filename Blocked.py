import ipaddress

autre = "netstat -r -s -e -a -b -x"
scanner = "netstat -r -s -e"

try:
    from colorama import *
    from art import *
    from ipaddress import *
    import os
    import requests
    import socket 
    import threading
    import queue
    import re
    import subprocess
    import time
except:
    print("Launching")
    os.system("pip install colorama >nul")
    os.system('pip install requests >nul')
    os.system("pip install art >nul")
    os.system('pip install ipadresse >nul')
    os.system("cls")

def avanced():
    try:    
        r = os.system(scanner)
        time.sleep(5)
        print(Fore.GREEN + "\n*" + Fore.RESET + " sought advance")
        input("")
        print(Fore.RED + r + Fore.RESET)
        input()
        print(Fore.GREEN + "*" + Fore.RESET + "Finish")
        finish = input("")
        os.system('set /p VarQuestion=.')
    except:
        try:
            print("Please run as administrator")         
        except:
            print('Error')
            input("")

def menu():
    os.system('cls')
    print("\n")
    tprint("blocked", font="random")
    print(Fore.RED + "          [1]" + Fore.RESET + "- Scanner")
    choice = input("\nEnter ur choice > ")

    if choice == "1":
        avanced()
    else:
        pass

menu()
