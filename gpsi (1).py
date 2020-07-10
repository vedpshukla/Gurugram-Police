import json
import requests  # Install through  pip.
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
print(colored("Coded By: anu", "blue"))
print(colored("Coded By: PR0_D3V1L", "blue"))
print(colored("Version:  1.0", "blue"))
print(colored("Website:  http://vedpshukla.ml", "blue"))
print(colored("Description:This is one of the tools to find out the owner, internet provider and location of any website, domain or IP address. Checking IP addresses is useful for locating the origin of unwanted emails or the source of spam, virus and attacks- Try it out it’s free! ","blue"))

def details(name):
    k=name
    result= requests.get('http://api.hackertarget.com/whois/?q='+k)
    k=result.text
    print(k)
def trace(name):
    command = "tracert " + name
    process = os.popen(command)
    result = str(process.read())
    print("processing ---->")
    print(result)
def ip_look(name):
    command = "nslookup " + name
    process = os.popen(command)
    result = str(process.read())
    print("processing ---->")
    print(result)
def ip_look2(name):
    command = "nslookup " + name
    process = os.popen(command)
    result = str(process.read())
    print("processing ---->")
    return(result)  
def location():
    i=int(input("Enter:\n 0 for IP\n 1 for domain\n"))
    if i==0:
        ko=input()
        print("processing ---->")
        result= requests.get('https://ipvigilante.com/'+ko)
        k=result.text
        res = json.loads(k)
        #print(res[0].item)
        for key, value in res.items():
            if key=='data':
                for i,j in value.items():
                    print(i, ' : ', j)
            else:
                print(key, ' : ', value)
    
    elif i==1:
        ko=input()
        ko=ip_look2(ko)
        k=list(ko.split("\n"))
        for i in k:
            if "Addresses" in i:
                ip=i[12:]
                
        result= requests.get('https://ipvigilante.com/'+ip)
        k=result.text
        res = json.loads(k)
        for key, value in res.items():
            if key=='data':
                for i,j in value.items():
                    print(i, ' : ', j)
            else:
                print(key, ' : ', value)
print("\n>>1 for website details\n>>2 for tracing\n>>3 for IP\n>>4 for location  ")
i=int(input())
if i==1:
    details(input("enter ip or domain :"))
elif i==2:
    trace(input("enter ip or domain name :"))
elif i==3:
    ip_look(input("enter domain name :"))
elif i==4:
    location()
