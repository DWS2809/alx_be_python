# prompt for a single task
task = input("Enter the task you want to be reminded of: ")
# prompt for priority level
priority = input("Enter the priority level (high, medium, low): ").lower()
# ask if the task is time-bound
time_bound = input("Is this task time-bound? (yes/no): ").lower()
# process task based on priority
match priority:
    case "high":
        print(f"'{task}' is a high priority task that requires immdiate attention today!")
    case "medium":
        print(f"'{task}' is a medium priority task. Try to complete it within the week.")
    case "low":
        print(f"'{task}' is a low priority task. You can get to it when you have spare time.")
    case _:
        print("Invalid priority level entered.") 
