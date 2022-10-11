import homcloud.interface as hc  # HomCloudのインターフェス
import numpy as np
import matplotlib.pyplot as plt
import homcloud.paraview_interface as pv

filename='111d4'


DATA_DIR = "./data/model data/"
CACHE_DIR = "./data/cache/"

#pdgm file
pointcloud = np.loadtxt('{}{}.txt'.format(DATA_DIR,filename))
pointcloud.shape
hc.PDList.from_alpha_filtration(pointcloud, save_to="{}{}.pdgm".format(CACHE_DIR,filename),save_boundary_map=True,weight=True,no_squared=True)

#pd0
pdlist = hc.PDList('{}{}.pdgm'.format(CACHE_DIR,filename))
pd0 = pdlist.dth_diagram(0)
np.savetxt("{}{}_b_pd0.txt".format(CACHE_DIR,filename),pd0.births,header='b')
np.savetxt("{}{}_d_pd0.txt".format(CACHE_DIR,filename),pd0.deaths,header='d')

#pd1
pdlist = hc.PDList("{}{}.pdgm".format(CACHE_DIR,filename))
pd1 = pdlist.dth_diagram(1)
np.savetxt('{}{}_b_pd1.txt'.format(CACHE_DIR,filename),pd1.births,header='b')
np.savetxt('{}{}_d_pd1.txt'.format(CACHE_DIR,filename),pd1.deaths,header='d')


print("end")

