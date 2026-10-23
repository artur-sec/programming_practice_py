#=========================================
#Worksheet 1:
#=========================================

#=========================================
#Task 1. Write a program to check if a given string is empty or not.
s = input("Enter a string: ")  
if s == "":  
    print("The given string is empty")  
else:  
    print("The given string is not empty") 

#=========================================
#Task 2.  Write a program to print each character of a string on a new line using a for loop. 
s = input("Enter a string: ")  
for i in s: 
    print(i) 
  
#=========================================  
#Task 3. Write a program to count the number of vowels in a string.
s = input("Enter a string: ")  
count = 0 
for i in s: 
    if i in 'aeiouAEIOU': 
        count += 1 
print(count)

#========================================
#Task 4. Write a program to reverse a string without using slicing. 
s = input("Enter a string: ") 
result = "" 
for i in s: 
    result = i + result 
print(result) 

#========================================
#Task 5. Write a program to check if a given string is a palindrome. 
#(A palindrome is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards, such as radar, level, and madam.)  
print("Enter a word: ") 
w = input() 
if w == w[::-1]: 
    print("It is a palindrome") 
else: 
    print("It is not a palindrome") 
  
#========================================
#Task 6. Write a program to count the occurrences of a specific character in a string.
s = input("Enter a string: ").lower()
let = input("Enter a letter: ").lower()
while len(let) != 1:
    print("Try again!")
    let = input("Enter a letter: ")
count = 0 
for i in s: 
    if i == let: 
        count += 1 
print("The letter", let, "appears " + str(count) + " times in the string.") 

#========================================
#Task 7. Write a program to convert a string to uppercase. 
s = input("Enter a string: ") 
print(s.upper()) 

#========================================
#Task 8. Write a program to replace all spaces in a string with a hyphen. 
s = input("Enter a string: ").replace(" ", "-") 
print(s) 

#========================================
#Task 9. Write a program to concatenate two strings.
s_1 = input("Enter a string: ") 
s_2 = input("Enter the second string: ") 
result = s_1 + s_2 
print(result)

#========================================
#Task 10. Write a program to find the first occurrence of a character in a string. 
s = input("Enter a string: ").lower()
char = input("Enter characters: ").lower() 
for i in range(len(s)): 
    if s[i] == char: 
        print(i) 
        break 
else:
    print("The character ", characters, " has not been founded.")

#========================================
#Worksheet 2:

#========================================
#Task 1. Write a program to print the characters at even index positions in a string.
s = input("Enter a string: ") 
print(s[::2]) 

#========================================
#Task 2. Write a program to copy all vowels from a string into a new string.  
s = input("Enter a string: ") 
vow = "" 
for i in s: 
    if i in "aeiouAEIOU": 
        vow += i 
print("Vowels in the string:", vow) 

#========================================
#Task 3. Write a program that counts how many words there are in a given string. Assume words are separated by spaces.
s = input("Enter a string: ")  
w = s.split() 
print(len(w)) 

#========================================
#Task 4. Write a program that removes any character from a given string if it appears more than once.
s = input("Enter a string: ") 
res = "" 
for i in s: 
    if s.count(i) == 1: 
        res += i 
print(res)

#=======================================
#Task 5. Write a program that counts the number of vowels and consonants in a given string. 
#(The string may include spaces and punctuations.)
s = input("Enter a string: ").upper()  
count_vowels = 0 
count_consonants = 0  
for i in s: 
    if i in "AEIOU": 
        count_vowels += 1 
    else: 
        if i in "BCDFGHJKLMNPQRSTVWXYZ": 
            count_consonants += 1 
print("Number of vowels: ", str(count_vowels))
print("Number of consonants: ", str(count_consonants))

#=======================================
#Task 6. Write a program that takes a string and toggles the case of every alphabetic character 
#(i.e., lowercase becomes uppercase, and vice versa). 
s = input("Enter a string: ") 
print(s.swapcase()) 

#=======================================
#Task 7. Write a Python program that extracts and concatenates all uppercase letters from a given string in the order they appear.
s = input("Enter a string: ") 
res = "" 
for i in s: 
    if i.isupper(): 
        res += i 
print(res) 
