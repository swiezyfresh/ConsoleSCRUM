#SPRINT CLASS CONTROL

class Sprint:
    object_count = 0
    sprint_list=[]
    def __init__(self, input_name, input_time_total, input_time_unit):
        Sprint.object_count +=1
        self.name = input_name
        self.time_total = input_time_total
        self.time_unit = input_time_unit
        self.identificator=Sprint.object_count
        self.iterations_count = int((self.time_total * 4) / self.time_unit)
        self.iterations=[]

    def __repr__(self):
        info = "Sprint {id}\nName: {name}\nTotal Time: {total_time}\nUnit Time: {unit_time}\nIterations Count: {iterations_count}\nIterations: {iterations}"
        return info.format(id=self.identificator,name=self.name,total_time=self.time_total,unit_time=self.time_unit,iterations_count=self.iterations_count,iterations=self.iterations)
       
    def add_sprint(name, time_total, time_unit):
        new_sprint = Sprint(name, time_total, time_unit)
        Sprint.sprint_list.append(new_sprint)
        
    def check_list():
        if len(Sprint.sprint_list) > 0:
            return True
        else:
            return False