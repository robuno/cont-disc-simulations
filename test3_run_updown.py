number_array = [
    0.41, 0.68, 0.89, 0.94, 0.74, 0.91, 0.55, 0.62, 0.36, 0.27,
    0.19, 0.72, 0.75, 0.08, 0.54, 0.02, 0.01, 0.36, 0.16, 0.28,
    0.18, 0.01, 0.95, 0.69, 0.18, 0.47, 0.23, 0.32, 0.82, 0.53,
    0.31, 0.42, 0.73, 0.04, 0.83, 0.45, 0.13, 0.57, 0.63, 0.29
    ]


number_array = [0.966, 0.261, 0.766, 0.569, 0.845, 0.044, 0.987, 0.601, 0.896, 0.381, 0.016, 0.587, 0.489, 0.169, 0.213, 0.197, 0.09, 0.395, 0.346, 0.142, 0.566, 0.899, 0.289, 0.898, 0.226, 0.046, 0.71, 0.873, 0.033, 0.887, 0.479, 0.683, 0.659, 0.826, 0.461, 0.813, 0.66, 0.169, 0.503, 0.616, 0.68, 0.711, 0.485, 0.051, 0.529, 0.581, 0.727, 0.288, 0.954, 0.043, 0.146, 0.331, 0.918, 0.174, 0.777, 0.479, 0.977, 0.952, 0.105, 0.09, 0.757, 0.883, 0.857, 0.85, 0.875, 0.88, 0.402, 0.611, 0.131, 0.84, 0.796, 0.037, 0.688, 0.16, 0.024, 0.088, 0.562, 0.218, 0.266, 0.143, 0.84, 0.233, 0.979, 0.626, 0.186, 0.542, 0.07, 0.189, 0.071, 0.46, 0.54, 0.574, 0.289, 0.231, 0.11, 0.345, 0.256, 0.379, 0.102, 0.373]


def print_array(array_list, divider):
    for i in range(len(array_list)):
        if i % divider == 0:
            print()
        print(array_list[i],end=" ")

def calc_z0(a, mean_val, dev_val):
    return (a-mean_val)/(dev_val)**(1/2)

def check_hypo(critical_val, Z0):
    if -critical_val <= Z0 <= critical_val:
        print("{} <= {} <= {}".format(-critical_val,Z0,critical_val))
        print("Independence of the numbers cannot be rejected!")
    else:
        print("Rejected!")

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




print_array(number_array,10)
print()

print_array(up_down_array,10)
print()

print("Number of runs: ", no_of_runs)
print()

Z0 = calc_z0(no_of_runs, mean_val, variance_val)
print("Z0: ",Z0)
check_hypo(Z_critical, Z0)