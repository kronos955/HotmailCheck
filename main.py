import requests
from termcolor import colored
import time
import concurrent.futures
import art
from colorama import Fore, init

init(autoreset=True)

Art = art.text2art("Kronos")
print(Fore.LIGHTGREEN_EX + Art)

print(Fore.YELLOW + "Hotmail Checker")

available = open('availableHotmail.txt', 'a+')
notAvailable = open('notAvailableHotmail.txt', 'a+')

def check(email):

    availableText = "Neither"
    notAvailableText = "MSAccount"
    link = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + email + "&_=1604288577990"
    data = ""
    header = {
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
        "Connection": "close",
        "Host": "odc.officeapps.live.com",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
        "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
        "canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
        "uaid": "d06e1498e7ed4def9078bd46883f187b",
        "Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"
        }
    response = requests.get(link, data=data, headers=header).text
    if availableText in response:
        print(colored("[+]AVAILABLE "+ email,'green'))
        available.write(email + "\n")
    elif notAvailableText in response:
        print(colored("[-]TAKEN "+ email,'red'))
        notAvailable.write(email + "\n")
    else:
        pass


with open('emails.txt', 'a') as f:
    emails = [line.strip() for line in f]

a = input("Press Enter to Start...")

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(check,emails)
