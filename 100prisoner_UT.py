import random
import time

NO_OF_PEOPLE = 100
box_list = []
for i in range(1,NO_OF_PEOPLE +1):
    box_list.append(i)

# print("Initial box list: ", box_list)

REPS = 10000
no_of_freedoms = 0

start_time = time.time()

for REPETITION in range(1,REPS+1):
    random.shuffle(box_list) 
    # print(REPETITION, " => ",box_list)

    person_failed = False

    person = 1
    while (person < NO_OF_PEOPLE +1) and (person_failed != True):
        # print("********\nperson: ",person)
        box_value = box_list[person-1]
        opened_boxes = 0

        while (opened_boxes <= (NO_OF_PEOPLE //2)+1): 
            opened_boxes +=1
            # print(opened_boxes," box value: ", box_value )
            if (box_value == person):
                # print("person found his number!")
                break
            if (opened_boxes == NO_OF_PEOPLE //2):
                person_failed = True
                # print("one couldnt't find!")
                break
            else:
                box_value = box_list[box_value-1]
    
        if person == NO_OF_PEOPLE and person_failed==False:
            no_of_freedoms +=1

        person +=1
    # print("# freedoms: ", no_of_freedoms)
    # print("**********************************************")


   
end_time = time.time()

prob = no_of_freedoms/REPS
print()
print("Probability(%): ",prob * 100)
print("time: ",end_time -  start_time)

