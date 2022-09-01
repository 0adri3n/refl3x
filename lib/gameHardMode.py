import pygame
import time
import random
from pygame.locals import *
import sys
import statistics
import yaml

def hardGame():


    WHITE = (255, 255, 255)
    BLUE = (  0,   0, 255)
    GREEN = (  0, 255,   0)
    RED = (255,   0,   0)
    BLACK = (0, 0, 0)
    YELLOW = (204, 102, 0)
    PURPLE = (255, 51, 255)
    CYAN = (153, 255, 255)


    pygame.init()
    pygame.mixer.init() 

    gameWin = pygame.display.set_mode((1000,600))

    winIcon = pygame.image.load("src/crosshair.png").convert()
    pygame.display.set_icon(winIcon)
    pygame.display.set_caption("refl3x")


    winBg = pygame.image.load("src/gameBackground.png").convert()
    winBg = pygame.transform.scale(winBg, (1000, 600))

    pygame.font.init()
    my_font = pygame.font.SysFont('consolas', 15)

    clicksound = pygame.mixer.Sound('src/clicksound.mp3')
    settingsfiles = open("data/settings.yaml", "r")
    settingsData = yaml.safe_load(settingsfiles)
    settingsfiles.close()
    clicksound.set_volume(float(settingsData["volume"]))

    
    inGame = True
    playing = True


    reactionTimeList = []
    wrongKey = 0


    while inGame:


        gameWin.blit(winBg, (0,0))
        text_surface = my_font.render('PRESS S TO START', False, (0, 0, 0))
        gameWin.blit(text_surface, (0, 0))
        pygame.display.flip()

        notpressed = True
        while notpressed:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_s:
                    notpressed = False
                    pygame.time.delay(3 * 1000)
                if event.type == pygame.QUIT:
                    pygame.quit()

        gameWin.blit(winBg, (0,0))
        text_surface = my_font.render('Green = Z | Blue = Q | Red = S | White = D | Black = A | Orange = E | Purple = P | Cyan = L', False, (0, 0, 0))
        gameWin.blit(text_surface, (0, 0))
        pygame.display.flip()


        for i in range(50):

            x = random.randint(20, 980)

            y = random.randint(20, 580)

            colorlist = [(GREEN, K_z), (BLUE, K_q), (RED, K_s), (WHITE, K_d), (BLACK, K_a), (YELLOW, K_e), (PURPLE, K_p), (CYAN, K_l)]
            
            choosenCombo = random.choice(colorlist)
            choosencolor = choosenCombo[0]
            goodKey = choosenCombo[1]

            pygame.draw.circle(gameWin, choosencolor, (x,y), 20, 20)
            pygame.display.flip()

            start = time.time()

            notpressed = True
            while notpressed:
                for event in pygame.event.get():
                    if event.type == KEYDOWN and event.key == goodKey:
                        clicksound.play()
                        notpressed = False
                        reactionTimeList.append(time.time() - start)
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == KEYDOWN and event.key != goodKey:
                        wrongKey += 1
            
            gameWin.blit(winBg, (0,0))
            text_surface = my_font.render('Green = Z | Blue = Q | Red = S | White = D | Black = A | Orange = E | Purple = P | Cyan = L | ' + str(i+1) + '/50', False, (0, 0, 0))
            gameWin.blit(text_surface, (0, 0))
            pygame.display.flip()


        pygame.display.flip()   

        gameWin.blit(winBg, (0,0))

        finishedtext = my_font.render('Session finished ! ', False, WHITE)
        gameWin.blit(finishedtext, (375, 50))

        wrongText = my_font.render('Time you pressed a wrong key : ' + str(wrongKey) + '', False, WHITE)
        gameWin.blit(wrongText, (250, 100))

        averageReactTime = statistics.fmean(reactionTimeList)
        averageReactTime = '%.3f'%averageReactTime
        timetext = my_font.render('Average reaction Time : ' + str(averageReactTime) + ' seconds', False, WHITE)
        gameWin.blit(timetext, (250, 150))

        bestscorefile = open("data/bestscore.yaml", "r")
        bestscoreData = yaml.safe_load(bestscorefile)
        bestscorefile.close()
        
        if float(bestscoreData['hardMode']) > float(averageReactTime):
            newscoretext = my_font.render('Brand new record !!! gg sir :)', False, RED)
            gameWin.blit(newscoretext, (250, 200))
            bestscoreData['hardMode'] = float(averageReactTime)
            bestscorefileWrite = open("data/bestscore.yaml", "w")
            bestscorefileWrite.write(yaml.dump(bestscoreData, default_flow_style=False))
            bestscorefileWrite.close()

        pygame.display.flip()

        closed = False
        while not closed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

