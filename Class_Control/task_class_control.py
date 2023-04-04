#TASK CLASS CONTROL
class Task:
    #CREATE A COUNTER OF ALL NEW INSTANCES OF TASK OBJECT
    task_count = 0

    #CONSTRUCT A NEW TASK INSTANCE
    def __init__(self, name, number, assignment, complexity):
        #INCREMENT TASK INSTANCES COUNTER AND ASSIGN IT AS TASK ID
        Task.task_count += 1
        self.id = Task.task_count
        #ASSIGN USER-INPUT PARAMETERS
        self.name = name
        self.number = number
        self.assignment = assignment
        self.complexity = complexity
        #ASSIGN LATE-USER-INPUT PARAMETER - DEFAULT STATUS
        self.status = "To Do"
    
    #PRINT INFORMATION ABOUT SPECIFIC TASK INSTANCE
    def __repr__(self) -> str:
        info = "Id: {id}, Name: {nam}, Number: {num}, Assigned: {ass}, Complexity: {comp}, Status: {stat}"
        return info.format(id=self.id, nam=self.name, num=self.number, ass=self.assignment, comp=self.complexity, stat=self.status)