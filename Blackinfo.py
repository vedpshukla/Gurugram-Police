import json
import requests
import re
import termcolor
import os
import sys
import colorama
from termcolor import colored


colorama.init()

print(colored("""

  ____  _            _         _____        __      
 |  _ \| |          | |       |_   _|      / _|     
 | |_) | | __ _  ___| | ________| |  _ __ | |_ ___  
 |  _ <| |/ _` |/ __| |/ /______| | | '_ \|  _/ _ \ 
 | |_) | | (_| | (__|   <      _| |_| | | | || (_) |
 |____/|_|\__,_|\___|_|\_\    |_____|_| |_|_| \___/ 


""", "red"))
print(colored("Coded By: Ark-Anu", "blue"))
print(colored("Coded By: PR0_D3V1L", "blue"))
print()
print(colored("Description:", "red"))
print(colored("This is one of the tools to find out the owner, internet provider and location of any website, domain or IP address. ", "blue"))
print(colored("Checking IP addresses is useful for locating the origin of unwanted emails or the source of spam, virus and attacks- Try it out it’s free! ","blue"))
print()


def details(name):
    k = name
    result = requests.get('http://api.hackertarget.com/whois/?q=' + k)
    k = result.text
    print(k)


def port_scan():
    import socket
    import subprocess
    import sys
    from datetime import datetime

    # Clear the screen
    subprocess.call('clear', shell=True)

    # Ask for input
    remoteServer = input("Enter a remote host to scan: ")
    target = socket.gethostbyname(remoteServer)

    # Print a nice banner with information on which host we are about to scan
    print("-" * 60)
    print("Please wait, scanning remote host", target)
    print("-" * 60)

    # Check what time the scan started
    t1 = datetime.now()

    # Using the range function to specify ports (here it will scans all ports between 1 and 1024)

    # We also put in some error handling for catching errors

    try:
        for port in range(1, 200):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((target, port))
            if result == 0:
                print("Port {}: 	 Open".format(port))
            sock.close()

    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

    # Checking the time again
    t2 = datetime.now()

    # Calculates the difference of time, to see how long it took to run the script
    total = t2 - t1

    # Printing the information to screen
    print('Scanning Completed in: ', total)


def ip_look(name):
    command = "nslookup " + name
    process = os.popen(command)
    result = str(process.read())
    print("processing ---->")
    print(result)


def location():
    i = int(input("Enter:\n 0 for IP\n 1 for domain\n"))
    if i == 0:
        ko = input()
        print("processing ---->")
        result = requests.get('https://ipvigilante.com/' + ko)
        k = result.text
        res = json.loads(k)
        # print(res[0].item)
        for key, value in res.items():
            if key == 'data':
                for i, j in value.items():
                    print(i, ' : ', j)
            else:
                print(key, ' : ', value)

    elif i == 1:
        ko = input()
        ko = ip_look(ko)
        k = list(ko.split("\n"))
        for i in k:
            if "Addresses" in i:
                ip = i[12:]

        result = requests.get('https://ipvigilante.com/' + ip)
        k = result.text
        res = json.loads(k)
        for key, value in res.items():
            if key == 'data':
                for i, j in value.items():
                    print(i, ' : ', j)
            else:
                print(key, ' : ', value)


while True:

    print("So how would you like to proceed with your investigation? ")
    print()
    print("\n>>1 Website details\n>>2 Port Scanner\n>>3 IP search\n>>4 Trace Location\n>>5 Exit  ")
    i = int(input("enter your choice: "))
    if i == 1:
       details(input("enter ip or domain :"))
    elif i == 2:
         port_scan()
    elif i == 3:
          ip_look(input("enter domain name :"))
    elif i == 4:
       location()
    elif i==5:
        break
