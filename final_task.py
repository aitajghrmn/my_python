"""number=int(input("Enter the number: "))
while number==0:
    print("The end of the game")
    number=int(input("Enter the number: "))"""

positive = 0
negative = 0

number = int(input("Enter the number (0 to stop): "))

while number != 0:
    
    if number > 0:
        positive = positive + 1
    else:
        negative = negative + 1

    number = int(input("Enter the number (0 to stop): "))

print("Positive numbers:", positive)
print("Negative numbers:", negative)
