from random import choice
from PIL import Image
import os

COLOURS = [0,255]


while True:
    folder = input("Enter folder name: ")

    victimFolder = os.fsencode(folder)

    for file in os.listdir(victimFolder):
        filename = os.fsdecode(file)
        if filename.endswith(".png"):
            img = Image.open(f"{folder}/{filename}")
            map = img.load()
            newImg = Image.new(img.mode,img.size)
            for i in range(newImg.size[0]):
                for j in range(newImg.size[1]):
                    try:
                        if map[i,j][3] == 255:
                            newImg.putpixel((i,j),(choice(COLOURS),choice(COLOURS),choice(COLOURS),255))
                    except:
                        continue
            print(f"{folder}/{filename}")
            newImg.save(f"{folder}/{filename}")
    print("Complete")