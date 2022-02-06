from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    users = sorted(users,key=lambda x: x["birthday"].replace(year=1970))

    curr = datetime.now()
    start = datetime(curr.year, curr.month, curr.day) - timedelta(curr.weekday()) + timedelta(5)
    end = start + timedelta(7)

    days = [[], [], [], [], []]

    for user in users:
        name = user["name"]
        birth = user["birthday"]

        if birth.replace(year=start.year) < start:
            continue
        if birth >= end:
            continue;

        if birth.weekday() == 0 or birth.weekday() > 4:
            days[0].append(name);
        else:
            days[birth.weekday()].append(name);
    
    for i, day in enumerate(days):
        if i == 0:
            print("Monday: ", end='')
        elif i == 1:
            print("Tuesday: ", end='')
        elif i == 2:
            print("Wednesday: ", end='')
        elif i == 3:
            print("Thursday: ", end='')
        elif i == 4:
            print("Friday: ", end='')

        print(*day, sep=', ')


users = [
    { "name": "Bill", "birthday": datetime.fromisoformat("1970-02-10 10:10:10") },
    { "name": "Ash", "birthday": datetime.fromisoformat("1970-02-10 10:10:10") },
    { "name": "Vanya", "birthday": datetime.fromisoformat("2022-02-05 10:10:10") },
    { "name": "Ak", "birthday": datetime.fromisoformat("2022-02-10 10:10:10") },
    { "name": "Zuk", "birthday": datetime.fromisoformat("2023-02-11 10:10:10") },
]

get_birthdays_per_week(users)