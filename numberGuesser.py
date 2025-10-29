import os
import random
import sys

program_banner= r"""
 _   _                 _                  ____                               
| \ | |_   _ _ __ ___ | |__   ___ _ __   / ___|_   _  ___  ___ ___  ___ _ __ 
|  \| | | | | '_ ` _ \| '_ \ / _ \ '__| | |  _| | | |/ _ \/ __/ __|/ _ \ '__|
| |\  | |_| | | | | | | |_) |  __/ |    | |_| | |_| |  __/\__ \__ \  __/ |   
|_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \____|\__,_|\___||___/___/\___|_|   
_____________________________________________________________________________
    
"""

main_menu = rf"""
{program_banner}
1- Start The Game
2- Exit
_____________________________________________________________________________
"""

def startGame():
    numbeRange = int(input("Enter the range (min 4) :: "))
    print("Creating the random number...")
    rNumber= random.randint(1,numbeRange)
    print("Number created.")
    guessed = False
    for i in range (3):
        guessNumber = int(input("Enter the guess :: "))
        if guessNumber == rNumber:
            guessed = True
            print("You guessed the number!")
        if guessNumber != rNumber:
            print("Your guess is wrong.")
    if guessed != True:
        print(f"You couldn't guess the number, the number was {rNumber}.")

    print("______________________________________________________________________")
    playAgain= input("Play again? (y/n) :: ")
    if playAgain == "y" or playAgain == "Y":
        startGame()
    if playAgain != "y" or "Y":
        print("Returning the main menu...")
        os.system("clear")
        print(main_menu)

def exit():
    print("Exiting...")
    sys.exit(1)

choiceList=[1,2]

def main():
    os.system("clear")
    print(main_menu)
    while True:
        choice = int(input("Enter your choice :: "))
        if choice == 1:
            startGame()
        elif choice == 2:
            exit()
        if not choice in choiceList:
            print("Please choose one of the mentioned options.")

if __name__ == "__main__":
    main()
