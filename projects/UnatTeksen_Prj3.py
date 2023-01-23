import random
import math

# lambda1 = int(input("Type rate lambda1: ")) # arrival rate for road1
# lambda2 = int(input("Type rate lambda2: ")) # arrival rate for road2
# lambda3 = int(input("Type rate lambda3: ")) # arrival rate for road3
# mu = int(input("Type rate mu: ")) # service rate foor toll booth

# debug_input = input("Debug mode (True/False): ") # show table
# if debug_input == "True":
#   debug_mode = True
# elif debug_input == "False":
#   debug_mode = False

lambda1 = 5 # arrival rate for road1
lambda2 = 3 # arrival rate for road2
lambda3 = 2 # arrival rate for road3
mu = 12 # service rate foor toll booth
debug_input = "True" # show table
if debug_input == "True":
  debug_mode = True
elif debug_input == "False":
  debug_mode = False

TABLE_CAR_NUMBER = 20 # number of rows to display
NUMBER_OF_CARS = 1000000 # iteration number

sum_waiting_queue = 0 
sum_waiting_system = 0
sum_arrivals = 0
sum_service_time = 0

sum_waited_customers = 0 # number of cars waited in queue
sum_idle_time = 0 # sum of idle time of toll booth
time_service_ends = 0 # time when last car left the system

sum_cars_from_road1 = 0 # number of cars coming from road 1
sum_cars_from_road2 = 0 # number of cars coming from road 2
sum_cars_from_road3 = 0 # number of cars coming from road 3

car_to_change_time = 0 # the road the service vehicle came

# exponential random variable generator with inverse transformation
def exp_var_creator(a, y_max =1):
  uniform_rv = random.uniform(0,y_max) # create uniform r.v. [0,1)
  return (-1/a)*(math.log(1-uniform_rv)) # generate exp. r.v. 


