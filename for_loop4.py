word = input("Enter a word: ")
count = 0

for letter in word:
    if letter.lower() in "aeiou":
        count = count + 1

print("Number of vowels:", count)