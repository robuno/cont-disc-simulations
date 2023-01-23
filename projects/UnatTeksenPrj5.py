def linear_cong_method(x0, a, c, m):
    number_array = []
    REPS = 100
    start_index = 1
    for REP in range(start_index, start_index + REPS):
        #print("X0: {},   a: {},   c: {}".format(x0, a, c))
        x_new = (a*x0 + c) % m 
        R = x_new / m 
        number_array.append(round(R,3))
        #print("X{}: {}".format(REP, x_new))
        #print("R{}: {}".format(REP,R))
        x0 = x_new
        #print()
    return number_array

def print_array(array_list, divider):
    for i in range(len(array_list)):
        if i % divider == 0:
            print()
        print(array_list[i],end="  ")

def calc_z0(a, mean_val, dev_val):
    return (a-mean_val) / ((dev_val)**(1/2))

def check_hypo(critical_val, Z0):
    if -critical_val <= Z0 <= critical_val:
        print("{} <= {} <= {}".format(-critical_val,Z0,critical_val))
        print("Independence of the numbers cannot be rejected!")
    else:
        print("Hyp. is rejected!")


# X0 = int(input("x0: "))
# a = int(input("a: "))
# c = int(input("c: "))
# m = int(input("m: "))

X0 = 123457
a = 16807
c = 0
m = 2147483647

number_array = linear_cong_method(X0, a, c, m)
Z_critical = 1.96
N = len(number_array)

mean_val = (2*N-1)/3
variance_val = (16*N-29)/90

up_down_array = []
no_of_runs = 1

# create list of up downs for each element
for i in range(1,len(number_array)):
    first_val = number_array[i-1]
    second_val = number_array[i]

    if (second_val < first_val):
        up_down_array.append(-1)
    
    if (first_val < second_val):
        up_down_array.append(1)

# determine the number of groups
for i in range(1,len(up_down_array)):
    first_sign = up_down_array[i-1]
    second_sign = up_down_array[i]

    if second_sign != first_sign:
        no_of_runs +=1


print("Random Numbers:")
print_array(number_array,10)
print()

print(number_array)

# print_array(up_down_array,10)
# print()

print()
print("Number of runs: ", no_of_runs)
print()

print("mean: ",round(mean_val,2))
print("variance: ", round(variance_val,2))
print()

Z0 = calc_z0(no_of_runs, mean_val, variance_val)
print("Z0: ",Z0)
check_hypo(Z_critical, round(Z0,3))
