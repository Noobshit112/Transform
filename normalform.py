# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 18:18:31 2017

@author: Admin
"""
import pandas as pd

def trans(frame,x1='x1',x2='x2',y='y'):
    listt = []
    le = len(frame.columns)
    for i in range(0,len(frame.index)):
        for j in range(0,le):
            #outt.append([frame.index[i],frame.columns[j],str(frame[(frame.index == frame.index[i])][frame.columns[j]])]) 
            listt.append([frame.index[i],frame.columns[j],float(frame.iloc[i][frame.columns[j]])])
    outt = pd.DataFrame(listt,columns = [x1,x2,y])
    return outt
'''
frame1 = pd.DataFrame(pd.read_excel('GDPpercapitaconstant2000US.xlsx'))   
frame2 = trans(frame = frame1.set_index('Country'))
print(frame2[frame2['x1'] == 'Algeria'])
'''    
    
    