print("What is your name human?")
name = str(input())

print("How old are you (in years)?")
age = int(input())

print("How tall are you (in meters)?")
height = float(input())

print("How much do you weigh (in kilograms)?")
weight = float(input())

bmi = (weight/(height*height))

print("{} you are {} years old and your bmi is {:.2f}".format(name,age, bmi))