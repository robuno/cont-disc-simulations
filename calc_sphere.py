r1 = 2.95
r2 = 3


import math

vol_outer = (2/3)*math.pi*(r2)**3
vol_inner = (2/3)*math.pi*(r1)**3

print("outer sphere: ", vol_outer)
print("inner sphere: ", vol_inner)

print("diff: ",vol_outer-vol_inner)
print(5**3)

# outer sphere:  56.54866776461627
# inner sphere:  53.768096466801516
# diff:  2.7805712978147525