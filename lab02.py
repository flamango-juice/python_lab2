import math

# Part 1: Variables and Assignments

# 1.1
name = "John Doe"
age = 200
height = 5 + (7/12)
favourite_colour = "Green"

# 1.2
print(name)
print(age)
print(height)
print(favourite_colour)

print(name, age, height, favourite_colour)

print(f"Hello! {favourite_colour} is my favourite colour!")
print(f"I am {height:2f} ft tall.")

print(f"""
    Name: {name}
    Age: {age}
    Height: {height}
    Favorite color: {favourite_colour}
""")

#1.3
rad = int(input("Enter a value:"))
circle_area = math.pi * (rad ** 2)
print(round(circle_area,1))
print(f"The area of a circle with the radius of {rad} is {circle_area}!")

# Part 2: Statements and Modules
print(math.sqrt(age))

sin = math.sin(height)
cos = math.cos(height)
print(sin, cos)

# Part 3: Expressions and Operators
a = age + 5
b = height - 4
c = age * height
d = height / 2
e = (height / 3) - (height // 3)
f = age**2
print(a,b,c,d,e,f)