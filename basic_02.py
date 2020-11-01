# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 16:27:02 2020
動画をgifで保存する
@author: stero
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_toy_data_01(mi, ma, div):
    x = np.linspace(mi, ma, div, endpoint=True)
    c, s, t = np.cos(x), np.sin(x), -np.tanh(x)
    return x, c, s, t

def main():
    print("Hello World!!!!!")
    #calculate toy data
    x, c, s, t = create_toy_data_01(-2*np.pi, 2*np.pi, 100)
    
    ims = []
    #create figure window
    fig = plt.figure(figsize=(12, 8), facecolor='w')
    fig.add_subplot(111)
    plt.rcParams['font.size'] = 22
    plt.rcParams['font.family'] ='Arial'
    
    im = plt.plot(x, c, 'k--',lw = 1.5,label='cos')
    im = plt.plot(x, s, 'b:',lw =5.0,label='sin')
    im = plt.plot(x, t, 'g-',lw = 1.5,alpha = 0.3,label='-tanh')
    plt.xlabel('x [-]', fontsize=22, color='black')
    plt.ylabel('Value [-]', fontsize=22, color='black')
    plt.grid(linestyle='--', lw=1, alpha=0.4, color='lightgray')
    plt.tick_params(direction='in', length=6, width=2, color='gray')
    lg=plt.legend(loc='upper left',fontsize=20)
    lg.get_title().set_fontsize(12)
    plt.tight_layout()
    for i in range(0,99,2):
        im =plt.plot(x[i], c[i], 'o', x[i], s[i], 'o', x[i], t[i], 'o', color="r", markersize=10, lw=1.5, alpha=0.6)
        ims.append(im)
    
    ani = animation.ArtistAnimation(fig, ims, interval = 100)
    ani.save('sample.gif', writer='pillow')
    plt.show()

if __name__=='__main__':
    main()