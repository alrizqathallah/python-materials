my_str_1 = 'Hello'
my_str_2 = "World"

my_str_3 = '''Multiline
string'''
my_str_4 = """Another
Multiline
String"""

msg = "It's a sunny day"
quote = 'She said, "Hello World!"'

msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""

my_str = 'Hello World'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False

my_str = 'Hello world'
print(len(my_str))  # 11

my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w

my_str = 'Hello world'
print(my_str[-1])  # d
print(my_str[-2]) # l

# String Concatenation
my_str_1 = 'Hello'
my_str_2 = "World"

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str)

# Casting operator
name = 'John Doe'
age = 26

name_and_age = name + str(age)
print(name_and_age) # John Doe26

# Augmeneted Operator
name = 'John Doe'
age = 26

name_and_age = name  # Start with the name
name_and_age += str(age)  # Append the age as string

print(name_and_age)  # John Doe26

# F-String
name = 'John Doe'
age = 26
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age) # My name is John Doe and I am 26 years old

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 10 is 15