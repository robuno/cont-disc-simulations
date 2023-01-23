import math 
import random


def func1(x):
    return math.sin(x/2)

def func2(x):
    return math.sin(-x/2) + 1

def calc_area(sum, lower, upper, n):
    return (upper-lower)*(1/n)*sum

x_lower = 0
x1 = math.pi/3
x2 = math.pi*(5/3)

print("x1: ", x1)
print("x2: ",x2)

# x1:  1.0471975511965976
# x2:  5.235987755982989


for i in range(0,00):
    func_1_val = func1(i/100)
    func_2_val = func2(i/100)
    print("x: ",i/100," f1: ",func_1_val)
    print("x: ",i/100," f2: ",func_2_val)
    print()
    if round(func_1_val,2) == round(func_2_val,2):
        print("x root found: ", i/100)





N = 1000000
sum1 = 0
sum2 = 0

sum3 = 0
sum4 = 0

for REP in range(N):
    x1_random = random.uniform(0,x1)

    sum1 += func2(x1_random)
    sum2 += func1(x1_random)

    x2_random = random.uniform(x1,x2)

    sum3 += func1(x2_random)
    sum4 += func2(x2_random)


area1 = calc_area(sum1, 0, x1, N)
area2 = calc_area(sum2, 0, x1, N)

area3 = calc_area(sum3, x1, x2, N)
area4 = calc_area(sum4, x1, x2, N)


print("A: ", area1-area2)
print("A: ", area3-area4)







