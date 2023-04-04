import Class_Control.iteration_class_control as iteration_cc
import Class_Control.sprint_class_control as sprint_cc

def exe_iteration_loop(sprint):
    for iteration in sprint.iterations:
        print("\n==================================")
        print("INFO: Executing Iteration {}: {}".format(str(iteration.index+1), iteration.name))
        print("INFO: Planning Iteration {} Tasks".format(str(iteration.index+1)))
        print("==================================\n")