calculate_to_minutes = 24 * 60
calculate_to_seconds = 24 * 60 * 60
calculate_to_hours = 24

input_message = "hello user please enter no of days and unit it to be converted in \n"
# no_of_days = ""


def calculate( no_of_days_dict,no_of_days_value, unit_value):
    if no_of_days_dict["units"] == "hours":
        return f"hours in {no_of_days_value} days are {no_of_days_value * calculate_to_hours}"
    elif no_of_days_dict["units"] == "seconds":
        return f"seconds in {no_of_days_value} are {no_of_days_value * calculate_to_seconds}"
    elif no_of_days_dict["units"] == "minutes":
        return f"minutes in {no_of_days_value} are {no_of_days_value * calculate_to_minutes}"
    else:
        return "please enter proper units"


def validate(no_of_days_dict):
    # no_of_days = input("enter number of days \n")
    if no_of_days_dict["days"].isdigit():
        no_of_days_value = int(no_of_days_dict["days"])
        if no_of_days_value > 0:
            # print(type(no_of_days_value))
            return calculate(no_of_days_dict,no_of_days_value, no_of_days_dict["units"])

        elif no_of_days_value == 0:
            print("please enter value greater than zero")
    else:
        print("please enter a valid number")
