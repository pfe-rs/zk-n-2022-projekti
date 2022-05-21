import numpy as np
import cv2
from math import sqrt

img = cv2.imread("sample.jpg")
h, w, c = img.shape

grayscale = np.zeros((h, w))
angles = np.zeros((h, w))
new_img = np.zeros((h, w))

horizontal_grid = [[-1, 0, 1],
                [-2, 0, 2],
                [-1, 0, 1]]

vertical_grid = [[1, 2, 1],
                [0, 0, 0],
                [-1, -2, -1]]

gauss_grid = [[1/16, 1/8, 1/16],
            [1/8, 1/4, 1/8],
            [1/16, 1/8, 1/16]]

def step0():
    for x in range(h):
        for y in range(w):
            grayscale[x][y] = int(0.299 * img[x][y][0] + 0.587 * img[x][y][1] + 0.114 * img[x][y][2])
    cv2.imwrite("pre-gauss.png", grayscale)

def step1():
    tmp = np.zeros((3, 3))
    tmp2 = np.zeros((3, 3))
    for x in range(h):
        for y in range(w):
            if (y > 0 and y < w - 1 and x > 0 and x < h - 1):
                for i in range(3):
                    for j in range(3):
                        tmp[i][j] = grayscale[x + (i - 1)][y + (j - 1)] * gauss_grid[i][j]
                        tmp2[i][j] = grayscale[x + (i - 1)][y + (j - 1)] * gauss_grid[i][j]
                gx = 0
                gy = 0
                for i in tmp:
                    gx += sum(i) / 1.1
                for i in tmp2:
                    gy += sum(i) / 1.1
                new_img[x][y] = sqrt(gx*gx + gy*gy)
    cv2.imwrite("gauss.png", new_img)

def step2():
    tmp = np.zeros((3, 3))
    tmp2 = np.zeros((3, 3))
    for x in range(h):
        for y in range(w):
            # uglovi => y = 0, y = w-1, x = 0, x = h-1
            if (y != 0 and y != w - 1 and x != 0 and x != h - 1):
                for i in range(3):
                    for j in range(3):
                        tmp[i][j] = grayscale[x + (i - 1)][y + (j - 1)] * horizontal_grid[i][j]
                        tmp2[i][j] = grayscale[x + (i - 1)][y + (j - 1)] * vertical_grid[i][j]
                gx = 0
                gy = 0
                for i in tmp:
                    gx += sum(i) #// 256
                for i in tmp2:
                    gy += sum(i) #// 256
                new_img[x][y] = sqrt(gx*gx + gy*gy)
                angles[x][y] = np.arctan(gy/gx)
    cv2.imwrite("edges.png", new_img)


step0()
step1()
step2()
# step3()