# 2 midproduct methods

import random

x0 = int(random.random()*1000)
x0p = int(random.random()*1000)

x0 = 2938
x0p = 7229


REPS = 3

for REP in range(REPS):

    print("##### REPS: ", REP)
    print("x0: ",x0,"     x0p: ",x0p)

    U = x0* x0p

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

