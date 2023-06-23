import Class_Control.sprint_class_control as sprint_cc
import Planning.iteration_plan_module as iteration_pm
import Execution.iteration_exe_module as iteration_exe

sprint_list = sprint_cc.Sprint.sprint_list

def exe_sprint_loop():
    for sprint in sprint_list:
        print("\n==================================")
        print("INFO: Executing Sprint: {name}".format(name=sprint.name))
        iteration_pm.add_iteration_loop(sprint)
        iteration_exe.exe_iteration_loop(sprint)
    exe_sprint_summary()

def exe_sprint_summary():
    print("\n==================================")
    print("INFO: Project Completed!")
    print("==================================")
    print("INFO: SUMMARY\n")
    for sprint in sprint_list:
        print("Sprint {}: {}".format(sprint.id,sprint.name))
        for iteration in sprint.iterations:
            print("Iteration {}: {} - {}".format(iteration.index, iteration.name, iteration.result))