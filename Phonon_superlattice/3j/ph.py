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


plt.axvline(1.4932, linewidth=1.25, color='k', alpha=1.0)
plt.axvline(2.8279, linewidth=1.25, color='k', alpha=1.0)
plt.axvline(4.3211, linewidth=1.25, color='k', alpha=1.0)

plt.axvline(4.8211, linewidth=1.25, color='k', alpha=1.0)
plt.axvline(6.1557, linewidth=1.25, color='k', alpha=1.0)
plt.axvline(7.6489, linewidth=1.25, color='k', alpha=1.0)

plt.axvline(8.9836, linewidth=1.25, color='k', alpha=1.0)

plt.axhline(0.0, linestyle='--', color='k')

plt.xlim(0.0, 8.9836)
plt.ylim(-200, 1000)


plt.xticks(ticks= [0, 1.4932, 2.8279, 4.3211, 4.8211, 6.1557, 7.6489, 8.9836], \
           labels=['$\Gamma$','$Y$','$T$','$Z$','$U$','$X$','$S$','$R$'])

plt.yticks(ticks= [-200, 0, 200,400,600,800,1000])

plt.savefig("see.png",dpi=300)
