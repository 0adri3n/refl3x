# IMPORTS
#---------------------------------------------------

from ctypes import LittleEndianStructure
from http import client
import tkinter
import tkinter.font as font
from PIL import Image, ImageTk
from lib import gameEasyMode, gameMediumMode, gameHardMode, rpc
import sys
import yaml
import time

#---------------------------------------------------


# LAUNCHER CODE
#---------------------------------------------------

# Functions
#----------------------------------


def startEasy():
    
    gameEasyMode.easyGame()


def startMedium():

    gameMediumMode.mediumGame()


def startHard():

    gameHardMode.hardGame()


def saveSettings(rpcVar, volumeValue, settingsData):


    settingsData["rpc"] = rpcVar.get()
    settingsData["volume"] = volumeValue.get()/10

    settingsWrite = open("data/settings.yaml", "w")
    settingsWrite.write(yaml.dump(settingsData, default_flow_style=False))
    settingsWrite.close()

def settingsWindow():

    settingapp = tkinter.Toplevel()
    settingapp.wm_title("refl3x Settings")
    settingapp.wm_geometry("300x200")
    settingapp.wm_minsize(300, 200)
    settingapp.wm_maxsize(300, 200)
    if sys.platform == "win32":
        settingapp.wm_iconbitmap("src/crosshairIcon.ico")
    settingapp.config(bg="#191919")

    settingsfiles = open("data/settings.yaml", "r")
    settingsData = yaml.safe_load(settingsfiles)
    settingsfiles.close()

    rpcVar = tkinter.IntVar()
    volumeValue = tkinter.IntVar() 

    if settingsData["rpc"] == 1:

        rpcChoice = tkinter.Checkbutton(settingapp, bg="#191919", fg="black", variable=rpcVar)
        rpcChoice.place(x=10, y=10)
        rpcChoice.select()

    else:

        rpcChoice = tkinter.Checkbutton(settingapp, bg="#191919", fg="black", variable=rpcVar)
        rpcChoice.place(x=10, y=10)

    rpcText = tkinter.Label(settingapp, text="Discord RPC", bg="#191919", fg="white")
    rpcText.place(x=30, y=12)

    volumetext = tkinter.Label(settingapp, text="Volume :", bg="#191919", fg="white")
    volumetext.place(x=10, y=35)

    volumeScale = tkinter.Scale(settingapp, bg="#191919", fg="white", from_=0, to=10, orient=tkinter.HORIZONTAL, variable=volumeValue)
    volumeScale.place(x=13, y=60)

    volumeScale.set(settingsData["volume"]*10)

    saveButton = tkinter.Button(settingapp, text="Save settings", bg="white", fg="black", command= lambda: saveSettings(rpcVar, volumeValue, settingsData))
    saveButton.place(x=15, y=165)

#----------------------------------



# Define app
#----------------------------------

launcherapp = tkinter.Tk()
launcherapp.geometry("700x400")
launcherapp.title("refl3x")
launcherapp.minsize(700,400)
launcherapp.maxsize(700,400)
if sys.platform == "win32":
    launcherapp.iconbitmap("src/crosshairIcon.ico")
launcherapp.config(bg="#632C6D")


#------------------------------------


# Left side
#-------------------------------------

titleFont = font.Font(family='Consolas', size=28)


FramePanel = tkinter.Frame(launcherapp, borderwidth=0, background="#191919")
FramePanel.pack(side=tkinter.LEFT)
FramePanel.place(x=0, y=0, width=220, height=400)

titleLabel = tkinter.Label(launcherapp, text="refl3x", fg="green", background="#191919")
titleLabel.place(x=45, y=5)
titleLabel['font'] = titleFont

easyMode = tkinter.Button(launcherapp, text="Easy Mode", fg="black", bg="green", command=startEasy)
easyMode.place(x=70, y=110)

mediumMode = tkinter.Button(launcherapp, text="Medium Mode", fg="black", bg="orange", borderwidth=0, command=startMedium)
mediumMode.place(x=60, y=170)

hardMode = tkinter.Button(launcherapp, text="Hard Mode", fg="black", bg="red", borderwidth=0, command=startHard)
hardMode.place(x=70, y=230)

settingsButton = tkinter.Button(launcherapp, text="Settings", fg="black", bg="white", command=settingsWindow)
settingsButton.place(x=80, y=330)

creditLabel = tkinter.Label(launcherapp, text="by akira :)", fg="white", bg="#191919")
creditLabel.place(x=77, y=370)

#-------------------------------------


# Right side
#-------------------------------------
welcomeFont = font.Font(family="Consolas", size=18)
prezFont = font.Font(family="Consolas", size=13)
tipsFont = font.Font(family="Consolas", size=9)

welcomeLabel = tkinter.Label(launcherapp, text="Welcome in the refl3x program.", fg="white", bg="#632C6D")
welcomeLabel.place(x=255, y=15)
welcomeLabel['font'] = welcomeFont

textLabel = tkinter.Label(launcherapp, text="Play. Press. Become faster.", fg='red', bg="#632C6D")
textLabel.place(x=330, y=80)
textLabel['font'] = prezFont

logoImage = tkinter.PhotoImage(file="src/crosshairPurpleBg.png")
logoBg = tkinter.Label(launcherapp,image=logoImage, borderwidth=0)
logoBg.place(x=360, y=128)

tipsLabel = tkinter.Label(launcherapp, text="Tips : U can modify the ingame's background by changing\n 'gameBackground.png' in src folder. Same for the click sound !", fg="white", bg="#632C6D")
tipsLabel.place(x=238, y=350)
tipsLabel['font'] = tipsFont


#-------------------------------------


settingsfiles = open("data/settings.yaml", "r")
settingsData = yaml.safe_load(settingsfiles)
settingsfiles.close()

if settingsData["rpc"] == 1:

    client_id = '1012394653196230737' 
    rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)
    start_time = time.mktime(time.localtime())

    activity = {
        "timestamps": {
                "start": start_time
            },
        "assets": {
            "large_image": "refl3xlogo" 
        },
        "buttons" : [{"label" : "github", "url" : "https://github.com/akira-trinity/refl3x"}]
    }
    rpc_obj.set_activity(activity)


launcherapp.mainloop()