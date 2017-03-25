#import cv2
import numpy as np
from PIL import Image

def compute_average_image_color(img):
    width, height = img.size

    r_total = 0
    g_total = 0
    b_total = 0

    count = 0
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = img.getpixel((x,y))
            r_total += r
            g_total += g
            b_total += b
            count += 1

    img_colour=r_total, g_total, b_total
    return(img_colour)


img_cal = Image.open('caliberate.jpg')
img_cal = img_cal.resize((50,50))  # Small optimization
cal_color = compute_average_image_color(img_cal)

img_comp = Image.open('image_comp.jpg')
img_comp = img_comp.resize((50,50))
comp_color = compute_average_image_color(img_comp)
abc=10000,10000,10000

if (comp_color<tuple(np.add(cal_color, abc)) and comp_color>tuple(np.subtract(cal_color, abc))):
	print("detected")

print("prog finish")


    
'''cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    cv2.imshow('frame',frame)

    #if cv2.waitkey(0) & 0xFF == ord('q'):
    #   break

cap.release()
cv2.destroyAllWindows() ''' 