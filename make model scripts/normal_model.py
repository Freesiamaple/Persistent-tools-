import random

filename="d20n1000_D10N10^4"

DATA_DIR = "./data/model data/"


#add
x_center=500
x_range =500

y_center=500
y_range =500

z_center=500
z_range =500

add_num=1000#数
add_r=100#半径の二乗

#body
x_center_b=500
x_range_b =500

y_center_b=500
y_range_b =500

z_center_b=500
z_range_b =500

body_num=10000
body_r=25#半径の二乗


RO = open(('{}{}.txt'.format(DATA_DIR,filename)), 'w')
random.seed(0)#fix seed
for i in range(add_num):
    RO.write(str(random.uniform(x_center-x_range,x_center+x_range)))
    RO.write(' ')
    RO.write(str(random.uniform(y_center-y_range,y_center+y_range)))
    RO.write(' ')
    RO.write(str(random.uniform(z_center-z_range,z_center+z_range)))
    RO.write(' ')
    RO.write(str(add_r))
    RO.write('\n')


random.seed(1)#fix seed
for j in range(body_num):
    RO.write(str(random.uniform(x_center_b - x_range_b,x_center_b + x_range_b)))
    RO.write(' ')
    RO.write(str(random.uniform(y_center_b - y_range_b,y_center_b + y_range_b)))
    RO.write(' ')
    RO.write(str(random.uniform(z_center_b - z_range_b,z_center_b + z_range_b)))
    RO.write(' ')
    RO.write(str(body_r))
    RO.write('\n')
RO.close()
print("end")