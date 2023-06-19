def display_tasks(iteration):
    task_display = "\n"
    for task in iteration.tasks:
        text = "Task {id}: {name} | Assignee: {ass} | Complexity: {comp} | Status: {stat}\n"
        task_display += text.format(id=task.id, name=task.name, ass=task.assignment, comp=task.complexity, stat=task.status)
    print(task_display)

def choose_task(max_id, correct_type=True):
    task_id = input("Choose task by typing its Id: ")
    if int(task_id) >= 0 and int(task_id) <= max_id:
        print("INFO: Task nr " + task_id + " chosen! ")
        correct_type = True
        return int(task_id)
    else: 
        print("WARNING: Wrong Id!")
        correct_type = False
        if correct_type == False: 
            choose_task(max_id)

def choose_status(task):
    task_status = input("Select status of this task - type in corresponding number: \n(1) To Do\n(2) Doing\n(3) Done\n")
    if task_status == "1":
        task.status = "To Do"
    elif task_status == "2":
        task.status = "Doing"
    elif task_status == "3":
        task.status = "Done"
    else:
        print = ("WARNING: Choose by typing in a status corresponding number - 1 / 2 / 3")
        return task.status
    return task.status

def choose_request():
    request = input("Do you want to select a new task? (Y/N): ")
    if request.upper() == "Y":
        return True
    else:
        return False

def exe_task_loop(iteration):
    status_select_request = True
    display_tasks(iteration)
    while status_select_request == True:
        task_id = choose_task(len(iteration.tasks))
        task = iteration.tasks[task_id]
        task.status = choose_status(task)
        status_select_request = choose_request()
        display_tasks(iteration)

