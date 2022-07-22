# -*- coding: utf-8 -*-
"""
Created on Mon May 10 15:18:16 2021

@author: gucheng
"""

import csv
import matplotlib.pyplot as plt
import numpy as np

m_reg = 2
s_reg = 4
n_reg = 16
f_reg = 2
l_reg = 8
k_reg = 32

ilas_len = f_reg * k_reg * 4

fin = open(r'D:\projects\DIQUN\write\zhangchao\real50m.csv')
f_csv = csv.reader(fin)
data = []
for x in f_csv:
    data.append(x[0])
fin.close()

l_data = [[],[],[],[],[],[],[],[]]
for x in data:
    x = x.strip()
    tmp_data = x.split()
    for l_idx in range(0,l_reg):
        l_data[l_idx].append(tmp_data[l_idx][6:])
        l_data[l_idx].append(tmp_data[l_idx][4:6])
        l_data[l_idx].append(tmp_data[l_idx][2:4])
        l_data[l_idx].append(tmp_data[l_idx][0:2])

all_data = []
first_ilas_idx = []
first_data_idx = []

l_user_data = []

for l_idx in range(0,l_reg):
    for x in range(0,len(l_data[l_idx])):
        if l_data[l_idx][x] == 'bc' and l_data[l_idx][x+1] == '1c':
            first_ilas_idx.append(x+1)
            first_data_idx.append(x+1+ilas_len)

Lid = []
for l_idx in range(0,l_reg):
    LID = int(l_data[l_idx][first_ilas_idx[l_idx]+f_reg*k_reg+4],16)
    Lid.append(LID)
    print (LID)
        
        

data_num = []
for l_idx in range(0,l_reg):
    for x in range(0,8):
        if l_idx == Lid[x]:
            l_user_data.append(l_data[x][first_data_idx[x]:])
            data_num.append(len(l_user_data[l_idx]))

process_data_num = min(data_num)
all_idx = int(process_data_num/f_reg)
print (all_idx)
last_frame_octet = [0]*8
last_multi_frame_octet = [0]*8
for x in range(0,all_idx):
    for y in range(0,l_reg):
        for z in range(0,f_reg):
            idx = x*f_reg+z
            temp_data = l_user_data[y].pop(0)
            if x%k_reg == k_reg-1 and z == f_reg-1:
                if temp_data == '7c':
                    temp_data = last_frame_octet[y]
                else:
                    last_multi_frame_octet[y] = temp_data
            if z == f_reg - 1:
                if temp_data == 'fc':
                    temp_data = last_frame_octet[y]
                else:
                    last_frame_octet[y] = temp_data
            all_data.append(temp_data)

m_data = [[],[]]
mdata = [[],[]]
all_m_idx = int(all_idx*f_reg*l_reg/2/m_reg/s_reg)
for x in range(0,all_m_idx):
    for y in range(0,m_reg):
        for z in range(0,2*s_reg):
            m_data[y].append(all_data.pop(0))
m_data_len = int(len(m_data[0])/2)
fo = open('m_data.dat', 'w')
for x in range(0,m_data_len):
    for y in range(0,m_reg):
        mdata[y].append(int(m_data[y][x*2]+m_data[y][x*2+1],16))
        fo.write(m_data[y][x*2]+m_data[y][x*2+1]+' ')
    fo.write('\n')
fo.close()

ts = np.linspace(1,len(mdata[0]),len(mdata[0]))
data = np.array(mdata[1])
data = np.where(data>32768,data-65536,data)
plt.figure(1)
plt.plot(ts, data)
plt.legend()
plt.show()

        