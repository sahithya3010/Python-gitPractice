import datetime
name = input("Enter your name: ")
age = int(input(f"Hi {name}, enter your age: "))
requiredYears = 100-age
now = datetime.datetime.now()
print(f"Hi {name}, you will turn 100 by {now.year+requiredYears}. Happy Living!")