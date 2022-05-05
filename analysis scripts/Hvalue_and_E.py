import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
import matplotlib.cm as cm


filename='_cut_C10R_d2n20_D10N10^3'


CACHE_DIR = "./data/cache/"
IMAGE_DIR = "./data/images/"
DATA_DIR = "./data/model data/"
plt.rcParams["font.family"] = "Arial" 
plt.rcParams["font.size"] = 14



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
L=len(B)
l=len(D)
if L!=l:
    print("Num error")
#重心
xc=sum(B)/len(B)
yc=sum(D)/len(D)
hmax=0
for i in range(len(B)):
    hmax=max(hmax,D[i]-B[i])
    

h1=(1/(2**(1/2)))*(yc-xc)
h2=2**(1/2)*xc
Hvalue=(h1**2+h2**2)**(1/2)/hmax
print("H =",Hvalue)


AZ = open('{}{}.txt'.format(DATA_DIR,filename), 'r')#座標のファイル名(txt)
K=[]
while True:
    AZ_datalist = AZ.readline()
    if AZ_datalist=='':
        break
    A=list(map(float,AZ_datalist.split()))
    K.append(A)
AZ.close()

R=[]

for i in K:
    p=4*np.pi/3*(i[3]**(3/2))
    R.append(p)
Porosity=sum(R)/1000/1000/400
Porosity_format=format(Porosity,'.9f')
print("porosity=",Porosity_format,"(-)")
Er=(1-Porosity**(2/3))**(1/Hvalue)
print("Enew/(E0×a0)=",Er)
##############################
H_list=[]
for i in range(len(B)):
    x_=B[i]
    y_=D[i]
    h1_=(1/(2**(1/2)))*(y_-x_)
    h2_=2**(1/2)*x_
    H_=(h1_**2+h2_**2)**(1/2)/hmax
    H_list.append(H_)

ar=np.array(H_list)
plt.hist(ar, bins=100,range=(0,4),log=True)
plt.ylim(0,18000)
plt.xlabel("H value (-)")          
plt.ylabel("Frequency")
plt.savefig("{}{}_H.png".format(IMAGE_DIR,filename),dpi=500)
#plt.show()
print("end")