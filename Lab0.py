num = float(input("Please enter a number:"))
print(num * 2)

name = input("Please enter your name:")
print(name.upper())

import random
x = random.randint(10,20)
while True:
    guess = int(input("Please guess a number between 10 and 20:"))
    if guess == x:
        print("Congratulations, you guessed correctly!")
        break
    else:
        print("Wrong, please try again.")
        break

age = int(input("Please enter your age:"))
if age <=19:
    print("You qualify for student discounts.")
elif 20 <= age <= 54:
    print("You don't qualify any age - based discounts.")
else: 
    print("You can receive senior discounts.")

def factorial_while(num):
    result = 1
    while num > 0:
        result = result * num
        num = num - 1  
    return result
number = int(input("Please enter a number:"))
print(factorial_while(number))

def factorial_for(num):
    result = 1
    for i in range(1,num + 1):
        result = result * i
    return result

number = int(input("Please enter a number:"))
print(factorial_for(number))

studentNames = ["Lisa","Liam","Leo","Linda"]
for name in studentNames:
    print(name + "Evans")

new_name = input("Please add a name:")
studentNames.append(new_name)

for name in studentNames:
    print(name + "Evans")
