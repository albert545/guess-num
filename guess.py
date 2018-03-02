# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 16:15:25 2018

@author: albert-w10
"""

import random
start = input('起始值:')
end = input('結束值:')
start = int(start)
end = int(end)

r = random.randint(start,end)
t = 0

while True:
    t = t + 1
    num = input('請猜數字:')
    num = int(num)
    if num == r:
        print('你猜對了')
        print('你總共猜了:',t,'次')
        break
    elif num > r:
        print('比答案大')
    elif num < r:
        print('比答案小')
    print('這是您猜的第',t,'次')    
    
        
    
        