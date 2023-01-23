import math
import random

REPS = 1000000
alfa = 4
beta = 12
LOWER = 0
UPPER = 0.412

fact_gamma = 1  # will be 6
for i in range(1,alfa):
  fact_gamma = fact_gamma *(i)

def func_distribution(x):
  func_dist = ((x**(alfa-1))*(math.exp(-beta*x))*(beta**4))/fact_gamma
  # func_dist = ((x**3)*(math.exp(-12*x))*(12**4))/6
  return func_dist


# find max of func
for i in range(LOWER, 45):
  print("i: ",i/100 , "value: ", func_distribution(i/100))
# i:  0.25 value:  2.688501691864653

fmax = 2.70
method_1_count = 0

#method hit or miss
for REP in range(REPS):
  x = random.uniform(LOWER, UPPER)
  y = random.uniform(0, fmax)
  if y <= func_distribution(x):
    # print("func val: ", func_distribution(x), "y: ", y)
    method_1_count +=1

apprx_int_1 = (method_1_count/REPS)*(UPPER-LOWER)*fmax

print("Hit or Miss Method")
print("Approximate Integral: ",apprx_int_1)
print()

sum_SM = 0
for REP in range(REPS):
  x = random.uniform(LOWER, UPPER)
  # # print("x: ",x, "value: ",func_distribution(x))
  # # print("sum: ", sum_SM)
  
  sum_SM += func_distribution(x)

approx_int_2 = (UPPER-LOWER)*(1/REPS)*sum_SM
print("Sample Mean Method")
print("Approximate Integral: ",approx_int_2)