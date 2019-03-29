def ages():
    size = raw_input("how many users are there: ")
    users = []
    for index in range(0, int(size)):
        age = raw_input(str(index) + ": what is the age: ")
        name = raw_input(str(index) + ": what is the name: ")
        users.append(User(name, int(age)))
    all_ages = ""
    for index in range(0, int(size)):
        all_ages += str(get_age_in_days(users[index].age)) + " "
    print all_ages
    all_ages = ""
    for index in range(0, int(size)):
        all_ages += str(get_age_in_hr(users[index].age)) + " "
    print all_ages
    all_ages = ""
    for index in range(0, int(size)):
        all_ages += str(get_age_in_min(users[index].age)) + " "
    print all_ages
    all_ages = ""
    for index in range(0, int(size)):
        what_am_I(users[index].age)

