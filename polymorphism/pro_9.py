class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Overload +
    def __add__(self, other):
        # Combine marks and make a new student with name combined
        return Student(self.name + "&" + other.name, self.marks + other.marks)

    # Overload ==
    def __eq__(self, other):
        return self.marks == other.marks

    # Overload >
    def __gt__(self, other):
        return self.marks > other.marks

    # Overload print()
    def __str__(self):
        return f"Name: {self.name}, Marks: {self.marks}"


# Testing
s1 = Student("Rajan", 90)
s2 = Student("Amit", 85)

# Add marks
s3 = s1 + s2
print(s3)          # Name: Rajan&Amit, Marks: 175

# Compare equality
print(s1 == s2)    # False

# Compare greater
print(s1 > s2)     # True



# 🔹 What is __str__ in Python?

# __str__ is a special (magic/dunder) method.

# It defines how an object should be represented as a string — basically, what you see when you do:

# print(object)


# If you don’t define __str__, Python shows something like:

# <__main__.Vector object at 0x7f4d2c0>


# This is the memory address of the object — not human-friendly.

# 🔹 Why we need __str__

# Think about this:

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# v1 = Vector(2, 3)
# print(v1)


# Output without __str__:

# <__main__.Vector object at 0x7f4d2c0>


# Looks confusing

# You can’t see x and y

# Not helpful if you want to read or debug

# Now, define __str__:

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"({self.x}, {self.y})"

# v1 = Vector(2, 3)
# print(v1)


# Output with __str__:

# (2, 3)


# ✅ Much easier to understand

# 🔹 How Python Uses __str__

# When you do:

# print(v1)


# Python internally calls:

# v1.__str__()


# So whatever string you return from __str__ is what gets printed



