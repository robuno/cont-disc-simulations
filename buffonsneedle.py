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
    
    
    
#a:  0.5050504947742617     b:  0.8566337409206476
#a:  1.197470725595553     b:  2.1981217053983704
#a:  1.9996168850552056     b:  1.1969356069026897
#a:  1.5296386360450123     b:  1.617103423921395
#a:  2.9996421994013     b:  1.187462337503683
#a:  2.673056744571089     b:  2.1601046598493947
#a:  2.6903630999540713     b:  1.7028122198281475
#***************
#Reps:  10000
## intersects:  6317
#pi:  3.1660598385309484
