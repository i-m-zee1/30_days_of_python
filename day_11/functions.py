'''📘 Day 11
Functions

So far we have seen many built-in Python functions. In this section, we will focus on custom functions. What is a function? Before we start making functions, let us learn what a function is and why we need them?
Defining a Function

A function is a reusable block of code or programming statements designed to perform a certain task. To define or declare a function, Python provides the def keyword. The following is the syntax for defining a function. The function block of code is executed only if the function is called or invoked.
Declaring and Calling a Function
'''
'''
When we make a function, we call it declaring a function. When we start using the it, we call it calling or invoking a function. Function can be declared with or without parameters.

# syntax
# Declaring a function
def function_name():
    codes
    codes
# Calling a function
function_name()

Function without Parameters

Function can be declared without parameters.
'''
#Example:

def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # calling a function

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()
'''
Function Returning a Value - Part 1

Function can also return values, if a function does not have a return statement, the value of the function is None. Let us rewrite the above functions using return. From now on, we get a value from a function when we call the function and print it.
'''
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())
'''
Function with Parameters

In a function we can pass different data types(number, string, boolean, list, tuple, dictionary or set) as a parameter

    Single Parameter: If our function takes a parameter we should call our function with an argument
  # syntax
  # Declaring a function
def function_name(parameter):
    codes
    codes
  # Calling function
  print(function_name(argument))
'''

# Example:

def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Asabeneh'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
'''
    Two Parameter: A function may or may not have a parameter or parameters. A function may also have two or more parameters. If our function takes parameters we should call it with arguments. Let us check a function with two parameters:

  # syntax
  # Declaring a function
  def function_name(para1, para2):
    codes
    codes
  # Calling function
  print(function_name(arg1, arg2))
'''
# Example:

def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Asabeneh','Yetayeh'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;

print('Age: ', calculate_age(2021, 1819))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))
'''
Passing Arguments with Key and Value

If we pass the arguments with key and value, the order of the arguments does not matter.

# syntax
# Declaring a function
def function_name(para1, para2):
    codes
    codes
# Calling function
print(function_name(para1 = 'John', para2 = 'Doe')) # the order of arguments does not matter here
'''
# Example:

def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print(print_fullname(firstname = 'Asabeneh', lastname = 'Yetayeh'))

def add_two_numbers (num1, num2):
    total = num1 + num2
    print(total)
print(add_two_numbers(num2 = 3, num1 = 2)) # Order does not matter
'''
Function Returning a Value - Part 2

If we do not return a value with a function, then our function is returning None by default. To return a value with a function we use the keyword return followed by the variable we are returning. We can return any kind of data types from a function.

    Returning a string: Example:
'''
def print_name(firstname):
    return firstname
print_name('Asabeneh') # Asabeneh

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print_full_name(firstname='Asabeneh', lastname='Yetayeh')

    # Returning a number:

# Example:

def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(2019, 1819))

    # Returning a boolean: Example:

def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # return stops further execution of the function, similar to break 
    return False
print(is_even(10)) # True
print(is_even(7)) # False

    # Returning a list: Example:

def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))
'''
Function with Default Parameters

Sometimes we pass default values to parameters, when we invoke the function. If we do not pass arguments when calling the function, their default values will be used.

# syntax
# Declaring a function
def function_name(param = value):
    codes
    codes
# Calling function
function_name()
function_name(arg)
'''
# Example:

def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Asabeneh'))

def generate_full_name (first_name = 'Asabeneh', last_name = 'Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('David','Smith'))

def calculate_age (birth_year,current_year = 2021):
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(1821))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - average gravity on Earth's surface
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # gravity on the surface of the Moon
'''
Arbitrary Number of Arguments

If we do not know the number of arguments we pass to our function, we can create a function which can take arbitrary number of arguments by adding * before the parameter name.

# syntax
# Declaring a function
def function_name(*args):
    codes
    codes
# Calling function
function_name(param1, param2, param3,..)
'''
# Example:

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10

# Default and Arbitrary Number of Parameters in Functions

def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','Asabeneh','Brook','David','Eyob'))

# Function as a Parameter of Another Function

#You can pass functions around as parameters
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27

