#SPRINT CLASS CONTROL

class Sprint:
    #DECLARE Object instances COUNTER
    object_count = 0

    #CONSTRUCTOR
    def __init__(self, input_name, input_time_total, input_time_unit):
        #UPDATE object_count when creating a new object
        Sprint.object_count +=1
        #ASSIGN basic instance attributes input - name, total time, unit time
        self.name = input_name
        self.time_total = input_time_total
        self.time_unit = input_time_unit

        #ASSIGN calculated instance attributes - total units count, iterations table
        self.identificator=Sprint.object_count
        #CREATE Iteration instances table for current sprint
        self.iterations_count = int((self.time_total * 4) / self.time_unit)
        self.iterations=[]
        for unit in range(self.iterations_count):
            self.iterations.append([])

    #REPRESENTATOR
    def __repr__(self):
        info = "Sprint {id}\nName: {name}\nTotal Time: {total_time}\nUnit Time: {unit_time}\nIterations Count: {iterations_count}\nIterations: {iterations}".format(id=self.identificator,name=self.name,total_time=self.time_total,unit_time=self.time_unit,iterations_count=self.iterations_count,iterations=self.iterations)
        return info
    
    #METHODS
    #CHECK if new Sprint instance inputs match general criteria
    def check_input_info(input_name, input_time_total, input_time_unit):
        #Sprint name must be less than 80 characters
        check_name = len(input_name) <= 80
        #Sprint duration must be less than 6 months
        check_time_total = input_time_total <= 6
        #Iteration duration must be 1, 2 or 4 weeks
        check_time_unit = input_time_unit in range(1,5) and input_time_unit != 3
        check_all = check_name and check_time_total and check_time_unit
        if check_all:
            return True
        else:
            return False