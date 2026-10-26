#=========================================
# Worksheet 1:
#=========================================

#=========================================
# Task 1. Write a function called print_poster() that accepts a size and the text of a message that should be printed on the poster. 
# The function should print a sentence summarizing the size of the poster and the message printed on it.
# Call the function once using positional arguments to print a poster. Call the function a second time using keyword arguments.
def print_poster(size, message):
    print(f"The poster size is {size}. The message is: '{message}'")
        
    #Using Positional argument:
print_poster("small", "My name is Artur!")

    #Using Keyword argument:
print_poster(size="large", message="Artur is my name")

#=========================================
# Task 2. Modify the print_poster() function from question 1 so that posters are large by default with a message that reads I love Python.
# Print a large poster and a medium poster with the default message, and a poster of any size with a different message
def print_poster(size="large", message="I love Python"):
    print(f"The poster size is {size}. The message is {message}")

    #Large Poster with default message:
print_poster()

    #Medium Poster with default message:
print_poster(size="medium")

    #Poster with any other size with a different message:
print_poster(size="small", message="Hello World!")

#=========================================
# Task 3. Write a function called describe_city() that accepts the name of a city and its country
# The function should print a simple sentence, such as London is in England. Give the parameter for the country a default value. 
# Call your function for three different cities, at least one of which is not in the default country
def describe_city(city, country="Ukraine"):
    print(f"{city} is in {country}")
    #First City which is in the default country:
describe_city(city="Kyiv")

    #Second city which is not in the default country:
describe_city(city="Manchester", country="the United Kingdom")
    
    #Third city which is not in the default country:
describe_city(city="Rosario", country="Argentina")

#=========================================
# Task 4. Write a function called city_country() that takes in the name of a city and its country.
# The function should return a string formatted like this: London, UK
def city_country(city, country):
    return f"{city}, {country}"
print(city_country(city="Warsaw", country="Poland"))

#=========================================
# Task 5. Make a list containing a series of short messages. 
# Pass the list to a function called display_messages(), which prints each message.
lst = ["Hello World!", 
       "London is the capital of Great Britain",
       "My name is Artur",
       "I'll be back"]
def display_messages(lst):
    for message in lst:
        print(message)
display_messages(lst)

#=========================================
# Task 6. Start with a copy of your program from question 5.
# Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. 
# After calling the function, print both of your lists to make sure the messages were moved correctly.


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

#=========================================