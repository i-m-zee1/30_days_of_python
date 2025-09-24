#Day 2: 30 Days of python programming

print('hello world');
print(len('hello world'))
print(type('hllow world'))
print(int(3.5))
print(str(6.9234))
print(float(6))
# name = input("Enter name: ")
# print(name)

help('keywords');

print(min(20,30,40,60,12))
print(max(20,30,40,60,12))
print(min([20,30,40,60,12]))
print(max([20,30,40,60,12]))
print(sum([20,30,40,60,12]))

# Variables in Python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

#Multiple variables can also be declared in one line:


first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

# first_name = input('What is your name: ')
# age = input('How old are you? ')

print(first_name)
print(age)

# Different python data types
# Let's declare variables with various data types

first_name = 'Asabeneh'     # str
last_name = 'Yetayeh'       # str
country = 'Finland'         # str
city= 'Helsinki'            # str
age = 250                   # int, it is not my real age, don't worry about it

# Printing out types
print(type('Asabeneh'))          # str
print(type(first_name))          # str
print(type(10))                  # int
print(type(3.14))                # float
print(type(1 + 1j))              # complex
print(type(True))                # bool
print(type([1, 2, 3, 4]))        # list
print(type({'name':'Asabeneh'})) # dict
print(type((1,2)))               # tuple
print(type(zip([1,2],[3,4])))    # zip

# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
num_float = float(num_str)
print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int))      # 10

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']
'''
💻 Exercises - Day 2
Exercises: Level 1

    Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
    Write a python comment saying 'Day 2: 30 Days of python programming'
    Declare a first name variable and assign a value to it
    Declare a last name variable and assign a value to it
    Declare a full name variable and assign a value to it
    Declare a country variable and assign a value to it
    Declare a city variable and assign a value to it
    Declare an age variable and assign a value to it
    Declare a year variable and assign a value to it
    Declare a variable is_married and assign a value to it
    Declare a variable is_true and assign a value to it
    Declare a variable is_light_on and assign a value to it
    Declare multiple variable on one line

Exercises: Level 2

    Check the data type of all your variables using type() built-in function
    Using the len() built-in function, find the length of your first name
    Compare the length of your first name and your last name
    Declare 5 as num_one and 4 as num_two
    Add num_one and num_two and assign the value to a variable total
    Subtract num_two from num_one and assign the value to a variable diff
    Multiply num_two and num_one and assign the value to a variable product
    Divide num_one by num_two and assign the value to a variable division
    Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
    Calculate num_one to the power of num_two and assign the value to a variable exp
    Find floor division of num_one by num_two and assign the value to a variable floor_division
    The radius of a circle is 30 meters.
        Calculate the area of a circle and assign the value to a variable name of area_of_circle
        Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
        Take radius as user input and calculate the area.
    Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
    Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
'''
    # Day 2: 30 Days of python programming';
first_name = 'Zeeshan'
last_name = 'Ali'
full_name = 'Muhammad Zeeshan Ali'
country = 'Pakistan'
city = 'Islamabad'
age = 37
year = 2025
is_married = True
is_true = False
is_light_on = False

full_name, country, city, age, year = 'Muhammad Zeeshan Ali', 'Pakistan','Islamabad', 37,2025;

print(type(first_name))
print(type(last_name))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))

print(len(first_name))

print(len(first_name)==len(last_name))

num_one=5
num_two=4
total=num_one+num_two
total=sum([num_one,num_two])
diff = num_one-num_two
product = num_one*num_two
division=num_one/num_two
remainder = num_two%num_one
exp=num_one**num_two
floor_division=num_one//num_two

area_of_circle = 3.14 * (30 ** 2)
circum_of_circle = 2 * 3.14 * 30

get_radius = input("Enter radius to calclute Area: ")
area = 3.14 * (int(get_radius) ** 2)

first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
country = input("Enter Country: ")
city = input("Enter City: ")
age = input("Enter Age: ")
print(help('keywords'))