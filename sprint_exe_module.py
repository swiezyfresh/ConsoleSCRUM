import sprint_class_control as sprint_cc
import iteration_plan_module as iteration_pm
sprint_list = sprint_cc.Sprint.sprint_list
def exe_sprint_loop():
    for sprint in sprint_list:
        print("\nINFO: Executing Sprint: {name}".format(name=sprint.name))
        print("==================================")
        iteration_pm.add_iteration_loop(sprint)