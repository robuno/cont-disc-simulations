# 3 constant multiplier method

import random

x0 = int(random.random()*1000)
K = int(random.random()*1000)

x0 = 7223
K = 3987


REPS = 3

for REP in range(REPS):

    x0sqr = x0**2

    print("##### REPS: ", REP)
    print("x0: ",x0,"     K: ",K)

    U = x0* K

    str_xsqr = str(U)
    len_xsqr = len(str_xsqr)

    print("len previous: ", len(str(str_xsqr)) )

    if len_xsqr < 8:
        no_of_zeros = 8 - len_xsqr
        for i in range(no_of_zeros):
            str_xsqr = "0" + str_xsqr

    print("len new: ", len(str(str_xsqr)),"   new str: ", str(str_xsqr))

    middle4 = str_xsqr[2:6]
    print("middle 4: ", middle4, "    int: ",int(middle4))

    x0 = int(middle4)
    print("R{}: {}".format(REP,(x0 /10000)))
    print()

