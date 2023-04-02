#ITERATION PLAN MODULE
import iteration_class_control as iteration_cc
import sprint_class_control as sprint_cc

def check_input(name, goal):
    check_name = len(name) < 80
    check_goal = len(goal) < 80
    check_all =  check_name and check_goal
    if check_all:
        print("INFO: All conditions correct\n")
        return True
    else:
        print("WARNING: All iteration details must match these criteria:\nIteration name maximum 80 chars\nIteration goal maximum 80 chars")
        return False

def check_type(name, goal):
    try:
        name, goal = str(name), str(goal)
        print("\nINFO: All types correct")
        return True
    except ValueError:
        print("\nWARNING: All iteration details must be correct data types: \Iteration name - String\nIteration goal - String")
        return False

def check_both(name, goal):
    if check_type(name, goal):
        return check_input(name, goal)
    else:
        return False

def input_iteration():
    all_valid = False
    while all_valid == False:
        name = input("\nEnter the name of the iteration (max 80 characters): ")
        goal = input("Enter the goal of the iteration (max 80 characters): ")
        all_valid=check_both(name, goal)
    return name, goal

def add_iteration_loop(sprint):
    for index in range(sprint.iterations_count):
        print("\nINFO: Planning iteration no. {num}".format(num=index+1))
        print("==================================")
        name, goal = input_iteration()
        iteration_cc.Iteration.add_iteration(sprint, name, goal, index)
