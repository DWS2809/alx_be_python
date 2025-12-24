# prompt for a single task
Task = input("Enter your task: ")
# prompt for priority level
Priority = input("priority (high, medium, low): ").lower()
# ask if the task is time-bound
Time_Bound = input("Is it time-bound? (yes/no): ").lower()
# process task based on priority
match Priority:
    case "high":
        if Time_Bound == "yes":
            print(f"'{Task}' is a high priority task that must be completed today!")
        else:
            print(f"'{Task}' is a high priority task.")
    case "medium":
        if Time_Bound == "yes":
            print(f"'{Task}' is a medium priority task. Try to complete it within the week.")
        else:
            print(f"'{Task}' is a medium priority task.")
    case "low":
        if Time_Bound == "yes":
            print(f"'{Task}' is a low priority task. You can get to it when you have spare time.")
        else:
            print(f"'{Task}' is a low priority task.")
    case _:
        print("Invalid priority level entered.") 
