import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
import matplotlib.cm as cm

filename='63'

xlim=[-30,0]
ylim=[-20,80]
width_y=100
width_x=100
plt.rcParams["font.family"] = "Arial"   # 使用するフォント
plt.rcParams["font.size"] = 14


DATA_DIR = "./data/model data/"
CACHE_DIR = "./data/cache/"
IMAGE_DIR = "./data/images/"
Birth=open('{}{}_b_pd0.txt'.format(CACHE_DIR,filename),'r')
Death=open('{}{}_d_pd0.txt'.format(CACHE_DIR,filename),'r')


B=[]
while True:
    B_datalist = Birth.readline()
    if "#" in B_datalist:
        continue
    if B_datalist=='':
        break
    A=float(list(map(str,B_datalist.split()))[0])
    B.append(A)
Birth.close()

D=[]
while True:
    D_datalist = Death.readline()
    if "#" in D_datalist:
        continue
    if D_datalist=='':
        break
    A=float(list(map(str,D_datalist.split()))[0])
    D.append(A)
Death.close()
L=len(B)
l=len(D)
if L!=l:
    print("Num error")

BD = open('{}{}_birth_death_pair_pd0.txt'.format(CACHE_DIR,filename), 'w')
for i in range(0,L):
    BD.write(str(B[i]))
    BD.write(" ")
    BD.write(str(D[i]))
    BD.write('\n')
BD.close()



x=B
y=D
fig = plt.figure()
ax = fig.add_subplot(121)
H = ax.hist2d(x,y, bins=[np.linspace(xlim[0],xlim[1],width_x),np.linspace(ylim[0],ylim[1],width_y)], norm=matplotlib.colors.LogNorm(), cmap=cm.rainbow)
plt.minorticks_on()
plt.grid(which="major", color="gray", linestyle="solid",linewidth=0.25)
plt.axhline(y=0, xmin=-10, xmax=120,linewidth=0.5,c='black')
ax.set_xlabel('Birth (μm)')
ax.set_ylabel('Death (μm)')
fig.colorbar(H[3],ax=ax, label='Number Density(-)') 
plt.savefig("{}{}_pd0.png".format(IMAGE_DIR,filename),dpi=500)
plt.show()
# 表示する


print("end")
