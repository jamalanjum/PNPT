#FUNCTIONs

def who_am_i(): #this is a function without parameters
    name = "Jamal" #local variable
    age = 30
    print("My name " + name + " and I am " + str(age) + " years old.")

who_am_i()

def add_one_hundred(num):
    print(num + 100)

add_one_hundred(100)

def add(x,y):
    print(x + y)

add(7,7)

def multiply(x,y):
    return x * y

multiply(7,7)
print(multiply(7,7))

def square_root(x):
    print(x ** .5)

square_root(64)

def nl(): #newline 
    print('\n')

nl()