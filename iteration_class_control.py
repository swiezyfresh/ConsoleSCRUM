#ITERATION CLASS CONTROL

class Iteration:
    
    def __init__(self, input_sprint, input_name, input_goal, input_index):
        self.sprint = input_sprint
        self.name = input_name
        self.goal = input_goal
        self.index = input_index
        self.tasks = []
    def __repr__(self):
        info = "Iteration {index}\nName: {name}\nGoal: {goal}\nTasks: {tasks}".format(index=self.index, name=self.name, goal=self.goal, tasks=self.tasks)
        return info
    def check_input_info(input_sprint, input_name, input_goal):
        check_name = len(input_name) < 80
        check_goal = len(input_goal) < 80
        check_all =  check_name and check_goal
        if check_all:
            return True
        else:
            return False