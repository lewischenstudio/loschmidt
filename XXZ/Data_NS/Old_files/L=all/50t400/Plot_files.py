# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 15:34:20 2017

@author: LewisCYC
"""
import os             
import glob
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import InsetPosition

L=800
delta=0.3
W=1.0
tmid=2
tmax=10
dt1=0.0008
dt2=0.05
cwd = os.getcwd() #current working directory
item=glob.glob("*.txt")
t1=np.arange(0,tmid,dt1)
t2=np.arange(tmid,tmax+dt2,dt2)
tm=np.concatenate((t1,t2), axis=0)
Pfiles=np.zeros((len(item),len(tm)))
a=0
for i in range(len(item)):
    f=open(item[i],'r')
    AA=f.readlines()
    for j in range(len(AA)):
        Pfiles[a][j]=AA[j]
    a+=1


"""Plot the Figure """
fig, ax = plt.subplots()
tiTle='Return Rate for L = '+str(L)+' with $\delta$ = +'+str(delta)+' and $\mu\in$ [$-W,W$]'
Wlabel=np.asarray([0.00005,2.5e-04,0.0005,0.0025,0.005,0.025,0.05,0.25,0.5,0.0])
plt.plot(tm[:2500],Pfiles[-1][:2500],label='W='+str(Wlabel[-1]))
a=0
for num in range(len(Pfiles)-1):
    #c1=np.random.rand()
    #c2=np.random.rand()
    #c3=np.random.rand()
    plt.plot(tm[:2500],Pfiles[num][:2500],label='W='+str(Wlabel[num]))#color=(c1,c2,c3))
    a+=1
plt.ylim([-0.1,1.8])
plt.xlim([0,3])
plt.xticks([0.0,0.5,1.0,1.5,2.0])
plt.xlabel('t')
plt.ylabel('l(t)')
#plt.title(tiTle,fontsize=11)
plt.legend(loc='upper right')

iax = plt.axes([-1, 0, 2, 2])
ip = InsetPosition(ax, [0.27, 0.05, 0.4, 0.4]) #posx, posy, width, height
iax.set_axes_locator(ip)
ss=Pfiles[:,981:984]
dd=ss
dd[0]=ss[-1]
dd[1:]=ss[0:-1]
for i in dd:
    plt.plot(i)
plt.ylim([1.2,1.65])
plt.xticks([])
plt.yticks([])
plt.show()



tiTle='Return Rate for L = '+str(L)+' with $\delta$ = +'+str(delta)+' and $\mu\in$ [$-W,W$]'
plt.plot(tm[981:984],Pfiles[len(item)-1][981:984],label='W='+str(Wlabel[-1]))
b=0
for num in range(len(Pfiles)-1):
    plt.plot(tm[981:984],Pfiles[num][981:984],label='W='+str(Wlabel[num]))#color=(c1,c2,c3))
    b+=1
plt.ylim([1.20,1.65])
plt.xlim([0.7852,0.7864])
plt.xlabel('t')
plt.ylabel('l(t)')
#plt.title(tiTle,fontsize=11)
plt.legend(loc='upper right')
plt.show()