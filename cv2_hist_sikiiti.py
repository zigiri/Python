# -*- coding: utf-8 -*-
"""
Created on Tue May 29 20:36:15 2018

@author:yamada
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():
    img = cv2.imread("sample4.jpg") #ここのファイルがヒストグラムを求めたい画像
    
    hist, bins = np.histogram(img.ravel(),256,[0,256])
    bins = bins[:-1]
    
    #頻度値の計算
    cumsum = np.cumsum(hist)
    
    #閾値求める
    p = 0.75 #対象物体が画像に占める割合
    for i in range(0, 256):
        pcent = cumsum[i] / cumsum[-1]
        if pcent > p:
            break
    
    
    print("percentile:", i) #閾値を表示

    # グラフ    
    plt.xlim(0, 255)
    plt.plot(hist)
    plt.xlabel("brightness value", fontsize=15)
    plt.ylabel("Number of pixels", fontsize=15)
    plt.grid()
    plt.show()
    
    #頻度値のグラフ
    plt.plot(bins, cumsum)
    plt.xlabel("Brightness Integration", fontsize=15)
    plt.ylabel("cumulative sum", fontsize=15)
    plt.annotate("percentile:{}".format(i), xy=(i,20), xytext=(i, 0),
                 arrowprops=dict(shrink=0.9))
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
    