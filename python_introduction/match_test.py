# Matching days of the  week using match-case statement
day = input("Enter a day of the week: ").lower()
match day:
    case "monday":
        print("It's the start of the work week. Got alot of work to do!")
    case "tuesday":
        print("It's Tuesday! Let's keep the momentum going.")
    case "wednesday":
        print("It's Wednesday! It is the middle of the week, hang in there. We are almost at the end.")
    case "thursday":
        print("It's Thursday! The weekend is just around the corner. We have one more day to go.")
    case "friday":
        print("It's Friday! The weeekend starts after work today. Hang in until after work.")
    case "saturday" | "sunday":
        print("It's the weekend! Time to relax and focus on Alx projects more.")
    case _:
        print("That's not a valid day of the week. Please enter a correct day.")