# String
my_str1 = 'Hello'
my_str2 = "Hello"

# Multiline String
my_str_3 = """Multiline
string"""
my_str_4 = '''Another
multiline
string'''

# Opposite Symbol
msg = "It's a sunny day"
quote = 'She said, "Hello World!"'

# Escape Sequence
msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""

# Operator `in`
my_str = 'Hello world'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False

# `len()` function
my_str = 'Hello world'
print(len(my_str))  # 11

# String Index
my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w

# String is Immutable
greeting = 'hi'
greeting = 'hello'
print(greeting) # hello

# String Concatenation
my_str_1 = 'Hello'
my_str_2 = "World"

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) # Hello World

# TypeError
name = 'John Doe'
age = 26

name_and_age = name + age
print(name_and_age) # TypeError: can only concatenate str (not "int") to str

# str() Function
name = 'John Doe'
age = 26

name_and_age = name + str(age)
print(name_and_age) # John Doe26

# Assigment Operator
name = 'John Doe'
age = 26

name_and_age = name  # Start with the name
name_and_age += str(age)  # Append the age as string

print(name_and_age)  # John Doe26

# String Slicing
# string[start:stop]
my_str = 'Hello world'

print(my_str[1:4])  # ell

print(my_str[:7])   # Hello w
print(my_str[8:])   # rld
print(my_str[:])   # Hello world
print(my_str[0:11:2])   # Hlowrd
print(my_str[::-1])   # dlrow olleH

# String Method

# upper()
my_str = 'hello world'

upper_my_str = my_str.upper()
print(upper_my_str)   # HELLO WORLD

# lower()
my_str = 'Hello World'

lowercase_my_str = my_str.lower()
print(lowercase_my_str)   # hello world

# strip()
my_str = '  hello world  '

trimmed_my_str = my_str.strip()
print(trimmed_my_str)   # "hello world"

# replace()
my_str = 'hello world'

replaced_my_str = my_str.replace('hello', 'hi')
print(replaced_my_str)   # hi world

# split()
my_str = 'hello world'

split_words = my_str.split()
print(split_words)   # ['hello', 'world']

# join()
my_list = ['hello', 'world']

joined_my_str = ' '.join(my_list)
print(joined_my_str)

# startswith()
my_str = 'hello world'

starts_with_hello = my_str.startswith('hello')
print(starts_with_hello)   # True

# endswith()
my_str = 'hello world'

ends_with_world = my_str.endswith('world')
print(ends_with_world)   # True

# find()
my_str = 'hello world'

world_index = my_str.find('world')
print(world_index)   # 6

# count()
my_str = 'hello world'

o_count = my_str.count('o')
print(o_count)   # 2

# capitalize()
my_str = 'hello world'

capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)  # Hello world

# isupper()
my_str = 'hello world'

is_all_upper = my_str.isupper()
print(is_all_upper)  # False

# islower()
my_str = 'hello world'

is_all_lower = my_str.islower()
print(is_all_lower)  # True

# title()
my_str = 'hello world'

title_case_my_str = my_str.title()
print(title_case_my_str)  # Hello World