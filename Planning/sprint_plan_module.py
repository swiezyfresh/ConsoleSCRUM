# SPRINT PLAN MODULE
import Class_Control.sprint_class_control as sprint_cc
  
def check_input(name, time_total, time_unit):
    check_name = len(name) <= 80
    check_time_total = int(time_total) <= 6
    check_time_unit = int(time_unit) in range(1,5) and int(time_unit) != 3
    check_all = check_name and check_time_total and check_time_unit

    if check_all:
        print("INFO: All conditions correct\n")
        return True
    else:
        print("WARNING: All sprint details must match these criteria:\nSprint name maximum 80 chars\nSprint duration 1:6 months\nIteration duration 1, 2, 4 weeks")
        return False

def check_types(name, time_total, time_unit):
    try:
        name, time_total, time_unit = str(name), int(time_total), int(time_unit)
        print("\nINFO: All types correct")
        return True
    except ValueError:
        print("\nWARNING: All sprint details must be correct data types: \nSprint name - String\nSprint duration - Integer\nIteration duration - Integer")
        return False

def check_both(name, time_total, time_unit):
    if check_types(name, time_total, time_unit):
        return check_input(name, time_total, time_unit)
    else:
        return False
    
def input_sprint():
    all_valid = False
    while all_valid == False:
        name = input("\nEnter the name of the sprint (max 80 characters): ")
        time_total = input("Enter total duration in months of the sprint (1,...,6): ")
        time_unit = input("Enter iteration duration in weeks for the sprint (1, 2, 4): ")
        all_valid = check_both(name, time_total, time_unit)
    return name, int(time_total), int(time_unit)


def add_sprint_loop():
    new_sprint_request = True
    while(new_sprint_request):
        name, time_total, time_unit = input_sprint()
        sprint_cc.Sprint.add_sprint(name, time_total, time_unit)

        request_choice = input("Do you want to add a new sprint? (Y/N)")
        if request_choice.upper() == "N":
            if sprint_cc.Sprint.check_list:
                new_sprint_request = False
            else:
                print("\nThen why would you even start this app? GOODBYE!")
                break