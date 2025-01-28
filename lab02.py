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
print(f"""
The sum of age and 5: {age + 5:d} 
The difference between height and 4: {height - 4}
The product of age and height: {age * height}
The quotient of height and 2: {height / 2}
The remainder of age divided by 3: {age % (age + 1)}
Age raised to the power of 2 (squared): {age ** 2}
""")

# Part 4: Temperature Conversion
fahrenheit = int(input("Enter the current temperature in Fahrenheit:"))
celsius = (fahrenheit - 32) * 5/9

print(f"""
Celsius: {celsius:.0f}°C
Fahrenheit: {fahrenheit}°F
""")

# version but with Celsius as an input.
cel = int(input("Enter the current temperature in Celsius:"))
fahr = (cel * 1.8) + 32

print(f"""
Celsius: {cel}°C
Fahrenheit: {fahr:.0f}°F
""")

