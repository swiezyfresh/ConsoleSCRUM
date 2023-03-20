# SPRINT PLAN MODULE

# IMPORT Sprint Class
import sprint_class_control as sprint_cc

#CREATE a GLOBAL list containing all instances of Sprint
sprint_list=[]

#CHECK if user added at least 1 Sprint instance
def check_sprints(sprint_list_to_check):
    sprint_list_length = len(sprint_list_to_check)
    if sprint_list_length > 0:
        return True
    else:
        print("Then why would you even start this app?")
        return False

#CHECK if input values for Sprint instance are correct
def input_sprint_info():
    #DECLARE variable CONDITION which keeps the loop running untill all values are correct
    all_valid = False
    #LOOP through single input series untill all values are correct
    while all_valid == False:
        #ASSIGN user inputs to es (enter_sprint) variables
        es_name = input("Enter the name of the sprint (max 80 characters): ")
        es_time_total = input("Enter total duration in months of the sprint (1,...,6): ")
        es_time_unit = input("Enter iteration duration in weeks for the sprint (1, 2, 4): ")
        #CHECK if inputs are correct data types
        try:
            es_time_total, es_time_unit = int(es_time_total), int(es_time_unit)
            #CHECK if inputs match requirements
            if sprint_cc.Sprint.check_input_info(es_name, es_time_total, es_time_unit):
                all_valid = True
            else:
                print("\nWARNING: All sprint details must match these criteria:\nSprint name maximum 80 chars\nSprint duration between 1 and 6 months\nIteration duration 1, 2 or 4 weeks\n")
        except ValueError:
            print("\nWARNING: Sprint and iteration duration must be integers\n")
    return es_name, es_time_total, es_time_unit

#LOOP untill user doesn't want to add Sprint instances anymore
#APPEND new Sprint instance to the sprint_list
def add_sprints():
    #CREATE a LOCAL list containing all instances of Sprint
    loc_sprint_list = []
    #DECLARE variable CONDITION which keeps the loop running untill user doesn't want to add new Sprint instances
    new_sprint_request = True
    while(new_sprint_request):
        #RUN the input_sprint_info function to add new sprint
        #ASSIGN results of the function to ns (new_sprint) variables
        ns_name, ns_time_total, ns_time_unit = input_sprint_info()
        #CREATE new Sprint instance
        new_sprint = sprint_cc.Sprint(ns_name,ns_time_total, ns_time_unit)
        #APPEND new Sprint instance to LOCAL Sprint list
        loc_sprint_list.append(new_sprint)
        #CHECK if the user wants to add new Sprint instances
        request_choice = input("Do you want to add a new sprint? (Y/N)")
        if request_choice == "N":
            new_sprint_request = False
    return loc_sprint_list

#RUN add_sprint function to start appending new sprints to the table
#ASSIGN returned LOCAL Sprint instance list to GLOBAL Sprint instance list
sprint_list = add_sprints()
print(sprint_list)