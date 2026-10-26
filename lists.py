#=========================================
# Worksheet 1:
#=========================================

#=========================================
# Task 1.
#Extract all the digits from a given string and store them in a list. 
#(Suppose a variable contains the following string: "hello123world456" Then the output should be: [1, 2, 3, 4, 5, 6])
s = "hello123world456" 
dig = [] 
for i in s: 
    if i.isdigit(): 
        dig.append(int(i)) 
print(dig) 

#=========================================
# Task 2. Find the second largest number in a list. 
num = input("Enter numbers separated by commas: ").split(",")
num = list(set(map(int, num)))
num.sort(reverse=True)
print(num[1])

#=========================================
# Task 3. Find the intersection of following three lists.
# P.S. use set function and & operator [1, 3, 2, 4, 2, 5] [0, 3, 4, 5, 6, 4, 9] [5, 6, 3, 3, 9, 3, 7, 1] 
lst_1 = [1, 3, 2, 4, 2, 5] 
lst_2 = [0, 3, 4, 5, 6, 4, 9] 
lst_3 = [5, 6, 3, 3, 9, 3, 7, 1]  
res = set(lst_1) & set(lst_2) & set(lst_3) 
print(res) 

#=========================================
# Task 4. Write a program which accepts a sequence of comma-separated numbers from user and generate a list which contains every number.
# (Suppose the following input is supplied by the user: 34,67,55,33,12,98 Then the output should be: [‘34’, ‘67’, ‘55’, ‘33’, ‘12’, ‘98’])
list = input("Enter your list of numbers: ")  
list = list.replace(" ", "") 
list = list.split(",")  
print(list) 

#=========================================
# Task 5. Write a program that accepts a comma separated sequence of words as input and prints the words in a comma separated sequence sorting them alphabetically. 
# (Suppose the following sequence is supplied by the user: without,hello,bag,world Then, the output should be: bag,hello,without,world)
lst = input("Enter a list of words separated by comma: ") 
lst = lst.split(",") 
lst.sort() 
print(", ".join(lst)) 

#=========================================
# Task 6. Write a program that accepts sequence of lines as input and prints the lines after making all characters in the lines capitalized. 
# (Suppose the following input is provided by the user: Hello world practice makes perfect Then, the output should be: HELLO WORLD PRACTICE MAKES PERFECT )
text = input("Enter a line: ") 
print(text.upper()) 

#=========================================
# Task 7. Write a program that accepts a sentence and calculates the number of letters and digits. 
# (Suppose the following input is provided by the user: Hello world! 123 Then, the output should be: Letters = 10 Digits = 3)
s = input("Enter a string: ") 
digits = 0 
letters = 0 
for i in s: 
    if i.isdigit(): 
        digits += 1 
    elif i.isalpha(): 
        letters += 1 
print("Letters = " + str(letters) +
      ". Digits = " + str(digits) + ".") 

#=========================================
# Worksheet 2. 
#=========================================

#=========================================
# Task 1. Write a program that accepts a sequence of comma separated numbers. Store the numbers in a list and squares each odd number.
num = input("Enter numbers separated by commas: ").split(',') 
for i in range(len(num)): 
    num[i] = int(num[i]) 
    if num[i] % 2 != 0: 
        num[i] = num[i] ** 2 
print(num) 

#=========================================
# Task 2. Write a program to compute the frequence of words from the input. 
#( Suppose the following input is supplied by the user: "New to python or choosing between Python 2 and Python 3? Read Python 2 or Python 3." Then the output should be: "2: 2 3.: 1 3?: 1 New: 1 Python: 5 Read: 1 and: 1 between: 1 choosing: 1 or: 2 to:1")
txt = input("Enter some text: ").lower().split()
frequency = {} 
for word in txt: 
    if word in frequency: 
        frequency[word] += 1 
    else: 
        frequency[word] = 1 
for word in frequency: 
    print(word.capitalize(), ":", frequency[word]) 

#=========================================
# Task 3. Write a Python program that reverses a list starting from a given index. 
#(Suppose the following input is supplied by the user: "Write a Python program that reverses a list", starting index for reversal: 3. Then the output should be: Reversed list: ['write', 'a', 'python', 'list', 'a', 'reverses', 'that', 'program'])
txt = input("Enter some text: ").lower().split() 
index = int(input("Enter index for reversal: ")) 
result = txt[:index] + txt[index:][::-1] 
print("Reversed list: ", result) 

#=========================================
# Task 4.Write a python code that takes the above list and generates a string with all the items separated by a comma and a space, with and inserted before the last item. The program should work with any list values.
# (Suppose there is a list: spam = [‘apples’, ‘bananas’, ‘tofu’, ‘cats’]. For example, the spam list should create the string: ‘apples, bananas, tofu, and cats’.)
spam = input("Enter list of words: ").split(", ")
result = ', '.join(spam[::-1]) + ', and ' + spam[-1] 
print(result)

#=========================================
# Task 5. Given the following list of lists, where each value in the inner lists is a one-character string:
# grid = [['.', '.', '.', '.', '.', '.'],
#         ['.', '0', '0', '.', '.', '.'],
#         ['0', '0', '0', '0', '.', '.'],
#         ['0', '0', '0', '0', '0', '.'],
#         ['.', '0', '0', '0', '0', '0'],
#         ['0', '0', '0', '0', '0', '.'],
#         ['0', '0', '0', '0', '.', '.'],
#         ['.', '0', '0', '.', '.', '.'],
#         [ '.', '.', '.', '.', '.', '.']]
# Write a program that uses the above list to print the following pattern:
# ..00.00..
# .0000000.
# .0000000.
# ..00000..
# ...000...
# ....0....
grid = [['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.', '.', '.', '.'],
        ['0', '0', '0', '0', '0', '.', '.', '.', '.'],
        ['.', '0', '0', '0', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '0', '.', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.']]
for row in range(6):
    for col in range(9):
        print(grid[col][row], end="")
    print()
