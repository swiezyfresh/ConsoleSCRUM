#SPRINT CLASS CONTROL
class Sprint:
    #CREATE A COUNTER OF ALL NEW INSTANCES OF SPRINT OBJECT
    sprint_count = 0
    #CREATE A GLOBAL LIST OF ALL INSTANCES OF A SPRINT OBJECT
    sprint_list=[]

    #CONSTRUCT A NEW SPRINT INSTANCE
    def __init__(self, input_name, input_time_total, input_time_unit):
        #INCREMENT SPRINT INSTANCES COUNTER AND ASSIGN IT AS SPRINT ID
        Sprint.sprint_count +=1
        self.id=Sprint.sprint_count
        #ASSIGN USER-INPUT PARAMETERS
        self.name = input_name
        self.time_total = input_time_total
        self.time_unit = input_time_unit
        #ASSIGN CALCULATED PARAMETERS - TOTAL NUMBER OF ITERATIONS FOR SPECIFIC SPRINT
        self.iterations_count = int((self.time_total * 4) / self.time_unit)
        #ASSIGN LATE-USER-INPUT PARAMETER - SPRINT INSTANCE ITERATIONS LIST
        self.iterations=[]

    #PRINT INFORMATION ABOUT SPECIFIC SPRINT INSTANCE
    def __repr__(self):
        info = "Sprint {id}\nName: {name}\nTotal Time: {total_time}\nUnit Time: {unit_time}\nIterations Count: {iterations_count}\nIterations: {iterations}"
        return info.format(id=self.id,name=self.name,total_time=self.time_total,unit_time=self.time_unit,iterations_count=self.iterations_count,iterations=self.iterations)
    
    #CREATE SPRINT INSTANCE AND APPEND IT TO GENERAL SPRINT LIST
    def add_sprint(name, time_total, time_unit):
        new_sprint = Sprint(name, time_total, time_unit)
        Sprint.sprint_list.append(new_sprint)
    
    #CHECK FUNC DETERMINING IF SPRINT LIST IS NOT EMPTY
    def check_list():
        if len(Sprint.sprint_list) > 0:
            return True
        else:
            return False