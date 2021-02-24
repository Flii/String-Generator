import time
import os
import string
import random
from sty import fg
import sys
import ctypes
import traceback

ctypes.windll.kernel32.SetConsoleTitleW("String Generator")
path = os.getcwd() + "/Flii/StringGen/"
letters = string.ascii_uppercase
digit = string.digits

a = fg.blue + """
 ___  ____  ____  ____  _  _   ___       ___  ____  _  _  ____  ____    __    ____  _____  ____ 
/ __)(_  _)(  _ \(_  _)( \( ) / __)     / __)( ___)( \( )( ___)(  _ \  /__\  (_  _)(  _  )(  _ \ 
\__ \  )(   )   / _)(_  )  ( ( (_-.    ( (_-. )__)  )  (  )__)  )   / /(  )\   )(   )(_)(  )   /
(___/ (__) (_)\_)(____)(_)\_) \___/     \___/(____)(_)\_)(____)(_)\_)(__)(__) (__) (_____)(_)\_)
"""

def logo():
    print(a)

def main():
    makefile()

def makefile():

    try:
        f = open(path + "generated.txt")
        time.sleep(0.5)
        logo()
        print("All Required Files Found - Starting Program")
        time.sleep(1.25)
        menu()
    except IOError:
        print("File Not Accessible - Creating it now...")
        time.sleep(0.5)
        try:
            os.makedirs(path)
            os.chdir(path)
            open("generated.txt", "x")
        except OSError:
            time.sleep(0.5)
            print ("File Creation at %s failed" % path)
            

        else:
            time.sleep(0.5)
            print ("Successfully created the file")
            menu()

def menu():
    os.system('cls')
    logo()
    print("""
[1] Generate String
[2] Previous Strings
[3] Quit""")
    mainmenu = input("Please Select An Option: ")

    if mainmenu == "1":
        stringcreation()

    if mainmenu == "2":
        previous()


    if mainmenu == "3":
        print("Thanks For Using Flii's String Generator")
        time.sleep(1.5)
        sys.exit()

def previous():
    os.system('cls')
    logo()
    try:
        file1 = open(path + "generated.txt", "r")
        Lines = file1.readlines()

        count = 0
        for line in Lines:
            count += 1
            time.sleep(0.05)
            print("{}: {}".format(count, line.strip()))
    except OSError:
        print("Error Occured, File Couldn't be reached.")
    retu=input("Type B To Return To Main Menu: ")
    if retu in ["B", "b"]:
        menu()

def randomization():
    quantity=int(input("How Many Strings Would You Like Generated (Max 10K): "))

    if quantity > 10000:
        print("Over Maximum String Limit 10K MAXIMUM, Retrying in 5 Seconds")
        time.sleep(5)
        randomization()
    else:

        e = quantity

        os.system('cls')
        logo()

        while e > 0:
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
            randomstring = ''.join(random.choice(letters + digit) for i in range(16))
            if quantity > 50:
                print (randomstring + "\n")
                try:
                    f = open(path + "generated.txt", "a")
                    f.write(randomstring + "\n")
                    f.close()
                    print("Saved To Backup File: " + path)
                except IOError:
                    print("File Error - This String Will Not Be Saved Please Try Again")

                e -= 1
            else:
                time.sleep(0.2)
                print (randomstring + "\n")
                try:
                    f = open(path + "generated.txt", "a")
                    f.write(randomstring + "\n")
                    f.close()
                    print("Saved To Backup File: " + path)
                except IOError:
                    print("File Error - This String Will Not Be Saved Please Try Again")

                e -= 1
        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
        ret=input("Type B To Return: ")
        if ret in ["b", "B"]:
            menu()

def stringcreation():
    randomization()
    
main()
