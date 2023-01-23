# 5 linear congruential method

import random

x0 = int(random.random()*1000)
a = int(random.random()*1000)
c = int(random.random()*1000)

m = 100 # mod
x0 = 27
a = 17
c = 43


m = (2**31) - 1 # mod
x0 = 123457
a = 7**5
c = 0

REPS = 20
START_X = 1

numbers_Array = []

for REP in range(START_X, START_X + REPS):

    print("X0: {},   a: {},   c: {}".format(x0, a, c))

    x_new = (a*x0 + c) % m 
    R = x_new / m 

    numbers_Array.append(round(R,4))

    print("X{}: {}".format(REP, x_new))
    print("R{}: {}".format(REP,R))

    x0 = x_new
    print()

print(numbers_Array)
