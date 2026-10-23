#Worksheet 1:

#=========================================
#Task 1.
#Extract all the digits from a given string and store them in a list. 
#(Suppose a variable contains the following string: "hello123world456" Then the output should be: [1, 2, 3, 4, 5, 6])
s = "hello123world456" 
dig = [] 
for i in s: 
    if i.isdigit(): 
        dig.append(int(i)) 
print(dig) 

#=========================================
#Task 2. Find the second largest number in a list. 
num = input("Enter numbers separated by commas: ").split(",")
num = list(set(map(int, num)))
num.sort(reverse=True)
print(num[1])

#=========================================
#Task 3. Find the intersection of following three lists.
#P.S. use set function and & operator [1, 3, 2, 4, 2, 5] [0, 3, 4, 5, 6, 4, 9] [5, 6, 3, 3, 9, 3, 7, 1] 
#=========================================

#=========================================

#=========================================

#=========================================

#=========================================

#=========================================

#=========================================

#=========================================

#=========================================

#=========================================

#=========================================

#=========================================
