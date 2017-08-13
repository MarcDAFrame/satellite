import cv2
import numpy as np



def check_if_real(file_name):

    img = cv2.imread(file_name)
    BAD_COLOR_AVG = (223,226)

    #print(img)

    avg1 = np.average(img, axis=0)
    avg = np.average(avg1)

    if (BAD_COLOR_AVG[0]  < avg and avg < BAD_COLOR_AVG[1]):
        print(avg)


