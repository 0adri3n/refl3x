# IMPORTS
#---------------------------------------------------

import tkinter
import tkinter.font as font
from PIL import Image, ImageTk
from lib import gameEasyMode, gameMediumMode, gameHardMode, rpc
import sys
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

creditLabel = tkinter.Label(launcherapp, text="by akira :)", fg="white", bg="#191919")
creditLabel.place(x=85, y=370)

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
