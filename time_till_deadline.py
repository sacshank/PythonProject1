from datetime import datetime

user_input = input("enter your goal with a deadline separated by colon \n")
input_list = user_input.split(":")

print(input_list)
print(type(input_list))
goal = input_list[0]
dead_line = input_list[1]
deadline_date = datetime.strptime(dead_line, "%d.%m.%Y")
todays_date = datetime.today()
remaining_days = deadline_date - todays_date
print(f"the remaining hours for the goal to {goal} is {remaining_days.days * 24}")
