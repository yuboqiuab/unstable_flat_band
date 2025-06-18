import numpy as np
import array
import math
import matplotlib.pyplot as plt
from matplotlib import rcParamsDefault
import time

with open('hfo_band.xmgr', 'r') as f1:
    row = f1.readlines()
i1,i2 = [],[]
for i in row:
   j=i.split()
   if(len(j)>1):
      i1.append(j[0])
      i2.append(j[1])

i1 = np.array(i1).reshape(-1, 1)
i1= i1.astype(np.float64)
i2 = np.array(i2).reshape(-1, 1)
i2= i2.astype(np.float64)

k=np.reshape(i1,(-1,1401))
band=np.reshape(i2,(-1,1401))

plt.rcParams["figure.dpi"]=150
plt.rcParams["figure.facecolor"]="white"
plt.rcParams["figure.figsize"]=(12, 5)
for i in range(len(k)):
     plt.plot(k[i], band[i], "-", markersize=0.2, linewidth=0.75, alpha=1.0, color='k')

tl=2000
pk=np.zeros(tl,dtype='float')
pb=np.zeros(tl,dtype='float')
lwidths=np.zeros(tl,dtype='float')


plt.axvline(0.2523, linewidth=1.25, color='k', alpha=1.0)
plt.axvline(0.7523, linewidth=1.25, color='k', alpha=1.0)
plt.axvline(1.0046, linewidth=1.25, color='k', alpha=1.0)

plt.axvline(1.5047, linewidth=1.25, color='k', alpha=1.0)
plt.axvline(2.0047, linewidth=1.25, color='k', alpha=1.0)
plt.axvline(2.2570, linewidth=1.25, color='k', alpha=1.0)
plt.axhline(0.0, linestyle='--', color='k')
plt.xlim(0.0, 2.7570)
plt.ylim(-200, 1000)



plt.xticks(ticks= [0, 0.2523, 0.7523, 1.0046, 1.5047, 2.0047, 2.2570, 2.7570], \
           labels=['$\Gamma$','$Y$','$M$','$Z$','$N$','$X$','$L$','$R$'])

plt.yticks(ticks= [-200, 0, 200,400,600,800,1000])

plt.savefig("see.png",dpi=300)
