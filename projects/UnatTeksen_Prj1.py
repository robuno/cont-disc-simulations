import random
import time

NO_OF_PEOPLE = 100
box_list = []
for i in range(1,NO_OF_PEOPLE +1):
    box_list.append(i)

# print("Initial box list: ", box_list)

REPS = 1000
no_of_freedoms = 0

start_time = time.time()
for REPETITION in range(1,REPS+1):
    random.shuffle(box_list)
    print("*****************************")
    print("Iteration: ", REPETITION, "    Shuffled box list: ",box_list)

    not_found_in_rep = 0

    for person in range(1,NO_OF_PEOPLE+1):

        print("person: ", person)
        print(box_list[person-1])
        next_index= person
        for open_box_iter in range(NO_OF_PEOPLE//2):
            if (box_list[next_index-1] == person):
                
                print("person ",person," found his number!")
                break
            else:
                next_index = box_list[next_index-1] 
                print(open_box_iter, "  next index: ",next_index, "next box value: ", box_list[next_index-1])
                if (open_box_iter==((NO_OF_PEOPLE//2)-1)) and (box_list[next_index-1] !=person):
                    not_found_in_rep = 1
                    print("one couldn't cant find his number!  ",not_found_in_rep)
                    break
        if (not_found_in_rep==1): 
            break

    if( not_found_in_rep ==0):
        no_of_freedoms +=1                


prob = no_of_freedoms/REPS

end_time = time.time()
print()
print("Probability(%): ",prob * 100)
print()
print("Elapsed time: ", end_time - start_time)
