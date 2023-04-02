#ITERATION CLASS CONTROL
class Iteration:
    def __init__(self, input_sprint, input_name, input_goal, input_index):
        self.sprint = input_sprint
        self.name = input_name
        self.goal = input_goal
        self.result = "Fail"
        self.index = input_index
        self.tasks = []
    
    def __repr__(self):
        info = "Iteration {index}\nName: {name}\nGoal: {goal}\nTasks: {tasks}"
        return info.format(index=self.index, name=self.name, goal=self.goal, tasks=self.tasks)
    
    def add_iteration(sprint, name, goal, index):
        iteration = Iteration(sprint, name, goal, index)
        sprint.iterations.append(iteration)

    def display_iterations(sprint):
        for iteration in sprint.iterations:
            print(iteration)