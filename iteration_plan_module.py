import iteration_class_control as iteration_cc

def input_iteration_info(sprint):
    all_valid = False
    while all_valid == False:
        input_name = input("Enter the name of the iteration (max 80 characters): ")
        input_goal = input("Enter the goal of the iteration (max 80 characters): ")
        input_sprint = sprint
        if iteration_cc.Iteration.check_input_info(input_sprint, input_name, input_goal):
            all_valid=True
        else:
            print("Something is wrong")
    return input_sprint, input_name, input_goal
