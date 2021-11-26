import pygame
import sys
from pygame.locals import *
from Engine.UserInterface import Button
import time

def main():
    pygame.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    green_1 = (55, 138, 80, 0.8)

    screen.fill(green_1)

    x, y = screen.get_size()
    counterx = x
    countery = y
        
    print(x,y)#debug

    x1, y1 = pygame.mouse.get_pos()
    counterx1 = x1
    countery1 = y1

    print(counterx1, countery1)

    image_1 = pygame.image.load(r"assets/UI/menu_background.png")#background
    image_2 = pygame.image.load(r"assets/UI/Start_button.png")#start Button
    image_2_2 = pygame.image.load(r"assets/UI/Start_button.png")#start Button
    image_3 = pygame.image.load(r"assets/UI/Start_button_hover.png")#start Button hover
    image_4 = pygame.image.load(r"assets/UI/exit_button.png")#exit button
    image_5 = pygame.image.load(r"assets/UI/Title.png")#Title
    image_6 = pygame.image.load(r"assets/icons/16.png")

    size = (x, y)
    image = pygame.transform.scale(image_1, size)
    
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit() 

        x, y = screen.get_size()
        if x != counterx:
            counterx = x
            size = (x,y)
            image = pygame.transform.scale(image_1, size)
        
        if y != countery:
            countery = y
            size = (x,y)
            image = pygame.transform.scale(image_1, size)

        x1, y1 = pygame.mouse.get_pos()#Hover effects

        start_x_1 = (counterx/4)
        start_x_2 = (start_x_1 + (counterx/4))
        start_y_1 = ((countery/5)*3)
        start_y_2 = (start_y_1 + (countery/8))

        exit_x_1 = ((x - counterx/16))
        exit_x_2 = (x)
        exit_y_1 = (0)
        exit_y_2 = (0 + (counterx/16))

        if start_x_1<x1<start_x_2:
            if start_y_1<y1<start_y_2:
                image_2 = image_3
            else:
                image_2 = image_2_2
        else:
            image_2 = image_2_2

        if event.type == pygame.MOUSEBUTTONDOWN:
            x2, y2 = pygame.mouse.get_pos()
            if exit_x_1< x2< exit_x_2:
                if exit_y_1<y2<exit_y_2:
                    pygame.quit()
                    sys.exit()
            if start_x_1<x1<start_x_2:
                if start_y_1<y1<start_y_2:
                    pygame.quit()
                    import LevelSelect

                    time.sleep(1)

        image1 = pygame.transform.scale(image_2, ((counterx/4), (countery/8)))  #Constantly updates the size of the button
        image2 = pygame.transform.scale(image_4, ((counterx/16), (counterx/16)))
        image3 = pygame.transform.scale(image_5, (((counterx * 3)/4), ((countery/7)*3)))

        pygame.display.set_icon(image_6)
        screen.blit(image, [0, 0])#Background
        screen.blit(image1, ((counterx/4), ((countery/5)*3)))#start button pos
        screen.blit(image2, (((x - counterx/16)), (0)))
        screen.blit(image3, (0,0))
        pygame.display.update()
            
if __name__ == '__main__':
    main()