#!/usr/bin/env python

import cv2
import os
import time
import sys
import shutil
from PIL import Image
from os import listdir
from os.path import isfile,join,isdir

caliberate_path=os.getcwd()+'/caliberate'
def read_fold():
    files=[f for f in listdir(caliberate_path)]
    ls=[]
    for x in range(4):
        ls.append(caliberate_path+'/'+files[x])
        ls[x]=Image.open(ls[x])
        ls[x]=ls[x].resize((50,50))
        ls[x]=compute_avg_image_color(ls[x])
    return (ls)

def compute_avg_image_color(img):
    width,height=img.size

    r_total=0
    g_total=0
    b_total=0
    for x in range(0,width):
        for y in range(0,height):
            r,g,b=img.getpixel((x,y))
            r_total += r
            g_total += g
            b_total += b

    return(r_total,g_total,b_total)


def capture_images():
    if (isdir(caliberate_path)):
        shutil.rmtree(caliberate_path)
    os.mkdir(caliberate_path)
    os.chdir(caliberate_path)
    time.sleep(1)     
    a=raw_input("Hit ENTER key for Rs 10")
    cam_activate(10)
    a=raw_input("Hit ENTER key for Rs 100")
    cam_activate(100)
    a=raw_input("Hit ENTER key for Rs 500")
    cam_activate(500)
    a=raw_input("Hit ENTER key for Rs 2000")
    cam_activate(2000)

def cam_activate(x):
    cam =cv2.VideoCapture(sys.argv[0])
    s,im = cam.read()
    cv2.imwrite('cal%d.jpg'%x, im)
    cam.release()

capture_images()
a=read_fold()

with open(caliberate_path+'/cal_values.txt','w') as fp:
    for line in a:
        strs=" ".join(str(x) for x in line)
        fp.write(strs+"\n")

print(a)
