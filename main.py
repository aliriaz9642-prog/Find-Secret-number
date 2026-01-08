# Find the secret number
from random import *
import pyttsx3
import sys
import time as t
from colorama import *
init(autoreset=True)

engine = pyttsx3.init()
engine.setProperty("rate",150) 

def speak(text):
    engine.say(text)

    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        t.sleep(0.05)

    engine.runAndWait()
    print()

while True:
    print(Fore.MAGENTA + "*****Choose the level (1-3)*****")
    print(Fore.BLUE+Style.BRIGHT+"1 - Easy\n2 - Medium\n3 - Hard")

    try:
        user = int(input("Enter level : "))
    except:
        print("Enter between (1-3)")

# Easy Level
    if user == 1:
        print(Fore.LIGHTGREEN_EX+Style.BRIGHT +"--------------------\n Easy level Selected \n--------------------")
        speak("You have 6 moves, to Find the number between 1 to 50")
        x = randint(1,50)
        for i in range(1,7):
            num = int(input(f"Attempt {i}, Enter number between (1-50): "))
            if num > 50 or num < 1:
                print("Enter between (1-50) only!")
                continue
            if num > x:
                print(Fore.LIGHTCYAN_EX +"|  Thora neechay try kro  |")
            elif num < x:
                print(Fore.LIGHTMAGENTA_EX+"|  Thora upar try kro  |")
            else:
                print(Fore.GREEN +" Congratulations, You found the secret number  ")
                break
            if i == 4:
                print(Fore.YELLOW +"|  2 Mvoves left  |")
            elif i == 5:
                print(Fore.YELLOW +"|  This is do or die  |")
        else:  
            print(Fore.RED +"Oops...! Try again")
            print(Fore.GREEN +"The number was", x)

# Medium Level
    elif user == 2:
        print(Fore.LIGHTYELLOW_EX+Style.BRIGHT +"-----------------------\n Medium level Selected \n----------------------")
        speak("You have 6 moves, to Find the number between 1 to 100")
        x = randint(1, 100)

        for i in range(1, 7):
            num = int(input(f"Attempt {i}, Enter number between (1-100): "))
            if  num > 100 or num < 1:
                print("Enter between (1-100) only!")
                continue

            if num > x:
                print(Fore.LIGHTCYAN_EX +"|  Thora neechay try kro  |")
            elif num < x:
                print(Fore.LIGHTMAGENTA_EX +"|  Thora upar try kro  |")
            else:
                print(Fore.GREEN + " Congratulations, You found the secret number ")
                break
            if i == 4:
                print(Fore.YELLOW+" | 2 Mvoves left |")
            elif i == 5:
                print(Fore.YELLOW+"This is do or die")
        else:
            print(Fore.RED+"Oops...! Try again")
            print(Fore.GREEN+"The number was", x)
    
# Hard Level
    elif user == 3:
        print(Fore.LIGHTRED_EX+Style.BRIGHT+"--------------------\n Hard level Selected \n--------------------")
        speak("You have 8 moves, to Find the number between 1 to 200")
        x = randint(1, 200)

        for i in range(1, 9):
            num = int(input(f"Attempt {i}, Enter number between (1-200): "))
            if num > 200 or num < 1:
                print("Enter between (1-200) only!")
                continue

            if num > x:
                print(Fore.LIGHTCYAN_EX+"|  Thora neechay try kro  |")
            elif num < x:
                print(Fore.LIGHTMAGENTA_EX+"|  Thora upar try kro  |")
            else:
                print(Fore.GREEN+" Congratulations, You found the secret number ")
                break
            if i == 6:
                print(Fore.YELLOW+"|  2 Mvoves left  |")
            elif i == 7:
                print(Fore.YELLOW+"|  This is do or die  |")
        else:
            print(Fore.GREEN+ "Oops...! Try again")
            print(Fore.GREEN+"The number was", x)
    else:
        print(Fore.RED+"invalid choice")

    play_again = input(Fore.LIGHTCYAN_EX+"Do you want to play again...? (y/n): ")

    if play_again.lower() == "y":
        continue
    elif play_again.lower() == "n":
        print(Fore.RED + "|  Game Over.....!  |")
        break
    else:
        print("Click Y/N only! Exiting...")
        break