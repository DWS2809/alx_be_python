# prompt for a single task
task = input("Enter your task: ")
# prompt for priority level
priority = input("priority (high, medium, low): ").lower()
# ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()
# process task based on priority
match priority:
    case "high":
        if time_bound == "yes":
            print(f"'{task}' is a high priority task that must be completed today!")
        else:
            print(f"'{task}' is a high priority task.")
    case "medium":
        if time_bound == "yes":
            print(f"'{task}' is a medium priority task. Try to complete it within the week.")
        else:
            print(f"'{task}' is a medium priority task.")
    case "low":
        if time_bound == "yes":
            print(f"'{task}' is a low priority task. You can get to it when you have spare time.")
        else:
            print(f"'{task}' is a low priority task.")
    case _:
        print("Invalid priority level entered.") 
