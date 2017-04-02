#!/usr/bin/bash

import Tkinter as tk
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
import tkMessageBox
import Image
from PIL import ImageTk

caliberate_path=os.getcwd()+'/caliberate'
output_path= os.getcwd()+ '/output'

def detect_callback():	
	os.chdir(caliberate_path)
	gis = ImageSignature()

	caliberate_files=["cal10.jpg","cal100.jpg","cal500.jpg","cal2000.jpg"]
	signature_values=[]

	for x in range(4):
	    signature_values.append(cv2.imread(caliberate_files[x]))
	    signature_values[x]=gis.generate_signature(signature_values[x])

	cam =cv2.VideoCapture(0)
	s,im = cam.read()
	cv2.imwrite('output.jpg', im)
	cam_out= cv2.imread("output.jpg")

	img = ImageTk.PhotoImage(Image.open(caliberate_path+'/'+'output.jpg'))
	panel = tk.Label(root, image = img)
	panel.pack(side = "bottom", fill = "both", expand = "yes")

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
			return_string = ("Rs 10 ")
	elif min_d==1:
		    return_string = ("Rs 100")
	elif min_d==2:
		    return_string = ("Rs 500")
	elif min_d==3:
			return_string = ("Rs 2000")        

	tkMessageBox.showinfo("DETECTION ALERT!", return_string)		


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


root = tk.Tk()  
root.title("currency detector")
root.geometry('700x500')
w = tk.Button(root,text ="Detect", command = detect_callback)
w.pack()


#Results.grid(row = 1, column = 1)
'''img = ImageTk.PhotoImage(Image.open(caliberate_path+'/'+'output.jpg'))
panel = tk.Label(master, image = img) '''
#panel.pack(side = "bottom", fill = "both", expand = "yes")
tk.mainloop()