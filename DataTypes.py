age = 20
is_adult = age >= 18
print(is_adult)
print(type(is_adult))

age = 20
price = 99.99
name = "Ali"
active = True
print(type(age))
print(type(price))
print(type(name))
print(type(active))

age = input("Enter you age: ") # default input type: string
print(f"Your age is: {age}")
print(type(age))

age = input("Enter you age: ") 
print(type(age))
age = int(age)
print(f"Your age is: {age}")
print(type(age))

age = int(input("Enter age: "))
print(type(age))

height = float(input("Enter height: "))
print(type(height))

#greet = int('hello')

#pi = int('3.14')
#val = '20' + 5

val = bool('a')
print(val)
print(type(val))
