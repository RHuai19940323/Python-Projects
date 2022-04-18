#!/usr/bin/env python
# coding: utf-8

# In[7]:


from PIL import Image
import glob
import os
import numpy as np
from random import randint
import time
import pygame

square_pngs = []
bg_pngs = []
circle_pngs = []
number_pngs = []
folder_num = len(glob.glob("source(png)/number/*"))
png_num = len(glob.glob("source(png)/number/01/*.png"))

for i in range(0, folder_num):
    square_pngs.append([])
    bg_pngs.append([])
    circle_pngs.append([])
    number_pngs.append([])
    for j in range(0, png_num):
        square_pngs[i].append(pygame.image.load(f"source(png)\\square\\0{i+1}\\0{j+1}.png"))
        bg_pngs[i].append(pygame.image.load(f"source(png)\\bg\\0{i+1}\\0{j+1}.png"))
        circle_pngs[i].append((pygame.image.load(f"source(png)\\circle\\0{i+1}\\0{j+1}.png")))
        number_pngs[i].append((pygame.image.load(f"source(png)\\number\\0{i+1}\\0{j+1}.png")))

def make_gif():
    gifs = []
    pngs = glob.glob(r"screenshot\*.png")
    random_char = "ABCDEFGHIJKLMNOPQRSTUVWKYZabcdefghijklmnopqrstuvwxyz0123456789"
    i, j = 0, 4
    while j <= len(pngs):
        frames = []
        filerange = list(range(i, j))
        for file in filerange:
            new_frame = Image.open(pngs[file])
            frames.append(new_frame)
        filerange.reverse()
        for fileR in filerange:
            new_frame = Image.open(pngs[fileR])
            frames.append(new_frame)
        gifs.append(frames)
        i += 4
        j += 4

    for m in range(0, len(gifs)):
        filename = ""
        for n in range(1, 24):
            r = randint(0, len(random_char)-1)
            filename += random_char[r]
        if len(gifs[m]) == 8:
            gifs[m][0].save(f"gifs\\{filename}.gif", format = "GIF",
                           append_images = gifs[m][1:],
                           save_all = True,
                           duration = 100, loop = 0)

window = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Paste PNG And Turn Into GIF")

FPS = 60

def main():
    savingNum = 1
    frameNum = 1
    shuffle = list(range(1, 5))
    for i in range(0, len(shuffle)):
        shuffle[i] = randint(0, png_num-1)
        
    clock = pygame.time.Clock()
    run = True
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        window.fill((0, 0, 0, 0))
        window.blit(square_pngs[frameNum-1][shuffle[0]], (0, 0))
        window.blit(bg_pngs[frameNum-1][shuffle[1]], (0, 0))
        window.blit(circle_pngs[frameNum-1][shuffle[2]], (0, 0))
        window.blit(number_pngs[frameNum-1][shuffle[3]], (0, 0))
        pygame.display.update()
        pygame.image.save(window, f"screenshot\\{savingNum}.png")
        time.sleep(1)
        savingNum += 1
        frameNum += 1
        if frameNum == 5:
            for i in range(0, len(shuffle)):
                shuffle[i] = randint(0, png_num-1)
            frameNum = 1
            make_gif()
            savingNum = 1
    pygame.quit()

if __name__=="__main__":
    main()

