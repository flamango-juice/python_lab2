import math

# Part 1: Variables and Assignments

# 1.1
name = "John Doe"
age = 67
height = 5 + (7/12)
favourite_colour = "Green"

# 1.2
print(name)
print(age)
print(height)
print(favourite_colour)

print(name, age, height, favourite_colour)

print(f"Hello! {favourite_colour} is my favourite colour!")
print(f"I am {height:.2f} ft tall.")

print(f"""
    Name: {name}
    Age: {age}
    Height: {height}
    Favorite color: {favourite_colour}
""")

#1.3

rad = 5
circle_area = math.pi * (rad ** 2)
print(round(circle_area,1))
print(f"The area of a circle with the radius of {rad} is {circle_area:.1f}!")

# Part 2: Statements and Modules
# 2.2
print(f"The square root of my age is {math.sqrt(age):.2f}")

# 2.3
print(f"""
    The sine of {height:.2f}: {math.sin(height):.2f}
    The cosine of {height:.2f}: {math.cos(height):.2f}
""")

# Part 3: Expressions and Operators
a = age + 5 # The sum of age and 5.
b = height - 4 # The difference between height and 4.
c = age * height # The product of age and height.
d = height / 2 # The quotient of height and 2.
e = height % 3 # The remainder of age divided by 3.
f = age ** 2 # age raised to the power of 2.
print(f"""
    {a:d}
    {b:.2f}
    {c:.2f}
    {d:.2f}
    {e:.2f}
    {f:d}
""")

# Part 4: Temperature Conversion
fahrenheit = int(input("Enter the current temperature in Fahrenheit:"))
celsius = (fahrenheit - 32) * 5/9
print(f"""
Celsius: {celsius:.0f}°C
Fahrenheit: {fahrenheit}°F
""")


