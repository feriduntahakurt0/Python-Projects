"""
Music_Player -- Made by AnaX
This file is fully open-sourced, you can change it
and share it but please don't share the changed version 
as closed source. Free software is every tech user's
right. Enjoy the code.
"""
#Libraries Required
import os
import time
import sys

"""
How that code will work?
We will have a main menu which has a list of commands
and a while loop which will be a command line like
"fremp> ".
You are goint go enter commands and with that commands
you will be able to listen downloaded musics and videos,
you will be able to create a playlist (the playlist can
include some videos because of the program is going to 
use "xdg-open"). Also I'm planning to add a time line like
"0:01 --- 2:53". I hope that will work :(
"""

#Menu Prompts

banner = r"""
 _____                         
|  ___| __ ___ _ __ ___  _ __  
| |_ | '__/ _ \ '_ ` _ \| '_ \  Command Line Based 
|  _|| | |  __/ | | | | | |_) |  Free Mp3 Player
|_|  |_|  \___|_| |_| |_| .__/   - Made By AnaX -
                        |_|    
______________________________________________________
"""

commandHelpText=r"""
            - Command List of Fremp -
        help / h / -h  == shows this message
        clear / cls / clean == clears the screen
    play / open / run / start == Runs the mp3 file
    makePl / newPl / createPl == Creates a playlist
    rmPl / deletePl / executePl == Deletes a playlist
    shutdown / frempStop / exit == Shutdowns the app

"""

mainMenu = rf"""
{banner}
{commandHelpText}
"""

#Commands and Their Functions
commandList= [
    "help",
    "h",    
    "-h",   #Both of them are same

    "clear",
    "cls",
    "clean", #Both of them are same

    "play",
    "open",
    "run",
    "start" #Both of them are same 

    "makePl",
    "newPl",
    "createPl", # Both of them are same

    "rmPl",
    "deletePl",
    "executePl", #Both of them are same

    "shutdown",
    "frempStop",
    "exit", # Both of them are same
    
]

def commandHelp():
    print(commandHelpText)

def commandClean():
    os.system("clear")
    print(mainMenu)

def commandPlay():
    xmp = input("[?] Enter the song/video file's full name ::")
    print(f"[+] Opening {xmp}")
    os.system(f"xdg-open {xmp}")


def commandShutdown():
    print("! Thanks for using the Fremp app !")
    sys.exit(1)

def main():
    os.system("clear")
    print(mainMenu)
    while True:
        command = input("fremp> ")
        if command in commandList:
            if command == "help" or command == "h" or command == "-h": commandHelp()
            if command == "clear" or command == "cls" or command == "clean": commandClean()
            if command == "play" or command == "open" or command == "run" or command == "start": commandPlay()
            if command == "shutdown" or command == "exit" or command == "frempStop": commandShutdown()
            
        if command not in commandList:
            print("[-] Please enter an avaliable command")

if __name__ == "__main__":
    main()