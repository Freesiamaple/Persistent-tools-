import homcloud.interface as hc
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
import matplotlib.cm as cm

filename='d5n1000_D10N10^4'

plt.rcParams["font.family"] = "Arial"   # 使用するフォント
plt.rcParams["font.size"] = 14

DATA_DIR = "./data/model data/"
CACHE_DIR = "./data/cache/"
IMAGE_DIR = "./data/images/"
INVERSE_DIR = "./data/Inverse analysis/"

pdlist = hc.PDList("{}{}.pdgm".format(CACHE_DIR,filename))
pd1 = pdlist.dth_diagram(1)

pair = pd1.nearest_pair_to(-10,-10)

optimal_volume = pair.optimal_volume()
print(pair)

#指定範囲(逆解析したい範囲)
b_range=(15,20)
d_range=(40,45)

L=[]

for i in range (b_range[0],b_range[1]+1):
    for j in range(d_range[0],d_range[1]+1):
        pair = pd1.nearest_pair_to(i,j)
        L.append(pair)

L=list(set(L))
RO = open(('{}{}_inverse.txt'.format(INVERSE_DIR,filename)), 'w')
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

