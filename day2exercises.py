# # 1. Hello, you!
name = input("What is your name? ")
print("Hello, " + name.upper())
namelength = len(name)

# 2. Hello, you!
print("Your name has " + str(namelength) + " letters! PRETTY COOL MAN")

# # 3. MADLIB
print("Fill in the blanks: ___(name)___'s favorite subject in school is ___subject___")
nameInput = input("What is the name? ")
subjectInput = input("What is the subject? ")
print(nameInput + "'s favorite subject in school is " + subjectInput)

# 4. Day of the Week
day = int(input('Day (0-6)?'))
if day == 0:
    print("Sunday")
elif day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")

# 5. Work or sleep in?
if day == 0 or 6:
    print("Sleep in")
else: 
    print("Work!")

# 6. Celsius or Fahrenheit?
tempInC = input("What is the temperature, in C? ")
tempInF = float(tempInC) * 1.8 + 32
print("Temp in fahrenheit is " + str(tempInF))

# 7. Tip calculator
bill = float(input("How much is the bill? $"))
serviceLevel = input("Level of service? (Good, Fair, Bad) ")
peopleNumber = input("Split how many ways? ")
if serviceLevel.upper() == "GOOD":
    tipPercentage = .20
elif serviceLevel.upper() == "FAIR":
    tipPercentage = .15
elif serviceLevel.upper() == "BAD":
    tipPercentage = .10

tip = bill * tipPercentage
totalAmount = tip + bill
print("You should tip " + "{:.2f}".format(tip))
print("Total amount: " + "{:.2f}".format(totalAmount)) #str(totalAmount))
print("Amount per person: " + str(totalAmount / float(peopleNumber)))

# 8. Tip Calculator 2


# 9. 1 to 10
number = 1
while number < 11:
    print(number)
    number += 1


# 10. How many coins?
userInput = "YES"
coinTally = 0
while userInput.upper() == "YES":
    userInput = input("Do you want a coin? Yes or no: ")
    if userInput.upper() == "YES":
        coinTally += 1
        print(str(coinTally))
    else:
        print("bye lol")



