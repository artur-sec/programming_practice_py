#=========================================
#Worksheet 1:
#=========================================

#=========================================
#Task 1. Write a function reverse_string that takes a string s and returns it reversed.
def reverse_string(s): 
    return s[::-1] 
s = input("Enter a string: ") 
print (reverse_string(s)) 

#=========================================
#Task 2. Write a function remove_duplicates(lst) that removes duplicates from the list lst. 
def remove_duplicates(lst): 
    return list(set(lst)) 
lst = input("Enter a list of numbers: ").split(",") 
print(remove_duplicates(lst)) 

#=========================================
#Task 3. Write a function longest_word_length(s) that returns the longest word and its length in the string s. 
def longest_word_length(s): 
    words = s.split() 
    longest = max(words, key=len) 
    return longest, len(longest) 
s = input("Enter a string: ") 
print(longest_word_length(s)) 

#=========================================
#Task 4. Write a function count_vowels(s) that counts the number of vowels in the string s.  
def count_vowels(s): 
    count = 0 
    for i in s: 
        if i in "aouei": 
            count += 1 
    return count 
s = input("Enter a string: ").lower()
print(count_vowels(s)) 

#=========================================
#Task 5. Write a function digit(s) that checks if the string s is composed of digits only. 
def digit(s): 
    return s.isdigit() 
s = input("Enter a string: ") 
print(digit(s)) 

#=========================================
#Task 6. Write a function second_largest(lst) that returns the second largest number in the list lst. 


#=========================================
#Task 7. Write a function count_occurrences(lst, x) that counts the number of occurrences of a number x in the numbers list lst. 


#=========================================
#Task 8. Write a function count_words(s) that counts the number of words in the string s


#=========================================
#Task 9. Write a function is_substring(s1, s2) that checks if s1 is a substring of s2.


#=========================================
#Worksheet 2:
#=========================================

#=========================================

#=========================================

#=========================================

#=========================================

#=========================================

#=========================================

#=========================================