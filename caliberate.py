#!/usr/bin/python

import cv2
import os
import time
import sys
import shutil
from PIL import Image
from os import listdir
from os.path import isfile,join,isdir

caliberate_path=os.getcwd()+'/caliberate'


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
    time.sleep(1)
    cam =cv2.VideoCapture(1)
    s,im = cam.read()
    cv2.imwrite('cal%d.jpg'%x, im)
    cam.release()

capture_images()

print("done")
