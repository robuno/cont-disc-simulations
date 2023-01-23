# numbers_array =[
#     0.44, 0.81, 0.14, 0.05, 0.93
#     ]

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

numbers_array =[
   0.27, 0.02, 0.77, 0.52, 0.27
    ]

N = len(numbers_array)

numbers_array = sorted(numbers_array, key=float)

Dplus_max = 0
Dminus_max = 0
D_max = 0

D_critical = 0.56

def check_hyp(D_max, D_critical):
    if (D_max <D_critical):
        print("{} < {}".format(D_max,D_critical))
        print("We don't have enough evidence to reject the null hypothesis")
    else:
        print("Rejected")

for i in range(1, N+1):

    R = numbers_array[i-1]
    i_div_N = i/N

    i_div_N_minus_R = (i/N) - R
    if (i_div_N_minus_R < 0):
        i_div_N_minus_R = 0

    R_minus_prev_i = R - ((i-1)/N)
    if (R_minus_prev_i < 0):
        R_minus_prev_i = 0

    Dplus_max = max(Dplus_max, i_div_N_minus_R)
    Dminus_max = max(Dminus_max, R_minus_prev_i)

    print( "i: {}    R:{}   i/N: {}  (i/N)-R: {}   R-(prev_i/N): {}"
                                            .format(i, 
                                            R, 
                                            i_div_N,
                                            round(i_div_N_minus_R,2),
                                            round(R_minus_prev_i,2)
                                            ) )


D_max = max(Dplus_max, Dminus_max)

print()
print("D+: {}".format(Dplus_max))
print("D-: {}".format(Dminus_max))
print("Dmax: {}".format(D_max))
check_hyp(D_max,D_critical)