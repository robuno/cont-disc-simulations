m = 100 # mod
x0 = 27
a = 17
c = 43

numbers_array = []

REPS = 100
START_X = 1
for REP in range(START_X, START_X + REPS):
    #print("X0: {},   a: {},   c: {}".format(x0, a, c))
    x_new = (a*x0 + c) % m 
    R = x_new / m 

    numbers_array.append(round(R,4))
    #print("X{}: {}".format(REP, x_new))
    #print("R{}: {}".format(REP,R))
    x0 = x_new
    #print()

print(numbers_array)




# numbers_array =  [
#      0.34, 0.90, 0.25, 0.89, 0.87, 0.44, 0.12, 0.21, 0.46, 0.67,
#      0.83, 0.76, 0.79, 0.64, 0.70, 0.81, 0.94, 0.74, 0.22, 0.74,
#      0.96, 0.99, 0.77, 0.67, 0.56, 0.41, 0.52, 0.73, 0.99, 0.02,
#      0.47, 0.30, 0.17, 0.82, 0.56, 0.05, 0.45, 0.31, 0.78, 0.05,
#      0.79, 0.71, 0.23, 0.19, 0.82, 0.93, 0.65, 0.37, 0.39, 0.42,
#      0.99, 0.17, 0.99, 0.46, 0.05, 0.66, 0.10, 0.42, 0.18, 0.49,
#      0.37, 0.51, 0.54, 0.01, 0.81, 0.28, 0.69, 0.34, 0.75, 0.49,
#      0.72, 0.43, 0.56, 0.97, 0.30, 0.94, 0.96, 0.58, 0.73, 0.05,
#      0.06, 0.39, 0.84, 0.24, 0.40, 0.64, 0.40, 0.19, 0.79, 0.62,
#      0.18, 0.26, 0.97, 0.88, 0.64, 0.47, 0.60, 0.11, 0.29, 0.78
#      ]


N = len(numbers_array) 
no_of_intervals = 10
X0_2_critical = 16.9
X0_2 = 0
Ei = N/no_of_intervals

def check_hyp(X0_2, X0_2_critical):
    if X0_2 < X0_2_critical:
        print("{} < {}".format(X0_2,X0_2_critical)),
        print("The null hypothesis of a uniform distribution is not rejected")
    else:
        print("Hyp. is rejected!")


observed_counts = [0] * no_of_intervals

# get observed values for intervals
for i in range(len(numbers_array)):
    if 0 <= numbers_array[i] <= 0.1:
        observed_counts[0] +=1
    if 0.1 < numbers_array[i] <= 0.2:
        observed_counts[1] +=1
    if 0.2 < numbers_array[i] <= 0.3:
        observed_counts[2] +=1
    if 0.3 < numbers_array[i] <= 0.4:
        observed_counts[3] +=1
    if 0.4 < numbers_array[i] <= 0.5:
        observed_counts[4] +=1
    if 0.5 < numbers_array[i] <= 0.6:
        observed_counts[5] +=1
    if 0.6 < numbers_array[i] <= 0.7:
        observed_counts[6] +=1
    if 0.7 < numbers_array[i] <= 0.8:
        observed_counts[7] +=1
    if 0.8 < numbers_array[i] <= 0.9:
        observed_counts[8] +=1
    if 0.9 < numbers_array[i] <= 1:
        observed_counts[9] +=1


print("\nObserved Count List: ",observed_counts)

for interval in range(no_of_intervals):

    # diff = Oi - Ei
    diff = observed_counts[interval] - Ei
    X02_interval = (diff**2)/Ei
    X0_2 += X02_interval

    print("i:{}  Oi: {}  Ei: {}  diff: {}  diff2: {}  X02: {}".format(
        interval + 1 ,
        observed_counts[interval],
        Ei,
        diff,
        diff**2,
        X02_interval)
        )

    
print()
print("XO2: ",round(X0_2,4))
check_hyp(X0_2,X0_2_critical)



# for i in range(10):
#     print(i/10,"-",(i+1)/10)
