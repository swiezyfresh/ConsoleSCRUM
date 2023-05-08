#ITERATION CLASS CONTROL
class Iteration:
    #CONSTRUCT A NEW ITERATION INSTANCE
    def __init__(self, input_sprint, input_name, input_goal, input_index):
        self.sprint = input_sprint
        self.name = input_name
        self.goal = input_goal
        self.result = "Fail"
        self.index = input_index
        self.tasks = []
    #PRINT INFORMATION ABOUT SPECIFIC ITERATION INSTANCE
    def __repr__(self):
        info = "Iteration {index}\nName: {name}\nGoal: {goal}\n"
        return info.format(index=self.index, name=self.name, goal=self.goal)
    
    #CREATE ITERATION INSTANCE AND APPEND IT TO SPECIFIC SPRINT ITERATIONS LIST
    def add_iteration(sprint, name, goal, index):
        iteration = Iteration(sprint, name, goal, index)
        sprint.iterations.append(iteration)

    #DISPLAY ALL ITERATION INSTANCES ASSIGNED TO SPRINT INSTANCE
    def display_iterations(sprint):
        print("\nITERATIONS SUMMARY FOR SPRINT {id}: {name}".format(id=sprint.id, name=sprint.name))
        for iteration in sprint.iterations:
            print(iteration)

    def check_tasks_list(self):
        if len(self.tasks) > 0:
            return True
        else:
            return False