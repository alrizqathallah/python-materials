# Deklarasi Variabel
name = 'Alrizq'

# 2x = 10

# Multiple Variable
x, y, z = 10, 20, 30

print(x)
print(y)
print(z)

# Value for Multiple Variable
a = b = c = "free"

print(a)
print(b)
print(c)

# Format Variable
first_name = 'Alrizq'
last_name = 'Athallah'

# Variable Concatenation / Operation
full_name = first_name + " " + last_name

print(full_name)

# Local Variable
def my_function():
  y = 'Saya Lokal'   # Variabel Lokal
  print(y)
  
my_function()

# Global Variable
x = "Saya Global"

def my_function():
  y = "Saya Lokal"
  print(y)
  print(x)

my_function()

# Kata Kunci `global`
def my_function():
  global user_name 
  user_name = 'alrizqathallah'
  print(user_name)

my_function()

print('The username is: ' + user_name)

# String
full_name = 'Alrizq Athallah'
print(full_name)
print(type(full_name))

# Integer
age = 28
print(age)
print(type(age))


# Float
gpa = 3.52
print(gpa)
print(type(gpa))


# Boolean
is_student = True
print(is_student)
print(type(is_student))

# List
formula_one = ["Mercedez", "Ferrari", "Renault", "Aston Martin", "Honda"]
print(formula_one)
print(type(formula_one))

# Tuple
fifa_world_cup = (2006, 2010, 2014, 2018, 2022)
print(fifa_world_cup)
print(type(fifa_world_cup))

# Dictionary
user_data = {"username": "thebenkz", "points": 2000, "is_active": True}
print(user_data)
print(type(user_data))

# Sets
moto_gp = {"Ducati", "Honda", "Yamaha"}
print(moto_gp)
print(type(moto_gp))

# None
x = None
print(x)
print(type(x))

# Casting
x = int(1)     # x akan menjadi 1
y = int(2.8)   # y akan menjadi 2 (desimal hilang)
z = int("3")   # z akan menjadi 3

x = float(1)     # x akan menjadi 1.0
y = float(2.8)   # y akan tetap 2.8
z = float("3")   # z akan menjadi 3.0
w = float("4.2") # w akan menjadi 4.2

x = str("s1") # x akan tetap "s1"
y = str(2)    # y akan menjadi "2"
z = str(3.0)  # z akan menjadi "3.0"