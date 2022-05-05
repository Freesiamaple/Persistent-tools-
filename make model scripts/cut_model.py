filename='C10P_d2n20_D10N10^3'
DATA_DIR = "./data/model data/"
xlim=[0,1000]
ylim=[0,1000]
zlim=[300,700]

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


RO = open(('{}_cut_{}.txt'.format(DATA_DIR,filename)), 'w')
for i in range(len(X)):
    RO.write(str(X[i]))
    RO.write(' ')
    RO.write(str(Y[i]))
    RO.write(' ')
    RO.write(str(Z[i]))
    RO.write(' ')
    RO.write(str(R[i]))
    RO.write(' ')
    RO.write('\n')
RO.close()