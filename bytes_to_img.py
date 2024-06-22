import cv2
import numpy as np
 
image = open('violao.txt','r').read().split(",")

lst = []

h = 96
w = 128

for i in range(h):
    lst_=[]
    for j in range(w):
        try:
            lst_.append([image[i*w+j]])
        except Exception as e:
            print(e,"-",i,":",j)
    lst.append(lst_.copy())

image = np.asarray(lst, dtype=np.uint8)

cv2.imshow("violao.jpg",image)
cv2.imwrite("violao.jpg",image)
cv2.waitKey()