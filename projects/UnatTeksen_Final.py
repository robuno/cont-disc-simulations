import math
import random


# r1 = 2.95
# r2 = 3
# N = 2000000

r1 = float(input("Enter r1: "))
r2 = float(input("Enter r2: "))
N = int(input("Number of sample points: "))

r_max = r2 + 0.15

hit_count_volume =0

for REP in range(N):
    x_rand = random.uniform(-r_max, r_max)
    z_rand = random.uniform(-r_max, r_max)
    y_rand = random.uniform(-r_max, 0)
    # print("x: ", x_rand, ",  y:",y_rand, ",  z:",z_rand)

    dist_to_origin = ((x_rand)**2 + (y_rand**2) + (z_rand)**2)**(1/2)

    if (r1 <= dist_to_origin <= r2 ):
        hit_count_volume+=1

# rectangular shape volume: (2*rmax)*(2*rmax)*(rmax)
conv_volume = (hit_count_volume / N) * 4 * (r_max)**3
print("------")
print("N: ", N)
print(hit_count_volume)
print("Volume: ", conv_volume)




