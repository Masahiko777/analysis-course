# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 18:13:51 2020
複数のグラフを1枚に表示する
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
    x, c, s, t = create_toy_data_01(-np.pi, np.pi, 100)

    #Vacant list for animation
    ims = []

    #create figure window
    fig = plt.figure(figsize=(20, 10), facecolor='w')
    plt.subplots_adjust(wspace=0.4, hspace=0.4)
    plt.rcParams['font.size'] = 20
    plt.rcParams['font.family'] ='sans-serif'
    
    plt.subplot(221)
    plt.plot(x, c, label='cos')
    plt.plot(x, s, label='sin')
    plt.plot(x, t, label='-tanh')
    plt.xlabel('x [-]')
    plt.ylabel('Value [-]')
    plt.grid(linestyle='--')
    plt.title('Case-1')
    
    plt.subplot(222)
    plt.plot(x, c, 'k--', lw=1.5, alpha=0.6, label='cos')
    plt.plot(x, s, 'b:', lw=3.0, label='sin')
    plt.plot(x, t, 'g-', label='-tanh')
    plt.xlabel('x [-]', fontsize=20, color='black')
    plt.ylabel('Value [-]', fontsize=20, color='black')
    plt.grid(linestyle='--', lw=1, alpha=0.4, color='lightgray')
    plt.tick_params(direction='in', length=6, width=2, color='gray')
    lg=plt.legend(loc='upper left',fontsize=10,title='Function')
    lg.get_title().set_fontsize(10)
    plt.title('Case-2',loc='left',fontsize=20)
    
    plt.subplot(223)
    im = plt.plot(x, c, 'k--', lw=1.5, alpha=0.6, label='cos')
    im = plt.plot(x, s, 'b:', lw=3.0, label='sin')
    im = plt.plot(x, t, 'g-', label='-tanh')
    plt.xlabel('x [-]', fontsize=20, color='black')
    plt.ylabel('Value [-]', fontsize=20, color='black')
    plt.grid(linestyle='--', lw=1, alpha=0.4, color='lightgray')
    plt.tick_params(direction='in', length=6, width=2, color='gray')
    lg=plt.legend(loc='upper left',fontsize=10,title='Function')
    lg.get_title().set_fontsize(10)
    plt.title('Case-2',loc='left',fontsize=20)
    
    for i in range(0,99,2):
        im =plt.plot(x[i], c[i], 'o', x[i], s[i], 'o', x[i], t[i], 'o', color="r", markersize=10, lw=1.5, alpha=0.6)
        ims.append(im)        
        #save series plot file
        #fnameF = 'ml_01/%03.f'%(i)+'.png'
        #plt.savefig(fnameF, dpi=200, bbox_inches="tight", pad_inches=0.1)
    
    #create animation
    ani = animation.ArtistAnimation(fig, ims)
    #save plot file
    fnameF = 'fig_01.png'
    plt.savefig(fnameF, dpi=200, bbox_inches="tight", pad_inches=0.1)
    
    plt.show()
    
if __name__ == '__main__':
    main()