'''
💻 Exercises: Day 11
Exercises: Level 1

    Declare a function add_two_numbers. It takes two parameters and it returns a sum.
    Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
    Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
    Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
    Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
    Write a function called calculate_slope which return the slope of a linear equation
    Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
    Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
    Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list1(["A", "B", "C"]))
# ["C", "B", "A"]

    Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
    Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))      [2, 3, 7, 9, 5]

    Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

    Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

    Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
    Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

Exercises: Level 2

    Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51.

    Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
    Call your function is_empty, it takes a parameter and it checks if it is empty or not
    Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

Exercises: Level 3

    Write a function called is_prime, which checks if a number is prime.
    Write a functions which checks if all items are unique in the list.
    Write a function which checks if all the items of the list are of the same data type.
    Write a function which check if provided variable is a valid python variable
    Go to the data folder and access the countries-data.py file.

    Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
    Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.

'''

def sum(a,b):
    return a+b
print("Sum: ",sum(3,4))
print("Sum: ",sum(7,9))

def circle_area(radius):
    return 3.14*(radius*radius)
print("Area of Circle: ",circle_area(5))
print("Area of Circle: ",circle_area(6))


def add_all_nums(*nums):
    sum=0
    for num in nums:
        if not isinstance(num,(int, float)):
            return f'{type(num)} cannot be added to numeric.'
        sum+=num
    return sum
print(add_all_nums(2,3,'a',5,6))
print(add_all_nums(2,3,5.5,5,6))
print(add_all_nums(2,3,True,5,6))
print(add_all_nums(2,3,[],5,6))

def convert_celsius_to_fahrenheit(temp):
    return round(((temp * (9/5)) + 32),2)
print(convert_celsius_to_fahrenheit(32))
print(convert_celsius_to_fahrenheit(67))
print(convert_celsius_to_fahrenheit(105))

def convert_temperature(temp, temp_type):
    return f'Fahrenheit: {round(((temp * (9/5)) + 32),2)}' if temp_type=='F' else f'Celsius: {round(((temp - 32) * 5/9),2)}'

print(convert_temperature(32,'C'))
print(convert_temperature(67, 'F'))
print(convert_temperature(105, 'C'))
print(convert_temperature(105, 'F'))

def check_season(month):
    if month in ['Dec','Jan','Feb']:
        return 'Winter'
    elif month in ['Mar', 'Apr', 'May']:
        return 'Spring'
    elif month in ['Jun', 'Jul','Aug']:
        return 'Summer'
    elif month in ['Sep', 'Oct', 'Nov']:
        return 'Autumn'
    else: return 'Month name is invalid'
print(check_season('Jan'))
print(check_season('Mar'))
print(check_season('Jun'))
print(check_season('xyz'))
print(check_season('Oct'))

def calculate_slope(x1,y1,x2,y2):
    if x2 == x1:
        return "Undefined (vertical line)"
    return (y2 - y1) / (x2 - x1)

print(calculate_slope(1, 2, 3, 6))   # 2.0
print(calculate_slope(2, 5, 2, 10))  # "Undefined (vertical line)"

import cmath  # handles both real and complex numbers

def solve_quadratic_eqn(a: float, b: float, c: float):
    if a == 0:
        return "Not a quadratic equation (a cannot be 0)."
    
    D = b**2 - 4*a*c  # discriminant
    root1 = (-b + cmath.sqrt(D)) / (2*a)
    root2 = (-b - cmath.sqrt(D)) / (2*a)
    
    return (root1, root2)

# Examples
print(solve_quadratic_eqn(1, -3, 2))   # (2, 1)  → two real roots
print(solve_quadratic_eqn(1, 2, 1))    # (-1, -1) → one real double root
print(solve_quadratic_eqn(1, 1, 1))    # complex roots

def print_list(lst:any):
    for l in lst:
        print(f'Element: {l}')
print_list([1, 2, 3, 4, 5])
print_list(["A", "B", "C"])
print_list(['Potato', 'Tomato', 'Mango', 'Milk','Meat'])
print_list([2, 3, 7, 9, 5])

def reverse_list(lst):
    new_lst=[]
    for i in range(len(lst)-1,-1,-1):
        new_lst.append(lst[i])
    return new_lst
print(reverse_list([1, 2, 3, 4, 5])) # [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"])) # ["C", "B", "A"]

def capitalize_list_items(lst):
    new_list=[]
    for l in range(len(lst)):
        new_list.append(lst[l].capitalize())
    return new_list
print(capitalize_list_items(['food_staff', 'mango','potato', 'tomato', 'mango', 'milk','meat']))

def add_item(lst,item):
    lst.append(item)
    return lst

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))      #[2, 3, 7, 9, 5]

def remove_item(lst, item):
    lst.remove(item)
    return lst
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

def sum_of_numbers(num:int):
    sum=0
    for i in range(1,num+1):
        sum+=i
    return sum
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

def sum_of_odds(num:int):
    sum=0
    for i in range(1,num+1):
        if i%2==1: sum+=i
    return sum
