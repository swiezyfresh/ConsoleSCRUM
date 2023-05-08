import Planning.task_plan_module as task_pm

def exe_iteration_loop(sprint):
    for iteration in sprint.iterations:
        print("\n==================================")
        print("INFO: Executing Iteration {}: {}".format(str(iteration.index+1), iteration.name))
        print("INFO: Planning Iteration {} Tasks".format(str(iteration.index+1)))
        print("==================================\n")
        task_pm.add_task_loop(iteration)