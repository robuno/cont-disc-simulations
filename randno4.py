# 4 additive congruential method

import random

x1 = int(random.random()*1000)
x2 = int(random.random()*1000)
x3 = int(random.random()*1000)
x4 = int(random.random()*1000)
x5 = int(random.random()*1000)

n = 5 # starter X to calculate next X
m = 100 # mod

x1 = 57
x2 = 34
x3 = 89
x4 = 92
x5 = 16

x_array = [x1,x2,x3,x4,x5]

REPS = 5
START_X = 6

for REP in range(START_X, START_X + REPS):

    x_first = x_array[0]
    x_second = x_array[-1]
    print("Xfirst: {},   Xsecond: {}".format(x_first,x_second))

    x_new = (x_first + x_second) % m

    print("X{}: {}".format(REP, x_new))
    print("R{}: {}".format(REP-n,(x_new /m)))

    del x_array[0] # delete resiudary initial element
    x_array.append(x_new)
    print()

