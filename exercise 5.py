Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# list of numbers
>>> numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# loop through the list and print squared numbers
>>> for value in numbers:
...     print(value ** 2)
...     squared_numbers = [value ** 2 for value in numbers]
... 
...     
1
4
9
16
25
36
49
64
81
100
