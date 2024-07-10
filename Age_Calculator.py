import datetime


def age_calc():
    y = int(input("Enter your birth year (YYYY): "))
    m = int(input("Enter your birth month (MM): "))
    d = int(input("Enter your birth day (DD): "))

    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today-dob).days / 365.25)
    print(f"You are approximately {age} years old")

while True:
    age_calc()
    try_again = input("Do you want try again? (y/n):").lower()
    if try_again != "y":
        break
print("Thank You")

