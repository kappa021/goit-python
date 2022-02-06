from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    users = sorted(users,key=lambda x: x["birthday"].replace(year=1970))

    curr = datetime.now()
    start = datetime(curr.year, curr.month, curr.day) - timedelta(curr.weekday()) + timedelta(5)
    end = start + timedelta(7)

    print(end)

    for user in users:
        name = user["name"]
        birth = user["birthday"]

        if birth.replace(year=start.year) < start:
            continue
        if birth.replace(year=end.year) >= end:
            continue;

        if birth.weekday() == 0 or birth.weekday() > 4:
            print(f"Monday: {name}")
        elif birth.weekday() == 1:
            print(f"Tuesday: {name}")
        elif birth.weekday() == 2:
            print(f"Wednesday: {name}")
        elif birth.weekday() == 3:
            print(f"Thursday: {name}")
        elif birth.weekday() == 4:
            print(f"Friday: {name}")


users = [
    { "name": "Bill", "birthday": datetime.fromisoformat("1970-02-10 10:10:10") },
    { "name": "Vanya", "birthday": datetime.fromisoformat("2022-02-05 10:10:10") },
    { "name": "Ak", "birthday": datetime.fromisoformat("1980-02-15 10:10:10") },
    { "name": "Zuk", "birthday": datetime.fromisoformat("2023-02-11 10:10:10") },
]

get_birthdays_per_week(users)