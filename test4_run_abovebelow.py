number_array = [
    0.63, 0.72, 0.79, 0.81, 0.52, 0.94, 0.83, 0.93, 0.87, 0.67,
    0.31, 0.45, 0.49, 0.43, 0.46, 0.35, 0.25, 0.39, 0.47, 0.41
    ]

def print_array(array_list, divider):
    for i in range(len(array_list)):
        if i % divider == 0:
            print()
        print(array_list[i],end=" ")


def calc_z0(runs,mean_val,var_val):
    return (runs-mean_val) / var_val

def check_hypo(critical_val, Z0):
    if -critical_val <= Z0 <= critical_val:
        print("{} <= {} <= {}".format(-critical_val,Z0,critical_val))
        print("Independence of the numbers cannot be rejected!")
    else:
        print("Rejected!")

Z_critical = 1.96

N = len(number_array)
n1 = 0
n2 = 0


for i in range(len(number_array)):
    if number_array[i] > 0.5:
        n1 +=1
    else:
        n2 +=1



mean_val = ((2*n1*n2)/N) + 1/2
variance_val =( 2*n1*n2*(2*n1*n2-N)) / ((N**2)*(N-1) )


up_down_array = []
no_of_runs = 1

for i in range(1,len(number_array)):
    if number_array[i-1] > 0.5:
        up_down_array.append(1)
    else:
        up_down_array.append(-1)

# determine the number of groups
for i in range(1,len(up_down_array)):
    first_sign = up_down_array[i-1]
    second_sign = up_down_array[i]

    if second_sign != first_sign:
        no_of_runs +=1



print_array(number_array,10)
print()

print_array(up_down_array,10)
print()


print("n1: {}   n2: {}".format(n1, n2))
print()

print("mean: ",mean_val)
print("variance: ", variance_val)
print()

print("Number of runs: ", no_of_runs)
print()

print("Z0 ", calc_z0(no_of_runs,mean_val,variance_val))
print()

