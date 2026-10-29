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
lst = ["Hello World!", 
       "London is the capital of Great Britain",
       "My name is Artur",
       "I'll be back"]
sent_messages = []
def send_messages():
    while lst:
        message = lst.pop(0)
        print(message)
        sent_messages.append(message)
send_messages()
print(lst)
print(sent_messages) 

#=========================================

#=========================================

#=========================================

#=========================================

#=========================================
# Worksheet 2:
#=========================================

#=========================================
# Task 1: Write a function greet that takes a name parameter and an optional greeting parameter with a default value of "Hello". 
# When called, the function should print the greeting followed by the name. How would you call this function with only the name argument?
def greet(name, greeting="Hello "):
    print(greeting, name)
greet("Artur")

#=========================================
# Task 2. Create a function calculate_rectangle_area that accepts two positional arguments, length and width, and returns the area of the rectangle.
# What happens if you call the function with only one argument?
def calculate_rectangle_area(length, width):
    area = length * width
    return area
print(calculate_rectangle_area(5, 3))
# if we call the function with only one argument, Python raises a TypeError because the secong argument is missing

#=========================================
# Task 3. Define a function create_profile that takes two parameters, name and age, with no default values. 
# Call the function using keyword arguments so that the order of arguments does not matter
def create_profile(name, age):
    print(name, age)
create_profile(age="19", name="Artur")

#=========================================
# Task 4. Write a function order_item that takes a required positional argument item and an optional keyword argument quantity with a default value of 1. 
# How would you call this function to specify both the item and quantity?
def order_item(item, quantity=1):
    print(item, quantity)
order_item("Laptop", quantity=3)

#=========================================
#Task 5. Create a function calculate_sum that can accept any number of numeric arguments 
# and returns their sum.
def calculate_sum(*args):
    return sum(args)
print(calculate_sum(1, 2, 3, 4, 5))

#=========================================
# Task 6. Write a function print_profile that accepts a variable number of keyword arguments. 
# It should print each value on a new line
def print_profile(**kward):
    for value in kward.values():
        print(value)
print_profile(age=19, name="Artur", city="London")

#=========================================
# Task 7. Write a function increment_counter that increments a global variable counter by 1 each time it is called. 
# Initialize counter outside the function with a value of 0. 
# How would you access and modify a global variable inside a function?
counter = 0
def increment_counter():
    global counter
    counter += 1
increment_counter()
increment_counter()
increment_counter()
print(counter)

#=========================================
# Task 8. Create a function book_ticket that takes two required parameters movie and date, and one optional parameter time with a default value of "7:00 PM". 
# How would you call this function to book a ticket for a specific movie and date, but with the default time?
def book_ticket(movie, date, time="7:00 PM"):
    print(f"Can I book a ticket for {movie} on {date},{time}")
book_ticket(movie="Interstellar", date="24.08.2027")

#=========================================
# Task 9. Create a function calculate_statistics that accepts a list of numbers and returns the minimum, maximum, and average of the list. 
# How would you call this function and print the returned values. 
def calculate_statistics(nums):
    return min(nums), max(nums), sum(nums)/len(nums)
print(calculate_statistics([1, 2, 3, 4, 5]))
#=========================================
# Task 10. Write a function log_event that accepts a string event_name as a required parameter, then
# any number of positional arguments and keyword arguments representing details about the event.
#It should print event_name, followed by each positional argument and each keyvalue pair in the keyword arguments.
def log_event(event_name, *args, **kwards):
    print(f"Event: {event_name}")
    print("Details:")
    for arg in args:
        print(f"- {arg}")
    for key, value in kwards.items():
        print(f"- {key}: {value}")
log_event(
    "Login Attempt",
    "User123",
    "Integrated Foundation Year",
    Location = "London",
    Email="user123@rhul.ac.uk")
#=========================================

#=========================================

#=========================================

#=========================================

#=========================================

#=========================================

#=========================================