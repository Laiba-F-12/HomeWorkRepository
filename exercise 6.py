Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# create an empty shopping cart
>>> shopping_cart = []
# add milk, bread and eggs to the cart
>>> shopping_cart.append('milk')
>>> shopping_cart.append('bread')
>>> shopping_cart.append('eggs')
# extend cart by adding butter and cheese
>>> shopping_cart.extend(['butter', 'cheese'])
>>> print(shopping_cart)
['milk', 'bread', 'eggs', 'butter', 'cheese']
