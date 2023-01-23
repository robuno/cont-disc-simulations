numbers_array = [
    0.12, 0.01, 0.23, 0.28, 0.89, 0.31, 0.64, 0.28, 0.83, 0.93,
    0.99, 0.15, 0.33, 0.35, 0.91, 0.41, 0.60, 0.27, 0.75, 0.88,
    0.68, 0.49, 0.05, 0.43, 0.95, 0.58, 0.19, 0.36, 0.69, 0.87
]

def calc_z0(var_sqr_val, autocorr):
    return autocorr / var_sqr_val

def calc_var_sqr(M,round_choice):
    if round_choice==False:
        return ((13*M+7)**(1/2)) / (12*(M+1))
    if round_choice==True:
        return round(((13*M+7)**(1/2)) / (12*(M+1)),4)

def calc_autocorr(M, sum):
    return ((1/(M+1))*sum) - 0.25

def check_hypo(critical_val, Z0):
    if -critical_val <= Z0 <= critical_val:
        print("{} <= {} <= {}".format(-critical_val,Z0,critical_val))
        print("Independence of the numbers cannot be rejected!")
    else:
        print("Rejected!")

i = 3
m = 5 # for 5 numbers
N = len(numbers_array)
M = 4 
critical_Z0 = 1.96

var_sqr = calc_var_sqr(M,True)


sum_multiply = 0
k = 0
while i+m*(k+1) <= N:
    val1_index = i + (m*k)
    val2_index = i + (m*(k+1))
    print(val1_index,"-",val2_index)
    sum_multiply += (numbers_array[val1_index-1] * numbers_array[val2_index-1])
    k+=1



autocorr_val = calc_autocorr(M,sum_multiply)
Z0 = calc_z0(var_sqr,autocorr_val)

print()
print("sum: ",sum_multiply)
print("Var sqr: ",var_sqr)
print("Autocorr: ",autocorr_val)
print("Z0: ",Z0)
check_hypo(critical_Z0,Z0)

