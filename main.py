from helper import validate, input_message

while True:

    no_of_days = input(input_message)
    if no_of_days == "exit":
        break
    else:
        no_of_days_dict = no_of_days.split(":")
        no_of_days_dict = {"days": no_of_days_dict[0], "units": no_of_days_dict[1]}
        result = validate(no_of_days_dict)
        print(result)
