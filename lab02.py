import math

# part 1
name = "John Doe"
age = 200
height = 5 + (7/12)
favourite_colour = "Green"

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

# part 2
print(math.sqrt(age))

sin = math.sin(height)
cos = math.cos(height)
print(sin, cos)

# part 3

a = age + 5
b = height - 4
c = age * height
d = height / 2
e = height // 3

