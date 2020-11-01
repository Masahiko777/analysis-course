# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:59:39 2020
グラフをつくる
@author: yamazaki
"""
import numpy as np
import matplotlib.pyplot as plt

def create_toy_data_01(mi, ma, div):
    x = np.linspace(mi, ma, div, endpoint=True)
    c, s, t = np.cos(x), 3*np.sin(x), -np.tanh(x)
    return x, c, s, t

def main():
    print("Hello World!!!!!")
    #calculate toy data
    x, c, s, t = create_toy_data_01(-2*np.pi, 2*np.pi, 100)
    
    #create figure window
    fig = plt.figure(figsize=(12, 8), facecolor='w')
    plt.rcParams['font.size'] = 22
    plt.rcParams['font.family'] ='Arial'
    
    plt.plot(x, c, 'k--',lw = 1.5,label='cos')
    plt.plot(x, s, 'b:',lw =5.0,label='sin')
    plt.plot(x, t, 'g-',lw = 1.5,alpha = 0.3,label='-tanh')
    
    plt.xlabel('x [-]', fontsize=22, color='black')
    plt.ylabel('Value [-]', fontsize=22, color='black')
    plt.grid(linestyle='--', lw=1, alpha=0.4, color='lightgray')
    plt.tick_params(direction='in', length=6, width=2, color='gray')
    lg=plt.legend(loc='upper left',fontsize=20)
    lg.get_title().set_fontsize(12)
    plt.tight_layout()
    plt.savefig('figname.png', transparent=True, dpi=300)
    plt.show()

if __name__=='__main__':
    main()

