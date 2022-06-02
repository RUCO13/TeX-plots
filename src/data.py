import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import numpy as np
import sys,os

x = np.array([i for i in range(-50,50,2)])
y = np.array([(5*x[j]**3-.2*x[j]) for j in range(len(x))])

expdata = np.zeros((len(x),2))
expdata[:,0]=x
expdata[:,1]=y
np.savetxt("test-data.dat",expdata,delimiter=',')

#plot data
fig,ax = plt.subplots(1,1,figsize=(5,8))
ax.plot(x,y,'-ob',ms=7,mfc="w")
plt.show()