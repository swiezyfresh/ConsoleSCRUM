import sprint_class_control as sprint_cc
import iteration_class_control as iteration_cc
import sprint_plan_module as sprint_pm
import iteration_plan_module as iteration_pm

#RUN add_sprint function to start appending new sprints to the table
#ASSIGN returned LOCAL Sprint instance list to GLOBAL Sprint instance list
sprint_cc.Sprint.sprint_list = sprint_pm.add_sprints()
project_sprint_list = sprint_cc.Sprint.sprint_list
print(project_sprint_list)

for sprint in project_sprint_list:
    for index in range(sprint.iterations_count):
        sprint_cc.Sprint.add_iteration(sprint,index)