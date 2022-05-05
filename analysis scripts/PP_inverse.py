import homcloud.interface as hc
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.art3d as art3d
import matplotlib.colors
import matplotlib.cm as cm

filename='D10N10^3'
filename_compare='C1_d2n20_D10N10^3'

#調べるb,dの範囲
blim=[0,5]
dlim=[0,5]

#グラフの表示範囲
xlim=[920,980]
ylim=[940,1000]
zlim=[40,100]

plt.rcParams["font.family"] = "Arial"   # 使用するフォント
plt.rcParams["font.size"] = 14

DATA_DIR = "./data/model data/"
CACHE_DIR = "./data/cache/"
IMAGE_DIR = "./data/images/"
INVERSE_DIR = "./data/Inverse analysis/"

BD=open('{}{}_birth_death_pair.txt'.format(CACHE_DIR,filename),'r')

BD1=[]
while True:
    BD_datalist = BD.readline()
    if "#" in BD_datalist:
        continue
    if BD_datalist=='':
        break
    A=list(map(float,BD_datalist.split()))
    if blim[0]<=A[0]<=blim[1] and dlim[0]<=A[1]<=dlim[1]:
        BD1.append(A)
BD.close()

BD=open('{}{}_birth_death_pair.txt'.format(CACHE_DIR,filename_compare),'r')

BD2=[]
while True:
    BD_datalist = BD.readline()
    if "#" in BD_datalist:
        continue
    if BD_datalist=='':
        break
    A=list(map(float,BD_datalist.split()))
    if blim[0]<=A[0]<=blim[1] and dlim[0]<=A[1]<=dlim[1]:
        BD2.append(A)
BD.close()


BD12 = [x for x in BD1 if x in BD2]
ch_BD2=[x for x in BD2 if not x in BD12]
ch_BD1=[x for x in BD1 if not x in BD12]
print("before=",len(BD1))
print("after=",len(BD2))
print("before ⋂ after=",len(BD12))
print("before only=",len(ch_BD1))
print("after only=",len(ch_BD2))


L=[]

pdlist = hc.PDList("{}{}.pdgm".format(CACHE_DIR,filename_compare))
pd1 = pdlist.dth_diagram(1)

for i in ch_BD2:
    pair = pd1.nearest_pair_to(i[0],i[1])
    L.append(pair)

L=list(set(L))
RO = open(('{}{}_inverse.txt'.format(INVERSE_DIR,filename_compare)), 'w')
for pair in L:
    optimal_volume = pair.optimal_volume()
    X=list(optimal_volume.boundary_points())

    for x in X:
        RO.write(str(x[0]))
        RO.write(" ")
        RO.write(str(x[1]))
        RO.write(" ")
        RO.write(str(x[2]))
        RO.write(" ")
    RO.write('\n')
RO.close()

filename_inverse='{}_inverse'.format(filename_compare)
AZ = open('{}{}.txt'.format(DATA_DIR,filename_compare), 'r')#座標のファイル名(txt)
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

A=ax.scatter(X, Y, Z, s =R*25 ,c=2*R**(1/2) , linewidths=0.25,edgecolors='black',cmap='jet',vmin=2,vmax=20,alpha=1)
fig.colorbar(A,ax=ax,shrink=0.8,pad=0.15).set_label('Pore Diameter(μm)')

AZ = open('{}{}.txt'.format(INVERSE_DIR,filename_inverse), 'r')#座標のファイル名(txt)
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
for i in K:
     if xlim[0]<=i[0]<=xlim[1] and ylim[0]<=i[1]<=ylim[1] and zlim[0]<=i[2]<=zlim[1] and xlim[0]<=i[3]<=xlim[1] and ylim[0]<=i[4]<=ylim[1] and zlim[0]<=i[5]<=zlim[1] and xlim[0]<=i[6]<=xlim[1] and ylim[0]<=i[7]<=ylim[1] and zlim[0]<=i[8]<=zlim[1]:
         X.append([i[0],i[3],i[6]])
         Y.append([i[1],i[4],i[7]])
         Z.append([i[2],i[5],i[8]])

#塗りつぶすとき
#for i in range(len(X)):
    #x = X[i]
    #y = Y[i]
    #z = Z[i]
    #poly = list(zip(x,y,z))
    #ax.add_collection3d(art3d.Poly3DCollection([poly],linewidth=1,color='gray'))
    
#塗りつぶさないで線分のみ
for i in range(len(X)):
    x=X[i]
    x.append(X[i][0])
    y=Y[i]
    y.append(Y[i][0])
    z=Z[i]
    z.append(Z[i][0])
    line= art3d.Line3D(x,y,z, color='gray')
    ax.add_line(line)




plt.savefig("{}{}_inverse.png".format(IMAGE_DIR,filename_compare),dpi=500)
plt.show()
print("end")