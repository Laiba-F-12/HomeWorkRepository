Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# define the range of numbers from 0 to 10
>>> numbers = range(11)
# filter out only the even numbers from the range
>>> even_numbers = [x for x in numbers if x % 2 == 0]
>>> print(even_numbers)
[0, 2, 4, 6, 8, 10]
# Using list comprehension to create a list of squares of all even numbers from 0 to 10
>>> squares_of_evens = [x**2 for x in numbers if x % 2 == 0]
# print the resulting list
>>> print(squares_of_evens)
[0, 4, 16, 36, 64, 100]
