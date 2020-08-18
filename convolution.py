import cv2 as cv
import numpy as np
import math
img = cv.imread('C:/Users/molg/Desktop/res.jpeg')

x = np.ndarray(shape=(img.shape[0],img.shape[1]),dtype=int)
x.fill(0)

filtre =[[1,0,1],[1,0,1],[1,0,1]]
seek=2
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

xRow=0
xColumn =0
def calculateConv(pointOne,pointTwo):
    global xRow
    global xColumn
    global x
   # print(pointOne,pointTwo)
    counterX=0
    counterY=0
    for row in range(pointOne[0],pointTwo[0]+1):
        for column in range(pointOne[1],pointTwo[1]+1):
            x[xRow][xColumn] = (filtre[counterX][counterY]*img[row][column])+x[xRow][xColumn]
            counterY=counterY+1
        counterX=counterX+1
        counterY=0
    xColumn=xColumn+1
    if(xColumn==img.shape[1]-2):
        xColumn=0
        xRow=xRow+1
    if(xRow==img.shape[0]-2):
        print('tamamdır..',xRow,xColumn)
       # print(x)
        x=x.astype(np.uint8)
        cv.imshow('result',x)
        cv.waitKey(0)


for rowm in range(0,img.shape[0]-2):
    for columnm in range(0,img.shape[1]-2):
        calculateConv((rowm,columnm),(rowm+seek,columnm+seek))
        if(columnm+(seek+1)>=img.shape[1]):
            break
    if(rowm+(seek+1)>=img.shape[0]):
        break

    


