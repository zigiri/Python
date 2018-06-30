# -*- coding: utf-8 -*-
"""
Created on Tue May 29 20:36:15 2018

@author: b1016132　山田大貴
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt


def main():
    img = cv2.imread("miraidai.JPG") #ここのファイルがヒストグラムを求めたい画像
    
    hist, bins = np.histogram(img.ravel(),256,[0,256])

    # グラフ
    plt.xlim(0, 255)
    plt.plot(hist)
    plt.xlabel("brightness value", fontsize=15)
    plt.ylabel("Number of pixels", fontsize=15)
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
    