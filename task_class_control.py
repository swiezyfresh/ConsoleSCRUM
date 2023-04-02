class Task:
    id_count = 0
    def __init__(self, name, number, assignment, complexity):
        Task.id_count += 1
        self.id = Task.id_count
        self.name = name
        self.number = number
        self.assignment = assignment
        self.complexity = complexity
        self.status = "To Do"
    
    def __repr__(self) -> str:
        info = "Id: {id}, Name: {nam}, Number: {num}, Assigned: {ass}, Complexity: {comp}, Status: {stat}"
        return info.format(id=self.id, nam=self.name, num=self.number, ass=self.assignment, comp=self.complexity, stat=self.status)