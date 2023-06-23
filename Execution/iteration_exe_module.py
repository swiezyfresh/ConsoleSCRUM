import Planning.task_plan_module as task_pm
import Execution.task_exe_module as task_exe

def exe_iteration_loop(sprint):
    for iteration in sprint.iterations:
        print("\n==================================")
        print("INFO: Executing Iteration {}: {}".format(str(iteration.index+1), iteration.name))
        print("INFO: Planning Iteration {} Tasks".format(str(iteration.index+1)))
        print("==================================\n")

        task_pm.add_task_loop(iteration)
        task_exe.exe_task_loop(iteration)

        print("INFO: The goal for this iteration was \"{}\"".format(iteration.goal))
        result = exe_iteration_result()
        iteration.result = result
        print("INFO: This iteration was marked as {}".format(iteration.result))



def exe_iteration_result():
    result = input("Was the iteration sucessful? (Y/N): ")
    if result.upper() == "Y":
        return "Success"
    elif result.upper() == "N":
        return "Fail"
    else:
        print("WARNING: Please enter your answer correctly (Y/N)!")
        exe_iteration_loop()
    