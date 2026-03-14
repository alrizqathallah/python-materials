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

my_str = 'Hello world'
print(my_str[8:])  # rld
print(my_str[:8])

my_str = 'Hello world'
print(my_str[0:11:2])  # Hlowrd

my_str = 'Hello world'
print(my_str[::-1]) # dlrow olleH

my_str = 'Hello World'

# upper
uppercase_str = my_str.upper()
print(uppercase_str)  # HELLO WORLD

# lower
lowercase_str = my_str.lower()
print(lowercase_str)  # hello world

my_str_2 = '  Hello World  '

# strip
strip_str = my_str_2.strip()
print(my_str_2)  # '  Hello World  '
print(strip_str)  # 'Hello World'

my_str_3 = 'hello world'

# replace
replaced_my_str = my_str.replace('hello', 'hi')
print(replaced_my_str)  # hi world

my_list = ['hello', 'world']

#join
joined_my_str = ' '.join(my_list)
print(joined_my_str)  # hello world

my_str = 'hello world'

# startswith
starts_with_hello = my_str.startswith('hello')
print(starts_with_hello)  # True

my_str = 'hello world'

# endswith
ends_with_world = my_str.endswith('world')
print(ends_with_world)  # True

my_str = 'hello world'

# find
world_index = my_str.find('world')
print(world_index)  # 6

my_str = 'hello world'

# count
o_count = my_str.count('o')
print(o_count)  # 2

my_str = 'hello world'

# capitalize
capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)  # Hello world

my_str = 'hello world'

# isupper
is_all_upper = my_str.isupper()
print(is_all_upper)  # False

my_str = 'hello world'

# islower
is_all_lower = my_str.islower()
print(is_all_lower)  # True

my_str = 'hello world'

# title
title_case_my_str = my_str.title()
print(title_case_my_str)  # Hello World