for CAR in range(1,NUMBER_OF_CARS+1):
  service_time = exp_var_creator(mu) # set service time for each car

  if CAR == 1:
    time_inter_arrival1 = exp_var_creator(lambda1) # set interarrival for road1's car
    time_inter_arrival2 = exp_var_creator(lambda2) # set interarrival for road2's car
    time_inter_arrival3 = exp_var_creator(lambda3) # set interarrival for road3's car

    # arrival times of vehicles to the toll booth
    arrival_time1, arrival_time2, arrival_time3 = 0, 0, 0

    # determine first arrival time
    first_arrival = min(time_inter_arrival1, time_inter_arrival2, time_inter_arrival3)

    # determine interarrival time for the car which arrives first
    inter_arrival = first_arrival

    first_arrival_PRINT = 0 # assume 0 for the first car
    inter_arrival_PRINT = 0 # assume 0 for the first car

    # check which road's car arrives first
    if (first_arrival == time_inter_arrival1):
      car_to_change_time = 1 # determine which car's interarrival will change
      sum_cars_from_road1 +=1

    if (first_arrival == time_inter_arrival2):
      car_to_change_time = 2 # determine which car's interarrival will change
      sum_cars_from_road2 +=1

    if (first_arrival == time_inter_arrival3):
      car_to_change_time = 3 # determine which car's interarrival will change
      sum_cars_from_road3 +=1

    time_service_begins = 0 # assume service starts to work @t=0
    idle_time = 0 # assume service is empty at the beginning

    if(debug_mode):
      print ("{:>3} {:>18} {:>14} {:>13} {:>21} {:>22} {:>20} {:>14} {:>12} {:>6}".format(
        "Car #", 
        "interarrival time", 
        "arrival time", 
        "service time", 
        "time service begins",
        "waiting time in queue",
        "time service ends",
        "time in sys",
        "idle time",
        "Road"))



  
  if CAR != 1:
    inter_arrival_PRINT = first_arrival # get first arrival time

    if (CAR == 2):
      arrival_time1 += time_inter_arrival1
      arrival_time2 += time_inter_arrival2
      arrival_time3 += time_inter_arrival3


    # if 1st road's car arrived first, set new interarrival for the next car
    if(car_to_change_time == 1):
      time_inter_arrival1 = exp_var_creator(lambda1)
      arrival_time1 += time_inter_arrival1

    # if 2nd road's car arrived first, set new interarrival for the next car
    if(car_to_change_time == 2):
      time_inter_arrival2 = exp_var_creator(lambda2)
      arrival_time2 += time_inter_arrival2

    # if 3rd road's car arrived first, set new interarrival for the next car
    if(car_to_change_time == 3):
      time_inter_arrival3 = exp_var_creator(lambda3)
      arrival_time3 += time_inter_arrival3


    # check which car arrives first
    first_arrival_PRINT = min(arrival_time1, arrival_time2, arrival_time3)


    # if road 1's car arrives first
    if (first_arrival_PRINT == arrival_time1):
      car_to_change_time = 1
      sum_cars_from_road1 +=1
      inter_arrival_PRINT = time_inter_arrival1 # set interarrival time of the road1's car

    # if road 2's car arrives first
    if (first_arrival_PRINT == arrival_time2):
      car_to_change_time = 2
      sum_cars_from_road2 +=1
      inter_arrival_PRINT = time_inter_arrival2 # set interarrival time of the road2's car

    # if road 3's car arrives first
    if (first_arrival_PRINT == arrival_time3):
      car_to_change_time = 3
      sum_cars_from_road3 +=1
      inter_arrival_PRINT = time_inter_arrival3 # set interarrival time of the road3's car
    
    # determining when the arriving car will enter service
    time_service_begins = max(first_arrival_PRINT,time_service_ends)

    # if service is empty and waits new car, calculate its empty time period
    idle_time = time_service_begins - time_service_ends
  

  sum_arrivals += inter_arrival_PRINT # sum of all times between arrivals
  sum_service_time += service_time # total time spent in service
  sum_idle_time += idle_time # total empty time for toll booth

  # time when the car will leave the system
  time_service_ends = time_service_begins + service_time

  # if car came earlier than the end time of the previous car's service
  waiting_time_in_queue = time_service_begins - first_arrival_PRINT

  if waiting_time_in_queue !=0:
    sum_waited_customers += 1 # add customers who spent time in queue

  sum_waiting_queue +=waiting_time_in_queue
  
  # the difference between when the car left the service and enter the system
  time_in_system = time_service_ends - first_arrival_PRINT
  sum_waiting_system += time_in_system

  # print rows with more specific details
  if (debug_mode) and ( CAR <= TABLE_CAR_NUMBER ):
    print ("{:>3} {:>20} {:>14} {:>13} {:>21} {:>22} {:>20} {:>14} {:>12} {:>6}".format(
          round(CAR,3), 
          round(inter_arrival_PRINT,3),
          round(first_arrival_PRINT,3), 
          round(service_time,3), 
          round(time_service_begins,3),
          round(waiting_time_in_queue,3),
          round(time_service_ends,3),
          round(time_in_system,3),
          round(idle_time,3),
          str(car_to_change_time)
          + " "+ str([round(arrival_time1,2), 
                    round(arrival_time2,2), 
                    round(arrival_time3,2)]))+ 
          " "+ str([round(time_inter_arrival1,2), 
                    round(time_inter_arrival2,2), 
                    round(time_inter_arrival3,2)]
          ))


print()
print("Average waiting time in the queue: ", sum_waiting_queue / NUMBER_OF_CARS)
print("Average waiting time in the system: ", sum_waiting_system / NUMBER_OF_CARS)
print("Average waiting time between arrivals: ", sum_arrivals / (NUMBER_OF_CARS-1))
print("Average service time: ", sum_service_time / NUMBER_OF_CARS)

print()
print("Probability (wait in queue): ", sum_waited_customers / NUMBER_OF_CARS )
print("Probability (idle time): ", sum_idle_time / time_service_ends ) 

if (sum_waited_customers !=0):
  print("Average waiting time of those who wait: ", sum_waiting_queue / sum_waited_customers)
if (sum_waited_customers ==0):
  print("Average waiting time of those who wait: ", sum_waiting_queue)

print()
print("road1: ",sum_cars_from_road1, "  road2: ",sum_cars_from_road2, "  road3: ",sum_cars_from_road3,)
print("Rate coming from road1 (%): ", (sum_cars_from_road1/NUMBER_OF_CARS)*100)
print("Rate coming from road2 (%): ", (sum_cars_from_road2/NUMBER_OF_CARS)*100)
print("Rate coming from road3 (%): ", (sum_cars_from_road3/NUMBER_OF_CARS)*100)
print("Checksum: ", sum_cars_from_road1 + sum_cars_from_road2 + sum_cars_from_road3)
print("Number of cars: ", NUMBER_OF_CARS)
