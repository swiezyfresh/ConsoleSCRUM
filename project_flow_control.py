import Class_Control.sprint_class_control as sprint_cc
import Class_Control.iteration_class_control as iteration_cc
import Planning.sprint_plan_module as sprint_pm
import Execution.sprint_exe_module as sprint_exe

#RUN add_sprint function to start appending new sprints to the table
#ASSIGN returned LOCAL Sprint instance list to GLOBAL Sprint instance list
sprint_pm.add_sprint_loop()
sprint_exe.exe_sprint_loop()

