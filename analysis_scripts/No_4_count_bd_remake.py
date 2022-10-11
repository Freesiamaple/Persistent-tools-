import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
import matplotlib.cm as cm

filename='n=151_Al'
filename_compare='n=152_Al'
#バグった場合この範囲外にPPがあると思います
xlim=[-100,1500]
ylim=[-100,1500]
width=100
plt.rcParams["font.family"] = "Arial"   # 使用するフォント
plt.rcParams["font.size"] = 14

DATA_DIR = "./data/model data/"
CACHE_DIR = "./data/cache/"
IMAGE_DIR = "./data/images/"
INVERSE_DIR = "./data/Inverse analysis/"


Birth=open('{}{}_b_pd1.txt'.format(CACHE_DIR,filename),'r')
Death=open('{}{}_d_pd1.txt'.format(CACHE_DIR,filename),'r')
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


#グラフ
x=B
y=D

fig = plt.figure()
ax = fig.add_subplot(111)

plt.xticks([i for i in range(xlim[0],xlim[1]+width,width)],fontsize=6)
plt.yticks([i for i in range(ylim[0],ylim[1]+width,width)],fontsize=6)
plt.minorticks_on()
plt.grid(which="major", color="gray", linestyle="solid",linewidth=0.25)
Gnum=len(B)

G=[[0]*((xlim[1]-xlim[0])//width) for _ in range((ylim[1]-ylim[0])//width)]
for i in range(len(B)):
    G[int((B[i]-xlim[0])//width)][int((D[i]-ylim[0])//width)]+=1


Birth=open('{}{}_b_pd1.txt'.format(CACHE_DIR,filename_compare),'r')
Death=open('{}{}_d_pd1.txt'.format(CACHE_DIR,filename_compare),'r')
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
Pnum=len(B)

P=[[0]*((xlim[1]-xlim[0])//width) for _ in range((ylim[1]-ylim[0])//width)]

for i in range(len(B)):
    P[int((B[i]-xlim[0])//width)][int((D[i]-ylim[0])//width)]+=1


#G:元の集団
#P比較対象
for j in range(len(G)):
    for k in range(len(G[j])):
        if G[j][k]==0 and P[j][k]==0:
            continue
        else:
            if G[j][k]==0:
                ax.text(xlim[0]+width*j, ylim[0]+width*k, "o", fontsize=8,c='red')
                continue
            if P[j][k]==0:
                ax.text(xlim[0]+width*j, ylim[0]+width*k, "x", fontsize=8,c='blue')
                continue
            if G[j][k]/Gnum>P[j][k]/Pnum:
                ax.text(xlim[0]+width*j, ylim[0]+width*k, str(int(((float(P[j][k]/Pnum)/(G[j][k]/Gnum))*100))), fontsize=5,c='blue')
            if G[j][k]/Gnum<P[j][k]/Pnum:
                ax.text(xlim[0]+width*j, ylim[0]+width*k, str(int(((float(P[j][k]/Pnum)/(G[j][k]/Gnum))*100))), fontsize=5,c='red')
            if G[j][k]/Gnum==P[j][k]/Pnum:
                ax.text(xlim[0]+width*j, ylim[0]+width*k,"0", fontsize=5,c='black')
ax.set_xlabel('Birth (μm)')
ax.set_ylabel('Death (μm)')


aspect = (ax.get_xlim()[1] - ax.get_xlim()[0]) / (ax.get_ylim()[1] - ax.get_ylim()[0])                     
ax.set_aspect(aspect)
ax.text(xlim[1]+width, ylim[0]+2*width, "{}:{}".format(str(filename),str(Gnum)), fontsize=6,c='black')
ax.text(xlim[1]+width, ylim[0], "{}:{}".format(str(filename_compare),str(Pnum)), fontsize=6,c='black')

plt.savefig("{}count_{}.png".format(IMAGE_DIR,filename_compare),dpi=500)
plt.show()

print("end")