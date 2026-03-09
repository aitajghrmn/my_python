largest = 0

for i in range(5):
    num = int(input("Enter a number: "))

    if num > largest:
        largest = num

print("Largest number:", largest)