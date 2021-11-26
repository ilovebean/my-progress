import sys
import time

import pygame
from pygame.locals import *


def main():
    pygame.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    green_1 = (55, 138, 80)

    screen.fill(green_1)

    x, y = screen.get_size()
    counterx = x
    countery = y

    print(x, y)  # debug

    mouse_x, mouse_y = pygame.mouse.get_pos()
    counterx1 = mouse_x
    countery1 = mouse_y

    print(counterx1, countery1)

    background = pygame.image.load(r"assets/UI/menu_background.png")  # background
    start_button = pygame.image.load(r"assets/UI/Start_button.png")  # start Button
    start_button_resize = start_button.copy()  # start Button Resized
    hovered_start_button = pygame.image.load(r"assets/UI/Start_button_hover.png")  # start Button hover
    exit_button = pygame.image.load(r"assets/UI/exit_button.png")  # exit button
    title = pygame.image.load(r"assets/UI/Title.png")  # Title
    icon = pygame.image.load(r"assets/icons/16.png")  # Icon

    size = (x, y)
    image = pygame.transform.scale(background, size)

    pygame.display.set_icon(icon)

    while True:
        x, y = screen.get_size()
        if x != counterx:
            counterx = x
            size = (x, y)
            image = pygame.transform.scale(background, size)

        if y != countery:
            countery = y
            size = (x, y)
            image = pygame.transform.scale(background, size)

        mouse_x, mouse_y = pygame.mouse.get_pos()  # Hover effects

        start_x_1 = (counterx / 4)
        start_x_2 = (start_x_1 + (counterx / 4))
        start_y_1 = ((countery / 5) * 3)
        start_y_2 = (start_y_1 + (countery / 8))

        exit_x_1 = (x - counterx / 16)
        exit_x_2 = (x)
        exit_y_1 = (0)
        exit_y_2 = (0 + (counterx / 16))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x2, y2 = pygame.mouse.get_pos()
                if exit_x_1 < x2 < exit_x_2:
                    if exit_y_1 < y2 < exit_y_2:
                        pygame.quit()
                        sys.exit()
                if start_x_1 < mouse_x < start_x_2:
                    if start_y_1 < mouse_y < start_y_2:
                        pygame.quit()

                        time.sleep(1)

        if start_x_1 < mouse_x < start_x_2:
            if start_y_1 < mouse_y < start_y_2:
                start_button = hovered_start_button
            else:
                start_button = start_button_resize
        else:
            start_button = start_button_resize

        scaled_start_button = pygame.transform.scale(start_button,
                                        ((counterx / 4), (countery / 8)))  # Constantly updates the size of the button
        scaled_exit_button = pygame.transform.scale(exit_button, ((counterx / 16), (counterx / 16)))
        scaled_title = pygame.transform.scale(title, (((counterx * 3) / 4), ((countery / 7) * 3)))

        
        screen.blit(image, (0, 0))  # Background
        screen.blit(scaled_start_button, ((counterx / 4), ((countery / 5) * 3)))  # start button pos
        screen.blit(scaled_exit_button, ((x - counterx / 16), 0))
        screen.blit(scaled_title, (0, 0))
        pygame.display.update()


if __name__ == '__main__':
    main()
