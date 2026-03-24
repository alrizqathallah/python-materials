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

