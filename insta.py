from myigbot import MyIGBot
import json
from colorama import Fore, Back, Style
from colorama import init
import os
init()
# Simple Instagram Comment Spammer using the MyIGBot library. (https://github.com/b31ngD3v/MyIGBot/)
# If you get a weird response code like "400" means that you are probably being rate limited by Instagram.

print(f"""
{Fore.MAGENTA}
   _____                                     _      _____
  / ____|                                   | |    / ____|
 | |     ___  _ __ ___  _ __ ___   ___ _ __ | |_  | (___  _ __   __ _ _ __ ___  _ __ ___   ___ _ __
 | |    / _ \| '_ ` _ \| '_ ` _ \ / _ \ '_ \| __|  \___ \| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
{Fore.LIGHTMAGENTA_EX} | |___| (_) | | | | | | | | | | |  __/ | | | |_   ____) | |_) | (_| | | | | | | | | | | |  __/ |
  \_____\___/|_| |_| |_|_| |_| |_|\___|_| |_|\__| |_____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|
                                                         | |
                                                         |_|

                            {Fore.MAGENTA}    Credit » https://github.com/A2uma0
""")
print(Fore.LIGHTBLACK_EX)
print("                           » Put your Username and Password in the Json «")
print(Fore.CYAN)
Post = input(f" Target Post Link » ")
Comment = input(f" Text to be Commented » ")
os.system("cls")
print(Fore.WHITE)
print(" » Started Spamming! ")

with open("login.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()


while 200:

    bot = MyIGBot(jsonObject['username'], jsonObject['password'],)
    response = bot.comment(Post, comment_text=Comment)
    if response == 200:
        print(" » Comment has been sent! « ")
