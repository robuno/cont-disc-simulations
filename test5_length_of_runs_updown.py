import math

number_array = [
    0.30, 0.48, 0.36, 0.01, 0.54, 0.34, 0.96, 0.06, 0.61, 0.85,
    0.48, 0.86, 0.14, 0.86, 0.89, 0.37, 0.49, 0.60, 0.04, 0.13,
    0.42
]

N = len(number_array)
critical_X02 = 7.81

def check_hyp(X0_2, X0_2_critical):
    if X0_2 < X0_2_critical:
        print("{} < {}".format(X0_2,X0_2_critical)),
        print("The null hypothesis of a uniform distribution is not rejected")
    else:
        print("Rejected")



up_down_array = []

for i in range(1,len(number_array)):
    first_val = number_array[i-1]
    second_val = number_array[i]

    if (second_val < first_val):
        up_down_array.append(-1)
    
    if (first_val < second_val):
        up_down_array.append(1)

print(up_down_array)



# get length of runs
length_of_runs = []
i = 0
while (i <= len(up_down_array)-1):
        count = 1
        j = i
        while (j < len(up_down_array)-1):
            if (up_down_array[j] == up_down_array[j+1]):
                count = count+1
                j = j+1
            else:
                break
        length_of_runs.append(count)
        i = j+1

print(length_of_runs)

obs_runs_1 = length_of_runs.count(1)
obs_runs_2 = length_of_runs.count(2)
obs_runs_3 = length_of_runs.count(3)

obs_array = []
for i in range(1,4):
    obs_array.append(length_of_runs.count(i))
    print("i: {}   Oi: {}".format( i, length_of_runs.count(i)))


 
def expected_val_updown(N,i):
    if i <= N-2:
        first_part = (2/math.factorial(i+3))
        second_1 = N*((i**2)+(3*i)+1)
        second_2 = ((i**3)+(3*(i**2))-i-4)
        second_part = second_1 - second_2
        return first_part * second_part
    if i == N-1:
        return  2 / (math.factorial(N))

def calc_mean(N):
    return (2*N-1)/3

#mean of total number of runs 
mean_val = calc_mean(60)
print("Mean: ",mean_val)
print()

EY1 = expected_val_updown(60,1)
EY2 = expected_val_updown(60,2)
EY3 = expected_val_updown(60,3)

print("EY1: ",round(EY1,2))
print("EY2: ",round(EY2,2))
print("EY3: ",round(EY3,2))

EYmore3 = mean_val - (EY1+EY2+EY3)
print("EYmore3: ",round(EYmore3,2))


#hardcoded Oi
obs_array = [26,9,5]

sum_X02 = 0 + EYmore3

for i in range(1,4):
    Oi = obs_array[i-1]
    ExY = expected_val_updown(60,i)
    X02 = ((Oi- ExY)**2)/ ExY
    sum_X02 += X02
    print("i: {}   Oi: {}   EY: {}   X02: {}".format(
        i,
        Oi,
        round(ExY,2),
        round(X02,2)
    ))


print("X02: ",sum_X02)

check_hyp(sum_X02,critical_X02)

