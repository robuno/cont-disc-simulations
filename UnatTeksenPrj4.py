import random

"""
CE 412 - PROJECT 4
“Simulation of a Grocery Store with DES”

Unat Teksen, 20181701048
November 29, 2022
"""

end_time = int(input("End time for stopping event: "))
debug_input = input("Debug mode (True, t /False, f): ") # show table

# end_time = 60
# debug_input = "True"

# print first row for column names
def print_debug_first():
    print ("{:>3} {:>7} {:>8} {:>62} {:>22} {:>15} {:>15} {:>10}".format(
        "Clock", 
        "Lq(t)", 
        "Ls(t)", 
        "FEL", 
        "Imm. Event",
        "Service Util",
        "Service Idle",
        "MQ"))

# print event rows
def print_debug_event(clock, state_queue, state_service, 
                    FEL, last_event, service_util_cumul, service_idle_cumul, max_queue_cumul):
    print ("{:>3} {:>7} {:>8} {:>64} {:>22} {:>15} {:>15} {:>10}".format(
        clock, 
        state_queue, 
        state_service, 
        str(FEL), 
        str(last_event),
        service_util_cumul,
        service_idle_cumul,
        max_queue_cumul))
    

clock = 0 # initial clock
state_queue = 0 # Ls(t)
state_service = 1 # Lq(t)
FEL = [] # future event list
service_util_cumul = 0 # cumulative service utilization
max_queue_cumul = 0 # max queue length
last_event = "-"

service_idle_cumul = 0 # cumulative service utilization

FEL.append(["E",end_time]) # add stopping event to FEL

# get interarrival time for arriving event from distribution
def get_arrival_from_dist():
    assigned_digit = random.randint(1,1000)
    if 1 <= assigned_digit <= 125: # prob: 12.5%
        return 1
    if 126 <= assigned_digit <= 250: # prob: 12.5%
        return 2
    if 251 <= assigned_digit <= 375: # prob: 12.5%
        return 3
    if 376 <= assigned_digit <= 500: # prob: 12.5%
        return 4
    if 501 <= assigned_digit <= 625: # prob: 12.5%
        return 5
    if 626 <= assigned_digit <= 750: # prob: 12.5%
        return 6
    if 751 <= assigned_digit <= 875: # prob: 12.5%
        return 7
    if 876 <= assigned_digit <= 1000: # prob: 12.5%
        return 8

# get service time for departure event from distribution
def get_service_t_from_dist():
    assigned_digit = random.randint(1,100)
    if 1 <= assigned_digit <= 10: # prob: 10%
        return 1
    if 11 <= assigned_digit <= 30: # prob: 20%
        return 2
    if 31 <= assigned_digit <= 60: # prob: 30%
        return 3
    if 61 <= assigned_digit <= 85: # prob: 25%
        return 4
    if 85 <= assigned_digit <= 95: # prob: 10%
        return 5
    if 96 <= assigned_digit <= 100: # prob: 5%
        return 6

# create arrival event
def add_arrival(arrival_time):
    sub_list_arrival = ["A",arrival_time]
    FEL.append(sub_list_arrival)

# create departure event
def add_departure(departure_time):
    sub_list_departure = ["D",departure_time]
    FEL.append(sub_list_departure)


# returns chronological order in event list
def sort_FEL(FEL):
    FEL.sort(key = lambda i: i[1])
    return FEL


# run it until reach end time
while clock <= end_time:

    # create initial FEL
    if clock == 0:
        inter_arrival = get_arrival_from_dist()
        service_time = get_service_t_from_dist()

        add_arrival(inter_arrival)
        add_departure(service_time)
        FEL = sort_FEL(FEL)

        # print(FEL)
        if (debug_input == "True") or (debug_input == "t"):
            print_debug_first()


    # execute imminent event
    new_event = FEL[0][0] # get new event
    new_clock = FEL[0][1] # get new event time

    # update max length among events 
    max_queue_cumul = max(max_queue_cumul, state_queue) 

    if (debug_input == "True") or (debug_input == "t"):
        print_debug_event(clock, state_queue, state_service, FEL, FEL[0], service_util_cumul, service_idle_cumul, max_queue_cumul)
    
    del FEL[0] # remove imminent event from FEL

    # if service is full, add service's working time to utilization time
    if (state_service == 1) and (new_clock <= end_time):
        service_util_cumul += new_clock-clock

    if (state_service == 0) and (new_clock <= end_time):
        service_idle_cumul += new_clock-clock




    # if "Arrival Event" is the next event
    if new_event == "A":
        inter_arrival = get_arrival_from_dist()
        service_time = get_service_t_from_dist()

        if state_service == 1: # if service is full
            state_queue +=1 # add next customer to the queue
            add_arrival(new_clock+inter_arrival) # create new arrival event
            FEL = sort_FEL(FEL)
            
        if state_service == 0: # if service is empty
            state_service +=1 # send customer to the service directly
            add_arrival(inter_arrival+new_clock) # create new arrival event
            add_departure(service_time+new_clock) # create new departure event
            FEL = sort_FEL(FEL)

    # if "Departure Event" is the next event
    if new_event == "D":
        inter_arrival = get_arrival_from_dist()
        service_time = get_service_t_from_dist()
        
        if state_queue == 0: # if no waiting customer in queue
            state_service = 0 # departure from service
        if state_queue > 0: # if customers wait in queue
            state_queue -= 1 # update queue
            add_departure(service_time+new_clock) # add departure event
            FEL = sort_FEL(FEL)


    clock = new_clock # advance CLOCK to imminent event time

print("\nMax Queue Length: ", max_queue_cumul)
print("Cumulative Service Utilization (m): ", service_util_cumul)
print("Service Util (%): ", (service_util_cumul/end_time)*100)
print("Service IDLE (%): ", ((end_time-service_util_cumul)/end_time)*100)