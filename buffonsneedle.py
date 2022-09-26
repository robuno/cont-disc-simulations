import random
import math

# print(math.pi)

d = 5
l = 5

N = 10000
prob = 0
for i in range(N):
    a = random.uniform(0,math.pi)
    b = random.uniform(0,d/2)
    print("a: ",a,"    b: ",b)


    if (l/2)*math.sin(a) >= b:
        prob +=1

print("***************")
print("Reps: ", N)
print("# intersects: ", prob)
print("pi: ", (2*N*l)/(prob*d))
    