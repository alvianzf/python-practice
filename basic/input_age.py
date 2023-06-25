# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

import datetime

name = input("what is your name ")
age = int(input("How old are you right now? "))

current_year = datetime.date.today().year

age_100 = (100-age+current_year)

print(f"you will reach 100 years old on the year {age_100}")