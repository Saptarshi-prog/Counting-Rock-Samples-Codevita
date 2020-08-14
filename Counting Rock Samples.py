# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 22:25:29 2020

@author: 91842
"""
samples, ranges = [int(i) for i in input().split()]
count = 0
final = []
arr = list(map(int,input().split()))

for i in range(0,ranges):
    min, max = [int(i) for i in input().split()]
    for j in range(0,samples):
        if min <= arr[j] <=max:
            count+=1
    final.append(count)
    count = 0
    
for i in range(0,len(final)):
    print(final[i], end = " ")
        
        
    
    
    