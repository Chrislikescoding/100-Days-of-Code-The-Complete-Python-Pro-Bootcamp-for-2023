#Odd or Even

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if  number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# BMI 2
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = round(weight / (height ** 2), 0)

if bmi < 18.5:
    print(f"Your BMI is {int(bmi)}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {int(bmi)}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {int(bmi)}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {int(bmi)}, you are obese.")
else:
    print(f"Your BMI is {int(bmi)}, you are clinically obese.")


# Leap Year
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
leapYear = False
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leapYear = True
    else:
        leapYear = True

if leapYear == True:
    print("Leap year.")
else:
    print("Not leap year.")

# Pizza Order practiice

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0

if size =='S':
    bill+=15
elif size == 'M':
    bill+=20
else:
    bill+=25

if add_pepperoni == 'Y':
    if size == 'S':
        bill+=2
    else:
        bill+=3

if extra_cheese == 'Y' :
     bill+=1

print(f"Your final bill is: ${bill}.")

#Love Calculator# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
string = (name1).lower() + name2.lower()
total1 = 0
total2 = 0
for letter in ['t','r','u','e']:
    total1 += string.count(letter)
for letter in ['l','o','v','e']:
    total2 += string.count(letter)

total = total1 *10 + total2

if total < 10 or total >90:
    print(f"Your score is **{total}**, you go together like coke and mentos.")
elif total > 40 and total < 50:
    print(f"Your score is **{total}**, you are alright together.")
else:
    print(f"Your score is **{total}**")

