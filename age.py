import datetime

birth_year = int(input("What is your birth year? "))
current_date = datetime.datetime.now()
day = current_date.day
year = current_date.year

age = year - (birth_year + 1)
print(f"You are {age} years old.")
print(" ")


def leap_year(lyear):
    if lyear % 400 == 0:
        return True
    elif lyear % 4 == 0 and not lyear % 100 == 0:
        return True
    return False


total_days = 0

for i in range(birth_year, year + 1):
    if leap_year(i):
        print(" ")
        print(f"{i} is leap year")
        print(" ")
    else:
        print(f"{i} is normal year")
