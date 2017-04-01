#!/usr/bin/env python

from os.path import isfile,join,isdir
import numpy as np
import cv2
from PIL import Image
from os import listdir
from os.path import isfile,join,isdir
import os
import time
import shutil
from image_match.goldberg import ImageSignature
import sys

caliberate_path=os.getcwd()+'/caliberate'
output_path= os.getcwd()+ '/output'

class MyException(Exception):
    pass

def chk_file():
    if isdir(caliberate_path):
        if isfile(cal_file):
            ls=[]
            with open(cal_file, "r") as f:
                ls=[tuple(map(int,i.strip().split(' '))) for i in f]
            if(len(ls)==4):
                return ls
            else:
                raise MyException("Please run Caliberate.py|file incompelete")
        else:
            raise MyException("Please run Caliberate.py|file don't exist")
    else:
        raise MyException("Please run Caliberate.py|folder dosen't exist")


def capture_input_image():
    if (isdir(output_path)):
        shutil.rmtree(output_path)
    os.mkdir(output_path)

    if (isfile(output_path+'output.jpg')):
        os.remove(output_path+'output.jpg')
    time.sleep(1)
    print("taking sample")
    time.sleep(1)
    cam =cv2.VideoCapture(1) #####video capture######
    s,im=cam.read()
    cv2.imwrite(os.path.join(output_path,'output.jpg'), im)
    cam.release()


os.chdir(caliberate_path)

gis = ImageSignature()

caliberate_files=["cal10.jpg","cal100.jpg","cal500.jpg","cal2000.jpg"]

signature_values=[]
for x in range(4):
    signature_values.append(cv2.imread(caliberate_files[x]))
    signature_values[x]=gis.generate_signature(signature_values[x])


raw_input("Hit ENTER key")
cam =cv2.VideoCapture(1)
s,im = cam.read()
cv2.imwrite('output.jpg', im)
cam_out= cv2.imread("output.jpg")

cam_out = gis.generate_signature(cam_out)

distance_values=[]
for x in range(4):
    distance_values.append(gis.normalized_distance(cam_out, signature_values[x]))

minv =10.000000
for x in range(4):
    if distance_values[x]<minv:
        minv=distance_values[x]
        min_d= x

if min_d==0:
    print("10 rs :%f"%distance_values[0])
elif min_d==1:
    print("100 rs :%f"%distance_values[1])
elif min_d==2:
    print("500 rs :%f"%distance_values[2])
elif min_d==3:
    print("2000 rs :%f"%distance_values[3])    

print("    ")

print (distance_values)







    			


      
