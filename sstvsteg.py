#!/usr/bin/python3

from PIL import Image,ImageDraw,ImageFont
from random import randint
from os import system

def makesound(file,name):
    if ".wav" not in name:
        name += ".wav"

    system("python3 -m pysstv {} {} > /dev/null".format(file,name))
    system("rm -rf "+file)


def makepicture(chars,lines,text,soundname,fontsize):
    cols = (((chars+2) * 8) + 320)
    rows = ((((lines+2) * 8) * 2) + 256) 
    img = Image.new('RGB',(cols,rows),color = (0,0,0))
    fnt = ImageFont.truetype("Hack-Bold.ttf",fontsize)
    d = ImageDraw.Draw(img)
    d.text((10,10),text,font=fnt,fill=(255,255,0))
    filename = str(randint(1000,9999))
    img.save(filename + ".jpg")
    makesound(filename+".jpg",soundname)

textfile = input("Text File  : ")
soundname = input("Output FileName : ")

fontsize = input("Font Size (default -> 15) : ")
if fontsize == "":
    fontsize = 15
else:
    fontsize = int(fontsize)
text = open(textfile)
text = text.readlines()

#for i in range(len(text)):
#    if text[i].strip("\n") != "":
#        text[i] = text[i].strip("\n")
chars = len(max(text))
lines = len(text)
txt = ""
for i in text:
    txt += i

makepicture(chars,lines,txt,soundname,fontsize)

    


