import Class_Control.task_class_control as task_cc

def check_input(name, assignment, complexity):
    check_name = len(name) < 140
    check_assignment = len(assignment) < 80
    check_complexity = int(complexity) in range(1,6)
    check_all = check_name and check_assignment and check_complexity
    if check_all:
        return True
    else:
        print("WARNING: All task details must match these criteria:\nName maximum 140 chars\nAssignment maximum 80 chars\nComplexity between 1...5")
        return False
def check_type(name, assignment, complexity):
    try:
        name, assignment, complexity = str(name), str(assignment), int(complexity)
        return True
    except ValueError:
        print("WARNING: All task details must be correct types:\nName - Text\nAssignment - Text\nComplexity - Integer")
        return False
def check_both(name, assignment, complexity):
    if check_type(name, assignment, complexity):
        return check_input(name, assignment, complexity)
    else:
        return False

def input_task():
    all_valid = False
    while all_valid == False:
        name = input("\nEnter task name (max 140 characters): ")
        assignment = input("Enter task assignment (max 80 characters): ")
        complexity = input("Enter task complexity (from 1...5 range): ")
        all_valid = check_both(name, assignment, complexity)
    return name, assignment, complexity

def add_task_loop(iteration):
    new_task_request = True
    new_task_counter = 0
    while new_task_request:
        new_task_counter += 1
        name, assignment, complexity = input_task()
        new_task = task_cc.Task.add_task(name, new_task_counter, assignment, complexity, iteration)
        print("\nNEW: TASK {num}, {name}, ASSIGNMENT: {ass}, COMPLEXITY: {cpx}\n".format(num=new_task.number, name=new_task.name, ass=new_task.assignment, cpx=new_task.complexity))
        request_choice = input("Do you want to add a new task? (Y/N)")
        if request_choice.upper() == "N":
            if iteration.check_tasks_list():
                new_task_request = False
            else:
                print("\nINFO: You need to add at least 1 task!")
