#Character Occurence

word = input("Enter the word you want to check: ")
char = input("Enter the character you want to check in the word: ")

i = 0
count = 0

while i < len(word):
    if word[i] == char:
        count = count + 1

    i = i +1
print (f"The number of times {char} has occured = {count}")