#!/usr/bin/env python3

import time
import pygame
import os
import json


black = (0,0,0) #Color for the output text

data = json.load(open("data.json")) #Loading the data from the json file
os.environ["SDL_VIDEO_CENTERED"] = "1" #Opens the window in the center of the screen

screen = pygame.display.set_mode((600, 800)) #Screen settings
pygame.display.set_caption("Morse Code") #Window caption

pygame.init() #This makes it work idk

img = pygame.image.load("morse_code.png") #Loadin the image and scailing it
img = pygame.transform.scale(img, (600, 800))

clock = pygame.time.Clock()

character = [] #The current character goes here
output_text = ""

running = True #This makes it not close immediatly
while running:
    screen.blit(img, (0, 0)) #Puts the image on the window

    font = pygame.font.SysFont(None, 45)   #Making the output text box
    output_label = font.render(output_text, True, black)
    screen.blit(output_label, [55, 675])

    pygame.display.update()

    for event in pygame.event.get(): #This is the main loop that gets all the key presses
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: #If ESCAPE is pressed, it closes the program
                running = False
                pygame.quit()
                break
            t_now = time.time()
        if event.type == pygame.KEYUP: #Writing the morse code
            if event.key == pygame.K_LCTRL: #If LCTRL is pressed, it ends the character
                for k, v in data.items():   # Creating the final text
                    if character == v:
                        output_text += k
                        pygame.display.update()
                character = []
            elif event.key == pygame.K_LSHIFT: #If LSHIFT is pressed, it adds a space
                output_text += "  "
            elif event.key == pygame.K_SPACE: #If SPACE is pressed, it types the character
                t = time.time() - t_now
                t = str(t)
                t = t[:5]
                if float(t) <= 0.5:
                    character.append("*")
                else:
                    character.append("-")
            elif event.key == pygame.K_BACKSPACE:
                output_text = output_text[:-1]
                pygame.display.update()

        clock.tick(60)