print(sum_of_odds(5))  # 15
print(sum_of_odds(10)) # 55
print(sum_of_odds(100)) # 5050

def sum_of_even(num:int):
    sum=0
    for i in range(1,num+1):
        if i%2==0: sum+=i
    return sum
print(sum_of_even(5))  # 15
print(sum_of_even(10)) # 55
print(sum_of_even(100)) # 5050

def evens_and_odds(num:int):
    e_sum=0
    o_sum=0
    for i in range(1,num+1):
        e_sum += i * (i % 2 == 0)
        o_sum += i * (i % 2 != 0)
    return f'The number of odds are {o_sum}. The number of evens are {e_sum}.'
print(evens_and_odds(5))  # 15
print(evens_and_odds(10)) # 55
print(evens_and_odds(100)) # 5050

def factorial(num:int):
    if num<=0: return 0
    elif num==1:return 1
    return num*factorial(num-1)
print(factorial(5))  # 15
print(factorial(4)) # 55
print(factorial(10)) # 5050

def is_empty(param):
    return 'Not Empty' if len(param) else 'Empty'

print(is_empty(''))
print(is_empty([]))
print(is_empty('1231'))
print(is_empty([1,2,3]))

# def calculate_mean():
#     pass
# def calculate_median(): pass
# def calculate_mode(): pass
# def calculate_range(): pass
# def calculate_variance(): pass
# def calculate_std(): pass

from collections import Counter
import math
import builtins

def calculate_mean(data: list) -> float:
    return (builtins.sum(data) / len(data))

def calculate_median(data: list) -> float:
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:  # even length
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:  # odd length
        return sorted_data[mid]

def calculate_mode(data: list):
    counts = Counter(data)
    max_count = max(counts.values())
    modes = [k for k, v in counts.items() if v == max_count]
    if len(modes) == 1:
        return modes[0]
    return modes  # multiple modes possible

def calculate_range(data: list) -> float:
    return max(data) - min(data)

def calculate_variance(data: list) -> float:
    mean = calculate_mean(data)
    return builtins.sum((x - mean) ** 2 for x in data) / len(data)

def calculate_std(data: list) -> float:
    return math.sqrt(calculate_variance(data))

nums = [2, 4, 4, 4, 5, 5, 7, 9]

print("Mean:", calculate_mean(nums))         # 5.0
print("Median:", calculate_median(nums))     # 4.5
print("Mode:", calculate_mode(nums))         # 4
print("Range:", calculate_range(nums))       # 7
print("Variance:", calculate_variance(nums)) # 4.0
print("Std Dev:", calculate_std(nums))       # 2.0

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # only check up to sqrt(n)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

print(is_prime(5))
print(is_prime(10))
print(is_prime(9))
print(is_prime(13))

def is_unique_items(lst:list) -> bool:
    return True if len(lst)==(len(set(lst))) else False
print(is_unique_items([1,2,3,4]))
print(is_unique_items([1,2,3,4,6,9,1]))
print(is_unique_items([1,2,3,2,4]))

def check_type(lst:list)->str:
    first_item_type = type(lst[0])
    for item in lst:
         if not isinstance(item,first_item_type):
            return 'Not of same type'
    return 'Same type'
print(check_type([1,2,3,4,'a']))
print(check_type([1,2,3,4,6,9,1,True]))
print(check_type([1,2,3,2,4]))

import keyword

def is_valid_variable(var: str) -> bool:
    return var.isidentifier() and not keyword.iskeyword(var)

print(is_valid_variable("my_var"))   # True
print(is_valid_variable("2var"))     # False (starts with digit)
print(is_valid_variable("for"))      # False (keyword)
print(is_valid_variable("_hidden"))  # True

def read_data()->any:
    with open("../data/countries-data.py") as f:   # 👈 go up one folder
    # exec(f.read(), data)
        content = f.read()

    return eval(content)   # convert text → Python list
# print(read_data())
from collections import Counter

def most_spoken_langs()->list:
    language_counter = Counter()

    for country in read_data():
        for lang in country['languages']:
            language_counter[lang] += 1

    most_spoken = language_counter.most_common(10)

    print("10 Most Spoken Languages:")
    for lang, count in most_spoken:
        print(lang, ":", count)

most_spoken_langs()

def most_populated_counts()->list:
    # Sort countries by population (descending)
    sorted_countries = sorted(read_data(), key=lambda x: x['population'], reverse=True)

    print("10 Most Populated Countries:")
    for country in sorted_countries[:10]:
        print(country['name'], ":", country['population'])

most_populated_counts()