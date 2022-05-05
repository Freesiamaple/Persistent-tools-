import math
import numpy as np
import matplotlib.pyplot as plt
from pyparsing import alphas


filename='C1_d2n20_D10N10^3'


xlim=[920,980]
ylim=[940,1000]
zlim=[40,100]

DATA_DIR = "./data/model data/"
IMAGE_DIR = "./data/images/"
plt.rcParams["font.family"] = "Arial"   # 使用するフォント
plt.rcParams["font.size"] = 14

AZ = open('{}{}.txt'.format(DATA_DIR,filename), 'r')#座標のファイル名(txt)
K=[]
while True:
    AZ_datalist = AZ.readline()
    if AZ_datalist=='':
        break
    A=list(map(float,AZ_datalist.split()))
    K.append(A)
AZ.close()
X=[]
Y=[]
Z=[]
R=[]

for i in K:
    if xlim[0]<=i[0]<=xlim[1] and ylim[0]<=i[1]<=ylim[1] and zlim[0]<=i[2]<=zlim[1]:
        X.append(i[0])
        Y.append(i[1])
        Z.append(i[2])
        R.append(i[3])

X=np.array(X)
Y=np.array(Y)
Z=np.array(Z)
R=np.array(R)


fig = plt.figure()

ax = fig.add_subplot(111, projection = '3d')
ax.set_xlim(xlim)
ax.set_ylim(ylim)
ax.set_zlim(zlim) 

ax.set_xlabel("x (μm)")
ax.tick_params(axis='x')
ax.set_ylabel("y (μm)")
ax.tick_params(axis='y')
ax.set_zlabel("z (μm)")
ax.tick_params(axis='z')

A=ax.scatter(X, Y, Z, s =R*20, c=2*R**(1/2) , linewidths=0.25,edgecolors='black',cmap='jet',vmin=2,vmax=20,alpha=1)
fig.colorbar(A,ax=ax,shrink=0.8,pad=0.15).set_label('Pore Diameter(μm)')

plt.savefig("{}focus{}.png".format(IMAGE_DIR,filename),dpi=500)
plt.show()
print("end")