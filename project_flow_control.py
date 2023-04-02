import sprint_class_control as sprint_cc
import iteration_class_control as iteration_cc
import sprint_plan_module as sprint_pm
import iteration_plan_module as iteration_pm
import sprint_exe_module as sprint_exe

#RUN add_sprint function to start appending new sprints to the table
#ASSIGN returned LOCAL Sprint instance list to GLOBAL Sprint instance list
sprint_pm.add_sprint_loop()
sprint_exe.exe_sprint_loop()

iteration_cc.Iteration.display_iterations(sprint_cc.Sprint.sprint_list[0])