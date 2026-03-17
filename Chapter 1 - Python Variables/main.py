# Membuat Variabel
name = 'Alice'   # <str>
age = 25         # <int>
height = 1.68    # <float>

# Mengecek tipe data varibel
x = 10
print(type(x))        # <class 'int'>

y = 3.14
print(type(y))        # <class 'float'>

name = 'Alice'
print(type(name))     # <class 'str'>

flag = False
print(type(flag))     # <class 'bool'>'

# Dynamic Typing
value = 10       # int
print(value)

value = 'ten'   # int
print(value)

# Multiple Assignment
a, b, c = 5, 10, 15
print(a)
print(b)
print(c)

x = y = z = 10
print(x, y, z)

a, b = 10, 20
print(a, b)   # 10 20

a, b = b, a   # swap
print(a, b)   # 20 10

# Konversi Tipe (Casting)
# String to integer
num_str = "123"
num_int = int(num_str)
print(num_int + 1)   # 124

# Integer to float
x = 5
x_float = float(x)
print(x_float)       # 5.0

# Float to integer (truncates decimal)
pi = 3.14159
approx = int(pi)
print(approx)        # 3

# Number to string
age = 30
message = "I am " + str(age) + " years old."
print(message)       # I am 30 years old.

# Konstanta (Constants)
PI = 3.14159
MAX_SIZE = 100
DEFAULT_COLOR = "blue"

# Menggunakan `input()`
name = input('What is your name? ')
print('Hello, ' + name + '!')

age_str = input("How old are you? ")
age = int(age_str)   # convert to int
next_year = age + 1
print("Next year you will be", next_year)

# Menggunakan F-String
name = "Bob"
age = 22
print(f"{name} is {age} years old.")